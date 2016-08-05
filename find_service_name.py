# Chapter-1.5 通过指定的端口和协议找到服务名
import socket


def find_service_name(port=input("Enter the service port: "), protocol=input("Enter the service protocol: ")):
    try:
        port = int(port)
        serv_name = socket.getservbyport(port, protocol)
        print("Port: %s => Service Name: %s" % (port, serv_name))

if __name__ == "__main__":
    find_service_name()
