# UDP receiver
# Simple UDP server that prints sequence numbers from received messages.

import socket

port = 12000

def udp_receiver() -> None:
    '''Receive UDP messages and print sequence numbers.'''
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(("", port))
    print("Ready to receive messages...")

    try:
        while True:
            msg, _ = sock.recvfrom(1500)
            try:
                sequence_number = int(msg.decode().split(";")[0])
                print(f"Received message {sequence_number}")
            except (ValueError, IndexError):
                print("Received unexpected message format")
    except KeyboardInterrupt:
        print("Receiver stopped by user.")
    except socket.error as e:
        print(f"Socket error: {e}")
    finally:
        sock.close()

if __name__ == "__main__":
    udp_receiver()
