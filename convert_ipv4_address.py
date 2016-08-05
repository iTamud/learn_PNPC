# Chapter-1.4 将IPv4地址转换成不同的格式
import socket
from binascii import hexlify


def convert_ipv4_address(ip_addr=input("Enter the IP address to be converted: ")):
    packed_ip_address = socket.inet_aton(ip_addr)
    unpacked_ip_address = socket.inet_ntoa(packed_ip_address)
    print("IP Address: %s => Packed: %s, Unpacked: %s" % (ip_addr, hexlify(packed_ip_address), unpacked_ip_address))

if __name__ == "__main__":
    convert_ipv4_address()
