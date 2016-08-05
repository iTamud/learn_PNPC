# 套接字服务器程序中使用FokingMixin类
import os
import socket
import threading
import socketserver

SERVER_HOST = 'localhost'
SERVER_PORT = 0
BUF_SIZE = 1024
ECHO_MSG = 'Hello echo server!'


class ForkingClient():
    def __init__(self, ip, port):
        self.sock = socket.socket()
        self.sock.connect((ip, port))

    def run(self):
        current_process_id = os.getpid()
        print('PID %s Sending echo message to the server: "%s"' % (current_process_id, ECHO_MSG))
        sent_data_length = self.sock.send(ECHO_MSG.encode())
        print('Sent: %d characters, so far...' % sent_data_length)
        response = self.sock.recv(BUF_SIZE)
        print('PID %s received: %s' % (current_process_id, response[5:].decode()))

    def shutdown(self):
        self.sock.close()


class ForkingServerRequestHandler(socketserver.BaseRequestHandler):
    def handler(self):
        data = self.request.recv(BUF_SIZE)
        current_process_id = os.getpid()
        response = 'PID %s received: %s' % (current_process_id, data)
        print("Server sending response [current_process_id: data] = [%s]" % response)
        self.sock.send(response.encode())
        return


class ForkingServer(socketserver.ForkingMixIn, socketserver.TCPServer):
    pass


def main():
    server = ForkingServer((SERVER_HOST, SERVER_PORT), ForkingServerRequestHandler)
    ip, port = server.server_address
    server_thread = threading.Thread(target=server.serve_forever)
    server_thread.setDaemon(True)
    server_thread.start()
    print('Server loop running PID: %s' % os.getpid())
    client1 = ForkingClient(ip, port)
    client1.run()

    client2 = ForkingClient(ip, port)
    client2.run()

    server.shutdown()
    client1.shutdown()
    client2.shutdown()
    server.socket.close()

if __name__ == '__main__':
    main()
