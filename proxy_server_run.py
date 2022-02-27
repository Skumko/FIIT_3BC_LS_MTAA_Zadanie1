import socketserver
import socket
import sys
import time
import logging

import sipfullproxy

# sipfullproxy lib is a part of GNU General Public License
# ***************************************************************************************
#    Title: PySipFullProxy
#    Author: Philippe THIRION (tirfil)
#    Date: 19.02.2022
#    Code version: 1.0
#    Availability: https://github.com/tirfil/PySipFullProxy/blob/master/sipfullproxy.py
#
# **************************************************************************************


def logging_setup():
    logging.basicConfig(format='%(asctime)s:%(message)s', filename='proxy_server.log', level=logging.INFO,
                        datefmt='%H:%M:%S')
    logging.info(time.strftime("%a, %d %b %Y", time.localtime()))


def main_test():
    logging_setup()

    hostname = socket.gethostname()
    ipaddress = socket.gethostbyname(hostname)

    if ipaddress == "127.0.0.1":
        ipaddress = sys.argv[0]

    logging.info("SERVER RUNNING --> HOSTNAME: " + hostname + " <<<>>> IP_ADDRESS: " + ipaddress + "\n")
    print(hostname, ipaddress)

    # setting up global variable with accordance to server implementation
    sipfullproxy.recordroute = f"Record-Route: <sip:{ipaddress}:{sipfullproxy.PORT};lr>"
    sipfullproxy.topvia = f"Via: SIP/2.0/UDP {ipaddress}:{sipfullproxy.PORT}"

    # creating a socketserver Server object, that will take logic implemented in sipfullproxy
    server = socketserver.UDPServer((ipaddress, sipfullproxy.PORT), sipfullproxy.UDPHandler)
    server.serve_forever()


if __name__ == '__main__':
    main_test()
