from twisted.internet.protocol import ClientFactory
from twisted.protocols.basic import LineOnlyReceiver
import sys
from PyQt5 import QtWidgets, QtGui, QtCore                                    # Импорт виджета
import design                                                   # Импорт кода с design

class ConnectorProtocol(LineOnlyReceiver):                      # При подключении записыват себя в окно, декодирует и отправляет в plainTextEdit
    factory: 'Connector'
    window: 'ChatWindow'

    def connectionMade(self):
        self.factory.window.protocol = self
        self.factory.window.plainTextEdit.appendPlainText("Conected")           # Информация об установленном соединении

    def lineReceived(self, line):
        message = line.decode()
        if message == 'Login уже существует. Введите верный пароль.':
            window.vis()
        self.factory.window.plainTextEdit.appendPlainText(line.decode())        # Добавить текст и сразу декодировать

class Connector(ClientFactory):                                 # При инициализации записывается в окно
    protocol = ConnectorProtocol
    window: 'ChatWindow'

    def __init__(self, app_window):
        super().__init__()
        self.window = app_window                                # Делаем связь между коннектором и окном

class ChatWindow(QtWidgets.QMainWindow, design.Ui_MainWindow):
    reactor = None                                              # Реактор нужен для управления всем процессом, запоминает кто такой реактор
    protocol: ConnectorProtocol                                 # Протокол чтобы отправлять сообщения, запоминает кто такой протокол

    def __init__(self):                                         # Конструктор, который вызывается автоматически при создании нового экземпляра объекта
        super().__init__()
        self.setupUi(self)
        self.init_handlers()                                    # Вызов Init handlers.

    def vis(self):
        self.lineEdit_2.setVisible(True)                        # При неудачном логине, поля вновь отображаются
        self.lineEdit_3.setVisible(True)
        self.label.setVisible(True)
        self.label_2.setVisible(True)
        self.lineEdit.setEnabled(False)

    def init_handlers(self):
        self.lineEdit.setEnabled(False)
        self.pushButton.clicked.connect(self.send_message)      # Действие по нажатию кнопки (настройка кнопки путём указания туда функции)
        self.lineEdit.returnPressed.connect(self.pushButton.click)
        self.lineEdit_2.returnPressed.connect(self.pushButton.click)
        self.lineEdit_3.returnPressed.connect(self.pushButton.click)

    def closeEvent(self, event):
        self.reactor.callFromThread(self.reactor.stop)              # При закрытии формы останавливается реактор

    def send_message(self):
        message = self.lineEdit.text()                              # Обращаемся к полю ввода сообщения и сохранения в короткую переменную
        message2 = self.lineEdit_2.text()
        message3 = self.lineEdit_3.text()
        if len(message) > 0:
            self.plainTextEdit.appendPlainText('You: ' + message)   # Вывод в PlainText, того что ввели.
            self.protocol.sendLine(message.encode())
            self.lineEdit.clear()
            self.lineEdit.setFocus()
        if len(message2) > 0 and len(message3) > 0:
            message2 = "login:" + message2 + " password:" + message3
            self.protocol.sendLine(message2.encode())
            self.lineEdit_2.clear()
            self.lineEdit_3.clear()
            self.lineEdit_2.setVisible(False)
            self.lineEdit_3.setVisible(False)
            self.label.setVisible(False)
            self.label_2.setVisible(False)
            self.lineEdit.setEnabled(True)

app = QtWidgets.QApplication(sys.argv)
import qt5reactor                                               # Запись импортирует мост между Qt и Реактором

window = ChatWindow()                                           # Создаём окно, вызываем show
window.show()

qt5reactor.install()                                            # Устанавливаем мост
from twisted.internet import reactor                            # Импортируем реактор
reactor.connectTCP(                                             # Конектимся по TCP и передаём window конструктор
    "192.168.0.102",
    1234,
    Connector(window)
)

window.reactor = reactor
reactor.run()