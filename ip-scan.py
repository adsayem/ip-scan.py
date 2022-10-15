import socket 
domain = input("enter your domain name  :")
ip = socket.gethostbyname(domain)
print(ip)