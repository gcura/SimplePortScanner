import optparse
import socket
from socket import *

from threading import *

def connScan(Host, tgtPort):
    try:
        #initiates TCP connection
        connSkt = socket(AF_INET, SOCK_STREAM)
        connSkt.connect((Host, tgtPort))
        print('[+] Port %d: Open'  % (tgtPort))
        connSkt.close()
    except:
        pass

def portScan(Host, tgtPorts):
    try:
        tgtIP = gethostbyname(Host)
    except:
        print("[-] Cannot resolve '%s': Unknown host" % (Host))
        return


    try:
        tgtName = gethostbyaddr(tgtIP)
        print('\n[+] Scan Results for : ' + tgtName[0])
    except:
        print('\n[+] Scan Results for : ' + tgtIP)
    setdefaulttimeout(1)
    #start a new thread when scanning for each port (makes port scan run a bit faster)
    #calls connScan function
    for tgtPort in tgtPorts:
        t = Thread(target=connScan, args=(Host, int(tgtPort)))
        t.start()



def main():
    parser = optparse.OptionParser('usage %prog -H ' +\
    '<target host> ')

    parser.add_option('-H', dest='Host', type='string', \
        help='specify target host')



    (options, args) = parser.parse_args()
    Host = options.Host
    #scans all ports
    tgtPorts = range(65535)
    

    #if there is no host option in cmdline
    if(Host == None):
        print(parser.usage)
        exit(0)
    portScan(Host, tgtPorts)

if __name__ == '__main__':
    main()
