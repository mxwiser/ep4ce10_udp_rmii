import socket

FPGA = ("192.168.15.14", 6000)   # 目标IP、目标端口(随意)
SRC_PORT = 6000                  # 本机发送用的源端口

tx = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
tx.bind(("0.0.0.0", SRC_PORT))
tx.sendto(b"hello fpga", FPGA)

# 你的设计回包发到"源端口+1"，所以监听 5001
rx = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
rx.bind(("0.0.0.0", SRC_PORT + 1))
rx.settimeout(2)
try:
    data, addr = rx.recvfrom(2048)
    print("收到回包:", data, "来自:", addr)
except socket.timeout:
    print("超时，无回包")