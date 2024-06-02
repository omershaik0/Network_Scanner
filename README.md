# Network Scanning Tool

## Description

This is a network scanning tool that identifies active hosts on a specified network by sending ARP requests. The tool is built using Python and utilizes libraries such as `scapy` for network probing and `colorama` for colored output.

## Features

- **Network Scanning**: Probes the target network IP range to identify active hosts.
- **Colored Output**: Uses `colorama` to display results in color for better readability.
- **Customizable Colors**: Allows customization of output colors using RGB values.
- **Error Handling**: Catches and displays exceptions that occur during execution.
- **Command-Line Interface**: Easy to use with command-line arguments for specifying the target network.

## Requirements

- Python 3.x
- Required Python packages:
  - `argparse`
  - `scapy`
  - `colorama`
  - `cryptography`

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/omershaik0/Network_Scanner.git
   cd Network_Scanner
   ```

## Usage

1. Run the script with the target network IP range as an argument:
   ```sh
   sudo python3 network_scanner.py -t <target_network_range>
   ```

   Replace `<target_network_range>` with the IP range you want to scan, e.g., `192.168.1.0/24`.

2. Example:
   ```sh
   sudo python3 network_scanner.py -t 192.168.1.0/24
   ```

## Script Flowchart

 ![ Alt Text](https://github.com/omershaik0/Network_Scanner/blob/main/network_scanner_flowchart.png)

## In Action

 ![ Alt Text](https://github.com/omershaik0/Network_Scanner/blob/main/network_scanner.gif)

## Disclaimer

Use Ethically :)

---
