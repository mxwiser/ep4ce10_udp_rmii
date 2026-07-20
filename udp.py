import socket
import time
fpga_ip = "192.168.15.14"
fpga_port = 8080

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("192.168.15.13", 8081))
sock.settimeout(2)

while True:
    data = b"123456"

    sock.sendto(data, (fpga_ip, fpga_port))
    print("send:", data)
    time.sleep(0.01)
    try:
        rx, addr = sock.recvfrom()
        print("recv:", rx, "from", addr)
    except:
        print("timeout")