import warnings
from cryptography.utils import CryptographyDeprecationWarning
warnings.filterwarnings("ignore", category=CryptographyDeprecationWarning)

import argparse
import sys
from scapy.all import srp
from scapy.layers.l2 import ARP, Ether
from colorama import init, Fore, Back, Style

init()
# Colors inside variables
r, g, b = 255, 165, 0
def rgb(r, g, b):
    return f'\033[38;2;{r};{g};{b}m'
background = Back.CYAN + Fore.BLACK
magenta = Fore.MAGENTA
green = Fore.GREEN
red = Fore.RED
cyan = Fore.CYAN
blue = Fore.BLUE
yellow = Fore.YELLOW
yellow_bright = rgb(255, 255, 0)
violet = rgb(238, 130, 238)
white = Fore.WHITE
green_bright = rgb(0, 255, 0)
reset = Style.RESET_ALL


script_name = sys.argv[0]

arguments = argparse.ArgumentParser(description="This is Network Scanning tool", usage=f"python3 {script_name} -t target network range")
arguments.add_argument('-t', "--target", help="Enter the Target Network IP range", required=True)
args = arguments.parse_args()

# Main variables
target_network = args.target
ether_frame = Ether(dst='ff:ff:ff:ff:ff:ff')
arp_frame = ARP(pdst=target_network)
network_probe = ether_frame/arp_frame

try:
    online_clients = []
    probe_result = srp(network_probe, timeout=3, verbose=0) #result format [answered[sent, received], unanswered]
    answered_probes = probe_result[0]
    for sent, received in answered_probes:
        online_clients.append({'ip': received.psrc, 'mac': received.hwsrc})
    print(f"\n{red}[{green}+{reset}{red}] Avaliable Hosts:{reset}\n")
    print(f"{yellow}IP "+ " "*20 +f" MAC{reset}")
    for client in online_clients:
        print('{}{}\t\t{}{}'.format(green, client['ip'], client['mac'], reset))
except Exception as e:
    print(e, " :(")
