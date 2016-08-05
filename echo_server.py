# 编写一个简单的回显服务器应用
import socket
import sys
import argparse

host = "localhost"
data_payload = 2048
backlog = 5


def echo_server(port):
    sock = socket.socket()
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_address = (host, port)
    print("Starting up echo server on host: %s port: %s" % server_address)
    sock.bind(server_address)
    sock.listen(backlog)
    while 1:
        print("Waiting to receive message from client")
        server, address = sock.accept()
        data = server.recv(data_payload)
        decoded_data = data.decode()
        if data:
            print("Data: %s" % decoded_data)
            server.send(data)
            print("Sent: %s back to %s" % (decoded_data, address))
        server.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Socket Server Example")
    parser.add_argument("--port", action="store", dest="port", type=int, required=True)
    given_args = parser.parse_args()
    port = given_args.port
    echo_server(port)
