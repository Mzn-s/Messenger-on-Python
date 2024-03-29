# Messenger-on-Python

Данный месенджер представляет собой окно общего чата пользователей.


* Сетевое взаимодействие осуществляется с использованием Twisted.

* Данные пользователей (логины, пароли, история переписок) хранятся в базе данных MySQL 5.7.

* Графичемкий интерфейс реализован с использованием PyQt5.

  Основная логика приложения написана по интенсиву Skillbox. 
  
  От себя добавлены: База данных для хранения информации, запоминание пользователей, авторизация по логину и паролю, изменена и дополнена графическая форма.
  В качестве тестового стенда приложения использовались:
  
  * Server: CentOS 7.  
  * Client: MS Windows 10.

## Описание файлов:


файл            | Описание файла
----------------|----------------------
Client.py       | Основной файл, запускаемый на удалённой машине - сервере.
Client.py       | Файл, производящий подключение к серверу и содержащий команды работы графической части.
normalize.css   | Нормалайзер CSS от Nicolas Gallagher
design.py       | Py файл характеристик ui файла
design.ui       | Ui файл Qt Designer
DMesDB.sql      | Дамп файл БД

## Скриншоты:
![alt text](https://github.com/Mzn-s/Messenger-on-Python/blob/master/Pictures/LoginScreen.JPG)
![alt text](https://github.com/Mzn-s/Messenger-on-Python/blob/master/Pictures/DialogScreen.JPG)
