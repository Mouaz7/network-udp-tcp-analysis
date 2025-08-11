# TCP sender
# Simple TCP client that sends sequence-numbered messages at a fixed rate.

import socket
import time
import sys

ip = "193.11.184.92"
port = 12000
size = 1450
total_messages = 500
rate = 30  # messages per second

def send_tcp_messages(ip_addr: str, port_num: int, message_size: int, total: int, msgs_per_sec: int) -> None:
    '''Send a series of TCP messages with a fixed rate and size.'''
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((ip_addr, port_num))

    packet_interval = 1.0 / msgs_per_sec
    start = time.time()

    try:
        for message_number in range(10001, 10001 + total):
            header = f"{message_number};"
            payload = "A" * (message_size - len(header) - len("####"))
            message = header + payload + "####"
            sock.sendall(message.encode())
            print(f"Sent message {message_number}")
            time.sleep(packet_interval)
    except KeyboardInterrupt:
        print("\nTerminating program...")
    finally:
        sock.close()
        end = time.time()
        print(end - start)
        sys.exit()

if __name__ == "__main__":
    send_tcp_messages(ip, port, size, total_messages, rate)
