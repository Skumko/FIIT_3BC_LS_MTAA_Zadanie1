import proxy
import socketserver
import socket
import sys
import time
import logging


def logging_setup():
    logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s', filename='proxy_server.log', level=logging.INFO,
                        datefmt='%H:%M:%S')
    logging.info(time.strftime("%a, %d %b %Y %H:%M:%S ", time.localtime()))


def main_test():
    # logging_setup()

    hostname = socket.gethostname()
    ipaddress = socket.gethostbyname(hostname)
    if ipaddress == "127.0.0.1":
        ipaddress = sys.argv[0]

    logging.info("HOSTNAME: "+hostname + "IP_ADDRESS: "+ipaddress)

    proxy.recordroute = f"Record-Route: <sip:{ipaddress}:{proxy.PORT};lr>"
    proxy.topvia = f"Via: SIP/2.0/UDP {ipaddress}:{proxy.PORT}"
    server = socketserver.UDPServer((proxy.HOST, proxy.PORT), proxy.UDPHandler)
    server.serve_forever()


if __name__ == '__main__':
    main_test()
