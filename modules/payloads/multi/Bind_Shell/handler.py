import socket

addr = input("int4 [Enter Rhost] >")
port = 4444

server_address = (addr, port)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.getsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)\

s.connect(server_address)
print(f"connected to {addr}")
server_name = s.recv(1024).decode()

while True:
    msg = input("int4 [" + server_name + "] >")
    if len(msg) > 0:
        s.send(msg.encode())
        asd = s.recv(4096).decode()
        print(f"{asd}", end="")

s.close()