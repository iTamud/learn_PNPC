# Chapter-1.6 主机字节序和网络字节序之间相互转换
import socket


def convert_integer(data=int(input("Enter the data to be converted: "))):
    # 32-bit
    print("Original: %s => Long host byte order: %s, Network byte order: %s" % (data, socket.ntohl(data), socket.htonl(data)))
    # 16-bit
    print("Original: %s => Long host byte order: %s, Network byte order: %s" % (data, socket.ntohs(data), socket.htons(data)))

if __name__ == "__main__":
    convert_integer()
