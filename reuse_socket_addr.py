# 重用套接字地址
import socket
import sys


def reuse_socket_addr():
    # sock = socket.socket()

    # 获取旧的SO_REUSEADDR状态
    # old_state = sock.getsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR)
    # print("Old socket state: %s" % old_state)

    # 开启SO_REUSEADDR
    # sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # new_state = sock.getsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR)
    # print("New socket state: %s" % new_state)

    local_port = 8282

    srv = socket.socket()
    srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    srv.bind(("", local_port))
    srv.listen(1)

    print("Listening on port: %s" % local_port)
    while 1:
        # try:
        #     print("Tamud!")
        # except KeyboardInterrupt:
        #     print("Terminated!")
        #     break
        try:
            print("before blocking")
            connection, addr = srv.accept()
            print("Connected by %s:%s" % (addr[0], addr[1]))
        except KeyboardInterrupt:
            break
        except (socket.error, msg) as e:
            print("%s" % (e,))


if __name__ == "__main__":
    reuse_socket_addr()
