# UDP sender
# Simple UDP client that sends sequence-numbered messages at a fixed rate.
# Comments are in English and kept short.

import socket
import time
import sys

ip = "192.168.0.103"
port = 12000
size = 1460
total_messages = 62
rate = 10  # messages per second

def send_udp_messages(ip_addr: str, port_num: int, message_size: int, total: int, msgs_per_sec: int) -> None:
    '''Send a series of UDP messages with a fixed rate and size.'''
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    packet_interval = 1.0 / msgs_per_sec

    try:
        for message_number in range(10001, 10001 + total):
            header = f"{message_number};"
            payload = "A" * (message_size - len(header) - len("####"))
            message = header + payload + "####"
            sock.sendto(message.encode(), (ip_addr, port_num))
            print(f"Sent message {message_number}")
            time.sleep(packet_interval)
    except KeyboardInterrupt:
        print("\nTerminating program...")
    finally:
        sock.close()
        sys.exit()

if __name__ == "__main__":
    send_udp_messages(ip, port, size, total_messages, rate)
