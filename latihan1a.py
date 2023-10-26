import socket

host_name = socket.gethostname()
ip = socket.gethostbyname(host_name)
print("nama komputer =", host_name)
print("ip komputer =", ip)