# Chapter-1.7 设定并获取默认的套接字超时时间
import socket


def test_socket_timeout(timeout=int(input("Enter the new timeout: "))):
    skt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Default socket timeout: %s" % skt.gettimeout())
    skt.settimeout(timeout)
    print("Current socket timeout: %s" % skt.gettimeout())

if __name__ == "__main__":
    test_socket_timeout()
