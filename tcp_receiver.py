# TCP receiver
# Simple TCP server that prints sequence numbers from received messages.

import socket

port = 12000

def tcp_receiver() -> None:
    '''Receive TCP messages and print sequence numbers.'''
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(("", port))
    sock.listen(1)
    print(f"Listening for TCP connections on port {port}")
    connection, client_address = sock.accept()

    try:
        print(f"Connected to {client_address}")
        while True:
            msg = connection.recv(1500)
            if not msg:
                print("No more data from client.")
                break
            try:
                decoded = msg.decode()
                if ";" in decoded:
                    sequence_number = int(decoded.split(";")[0])
                    print(f"Received message {sequence_number}")
                else:
                    print("Received unexpected message format")
            except ValueError:
                print("Error: Received a non-integer sequence number.")
    except KeyboardInterrupt:
        print("Receiver stopped by user.")
    finally:
        connection.close()
        sock.close()

if __name__ == "__main__":
    tcp_receiver()
