import socket
import threading


def parser (parse):
    if parse[0] == '1' and parse[1] == 'SBER': #записываем цену текущего тика SiM0 в список ticks
        return parse

def service():
    sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    sock.bind(('127.0.0.1', 3587)) #Хост-этот компьютер, порт - 3587
    while True:
        data, client = sock.recvfrom(2048)
        data = parser(data.decode('utf-8').split(' '))
        if data == '<qstp>\n':  #строка приходит от клиента при остановке луа-скрипта в КВИКе
            break
        elif data:
            print(data) #Здесь вызываете свой парсер. Для примера функция: parser (parse)
            if float(data[4]) > 268.23:
                sock.sendto('I want to buy this ticket'.encode(), client)
            else:
                sock.sendto('Nothing'.encode(), client) # отправка сообщения если ничего делать клиенту не нужно
    sock.close()

#Запускаем сервер в своем потоке
t = threading.Thread(name='service', target = service)
t.start()
print("Запущен")
