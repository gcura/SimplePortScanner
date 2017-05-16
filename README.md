# SimplePortScanner
Python program that utilizes the TCP full connect scan to scan the top 1000 most common TCP ports on a host.

# Install
<pre> $ git clone https://github.com/gcura/SimplePortScanner.git</pre>

# Usage:
<pre>
python Simple_Port_Scanner.py -H 192.168.182.150

Options:
  -h, --help  show this help message and exit
  -H HOST     specify target host
</pre>

# Output

<pre>
[+] Scan Results for : 192.168.182.150
[+] Port 21: Open
[+] Port 22: Open
[+] Port 23: Open
[+] Port 25: Open
[+] Port 53: Open
[+] Port 80: Open
[+] Port 111: Open
[+] Port 139: Open
[+] Port 445: Open
[+] Port 512: Open
[+] Port 513: Open
[+] Port 514: Open
[+] Port 1524: Open
[+] Port 2049: Open
[+] Port 2121: Open
[+] Port 3306: Open
[+] Port 5432: Open
[+] Port 5900: Open
[+] Port 6000: Open
[+] Port 8009: Open
</pre>

# Requirments

Python v2.7 required. The program will not run in python v3.x
