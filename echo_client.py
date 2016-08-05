# 编写一个简单的回显服务器应用
import socket
import sys
import argparse

host = "localhost"


def echo_client(port):
    sock = socket.socket()
    server_address = (host, port)
    print("Connecting to host: %s port: %s" % server_address)
    sock.connect(server_address)

    try:
        message = "Test message. This will be echoed."
        print("Sending: %s" % message)
        message = message.encode()
        sock.sendall(message)
        amount_received = 0
        amount_expected = len(message)
        print("amount_expected: %s" % amount_expected)
        while amount_received < amount_expected:
            data = sock.recv(16)
            amount_received += len(data)
            print("amount_received: %s" % amount_received)
            print("Received: %s" % data.decode())
    except (socket.error, msg) as e:
        print("Socket Error: %s" % e)
    except (Exception, msg) as e:
        print("Other Exception: %s" % e)
    finally:
        print("Closing connection to the server")
        sock.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Socket Server Example")
    parser.add_argument("--port", action="store", dest="port", type=int, required=True)
    given_args = parser.parse_args()
    port = given_args.port
    echo_client(port)
