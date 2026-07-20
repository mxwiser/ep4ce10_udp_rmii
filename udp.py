import socket
import time
fpga_ip = "192.168.15.14"
fpga_port = 8090

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("192.168.15.13", 8081))
sock.settimeout(2)
sock.setblocking(False)
while True:
    data = b"Hello world! Make Altera Great Again!"
    sock.sendto(data, (fpga_ip, fpga_port))
    print("send:", data)
    try:
        rx, addr = sock.recvfrom(1024)
        print("recv:", rx, "from", addr)
    except:
        print("timeout")
    time.sleep(0.1)