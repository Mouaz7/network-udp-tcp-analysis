# Network UDP/TCP Analysis

## Overview
This repository contains Python implementations and analysis for a lab assignment (ET1524) focusing on network communication using UDP and TCP. The project includes sender and receiver programs for both protocols, along with detailed analysis based on measured performance.

## Contents
- **udp_sender.py** – UDP sender that transmits messages with sequence numbers at a controlled rate.
- **udp_receiver.py** – UDP receiver that listens for incoming datagrams, extracts sequence numbers, and measures packet rate.
- **tcp_sender.py** – TCP sender that transmits messages with sequence numbers using a reliable byte stream.
- **tcp_receiver.py** – TCP receiver that accepts incoming connections, reconstructs messages from the byte stream, and measures throughput.
- **Lab Analysis (PDF)** – Detailed explanation of test methodology, results, and conclusions.

## UDP Details
- Sequence numbers included in packet headers (`f"{sequence};"`).
- Packets terminated with `####`.
- Packet sizes close to MTU (1460 bytes for UDP).
- Tested at rates: 10 pps, 50 pps, and maximum (no sleep).
- Receiver uses `recvfrom(1500)` to handle UDP datagrams.

### Observations
- **10 pps**: Mostly stable; occasional minor deviation.
- **50 pps**: Stable initially, packet loss at higher load.
- **Max rate**: Very high burst; many packets dropped.

## TCP Details
- Packet size: 1450 bytes.
- Sender uses `sendall` to ensure complete transmission.
- Receiver reads with `recv(1500)` and reconstructs messages based on delimiter `####`.
- Tested at rates: 10 pps, 50 pps.

### Observations
- **10 pps**: Fully stable; no ordering issues.
- **50 pps**: Stable to some extent but retransmissions observed.

## Protocol Comparison
- **TCP**: Reliable, ordered delivery with retransmissions and acknowledgements.
- **UDP**: Faster, lightweight, but no delivery or ordering guarantees.

**Metaphor:**  
TCP = registered letter with receipt.  
UDP = postcard – fast but no guarantee.

## How to Run
1. Start receiver on one machine or terminal:
    ```bash
    python3 udp_receiver.py
    ```
    or
    ```bash
    python3 tcp_receiver.py
    ```

2. Start sender on another machine or terminal:
    ```bash
    python3 udp_sender.py
    ```
    or
    ```bash
    python3 tcp_sender.py
    ```

## Author
Mouaz7
