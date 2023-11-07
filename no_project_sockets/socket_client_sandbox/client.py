import socket

HOST = 'localhost'    # The remote host
PORT = 3587           # The same port as used by the server

data = "1 SBER some_index trade_num 278.5 1 3 7.11.2023 18:23:03.00"
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client:
    client.sendto(data.encode(), (HOST, PORT))
    data = client.recv(1024)
print('Received', repr(data))
