# 从网络时间服务器获取并打印当前时间
import ntplib
from time import ctime


def print_time(ntp_addr="pool.ntp.org"):
    ntp_client = ntplib.NTPClient()
    response = ntp_client.request(ntp_addr)
    print(ctime(response.tx_time))


if __name__ == "__main__":
    print_time()
