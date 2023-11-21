import socket
import random
import time


HOST = 'localhost'    # The remote host
PORT = 3587           # The same port as used by the server

base_string_stock = '1 SBER some_index trade_num {0:3.2f} 1 {1} 7.11.2023 18:23:03.00'

def format_strint_from_client() -> str:
    price = 258.01 + random.random()
    volume = random.randrange(10)
    return base_string_stock.format(price, volume)


with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client:
    while True:
        data = format_strint_from_client()
        client.sendto(data.encode(), (HOST, PORT))
        time.sleep(1)
        data = client.recv(1024)
        print('Received', repr(data.decode('utf-8')))
