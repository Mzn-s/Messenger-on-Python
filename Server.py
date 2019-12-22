from twisted.internet import reactor
from twisted.internet.protocol import ServerFactory, connectionDone
from twisted.protocols.basic import LineOnlyReceiver
import pymysql.cursors
import re

class Serverprotocol(LineOnlyReceiver):             # LineOnlyReceiver - протокол передачи текста.
    factory: 'Server'                               # Чтобы сервер протокол знал, что является его сервером
    login: str = None

    # Добавление в список новых клиентов при установленном соединении
    def connectionMade(self):
        self.factory.clients.append(self)

    # Удаление всего из списка при разрыве соединения
    def connectionLost(self, reason=connectionDone):
        self.factory.clients.remove(self)

    # Проверка имеющегося логина и пароля в БД. 1 - всё совпадает. 2 - совпал только логин. 3 - введённый логин пользователя свободен.
    def logins_sql(self, b, p):
        with self.factory.connection:
            cur = self.factory.connection.cursor()
            cur.execute("SELECT login, password FROM Logins")
            result = cur.fetchall()
            for x in range(len(result)):
                if b in result[x].values() and p in result[x].values():
                    return 1
                elif b in result[x].values() and p not in result[x].values():
                    return 2
            return 3

    # Выгрузка истории сообщений из БД.
    def send_history(self):
        with self.factory.connection:
            cur = self.factory.connection.cursor()
            cur.execute("SELECT `mail` FROM History")
            res = cur.fetchall()
            for user in self.factory.clients:
                if user is self and len(res)>=1:
                    for x in range (len(res)):
                        c1 = ' '.join(res[x].values())
                        user.sendLine(c1.encode())

    # Метод получения сообщения. bytes - строка,закодированная в специальный пакет данных, доступный для передачи по сети
    def lineReceived(self, line: bytes):
        content = line.decode()                                     # Декодирую сообщение.
        if not content.startswith("login:"):                        # Проверка на то, вводится логин или сообщение.
            content = f"От {self.login}: {content}"

            with self.factory.connection.cursor() as cursor:
                sql = "INSERT INTO `History` (`mail`) VALUES (%s)"  # Запись в БД сообщения.
                cursor.execute(sql, (content))
            self.factory.connection.commit()

            for user in self.factory.clients:
                if user is not self:
                    user.sendLine(content.encode())                 # Кодирую строчку при отправке
        else:
            if content.startswith("login:"):
                # Передача логина и пароля переменным:
                self.password = re.search('password:.*?(.+)', content).group(1)
                self.login = re.search('login:.*?(.+)(\s)', content).group(1)
                a = self.logins_sql(self.login, self.password)
                if a == 3:
                    with self.factory.connection.cursor() as cursor:
                        sql = "INSERT INTO `Logins` (`login`, `password`) VALUES (%s, %s)"   # Запись в БД нового пользователя.
                        cursor.execute(sql, (self.login, self.password))
                    self.factory.connection.commit()
                    self.sendLine("Welcome".encode())                                        # После тоrо как клиент авторизуется, то получит сообщение
                    self.send_history()
                elif a == 2:
                    self.sendLine("Login уже существует. Введите верный пароль.".encode())
                else:
                    self.sendLine("Welcome".encode())
                    self.send_history()
            else:
                self.sendLine("Invalid login".encode())


class Server(ServerFactory):
    protocol = Serverprotocol               # Ставим, чтобы сервер знал какой использовать протокол.
    clients: list                           # Список для запоминания пользователей.

    def startFactory(self):
        self.clients = []                   # При старте сервера инициализирую список с пустым значением

        self.connection = pymysql.connect(  # Соединение с БД.
        	host='localhost',
    		user='Admin',
    		password='Asap228!',
    		db='MesDB',
    		charset='utf8mb4',
    		cursorclass=pymysql.cursors.DictCursor)

        print('Server started')
    def stopFactory(self):
        print('Server closed')


reactor.listenTCP(1234, Server())           # Указываем ректору какой порт ему слушать на входящие подключения и что является сервером.
reactor.run()                               # Запуск реактора
