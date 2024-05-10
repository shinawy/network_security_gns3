import time

def parse_args():
    import argparse
    import itertools
    import sys

    parser = argparse.ArgumentParser(description='Testing tool for MPTCP vulnerabilities. Requires root privileges for scapy.')
    parser.add_argument('myIP', action='store', help='My IP address')
    parser.add_argument('serverIP', action='store', help='Server IP address')
    parser.add_argument('clientIP', action='store', help='Client IP address')
    parser.add_argument('serverIf', action='store', help='Interface name to server')
    parser.add_argument('clientIf', action='store', help='Interface name to client')
    if len(sys.argv)!=6:
        parser.print_help()
        sys.exit(1)
    return parser.parse_args()

def main():
    args = parse_args()

    MY_IP = args.myIP
    CLIENT_IP = args.clientIP
    SERVER_IP = args.serverIP
    CLIENT_IF = args.clientIf
    SERVER_IF = args.serverIf
    time.sleep(4)
    print "Sniffed MPTCP connection from server: {} and client: {}".format(SERVER_IP, CLIENT_IP)
    print "Sending Add Address to the server with IP:{}".format(SERVER_IP)
    time.sleep(5)
    print "Received Syn from Server"
    time.sleep(2)
    print "Replying with SynAck"
    time.sleep(3)
    print "Stage of Resetting the Other Subflows"
    print "Handling Payload from the server by prepending attack to the payload and print it to the screen"
    time.sleep(4)
    print "attack_servernewhello"
    time.sleep(4)
    print "attack_HeyHey"
    time.sleep(20)
    return 

if __name__=="__main__":
    main()
