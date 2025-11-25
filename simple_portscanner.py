import socket

def is_port_open(host, port):
    
    # Determine whether 'host' has the 'port' open

    # Creates a new socket
    s = socket.socket()
    s.settimeout(0.2)
    try:
        # Tries to connect to host using that port
        s.connect((host, port))
    except:
        # Cannot connect, port is closed
        return False
    else:
        # The connection was established, port is open
        return True

# Get the host from the user
host = input('Enter the host: ')
# Iterate over ports, from 1 to 1024
for port in range(1, 1024):
    if is_port_open(host, port):
        print(f'\033[32m[+] {host}:{port} is open\033[0m')
    else:
        print(f'\033[31m[!] {host}:{port} is closed\033[0m')