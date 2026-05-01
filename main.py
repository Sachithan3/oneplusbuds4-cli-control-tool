#!/usr/bin/env python3
"""
Oneplus buds 4 controller
(Does not work on windows)
(replace mac address with your address and you might have to change the RFCOMM channel as well)
Usage:
  python3 main.py [on|off|a(adaptive)|t(transparency)]
"""

import socket
import sys
import json

def load_mac():
    with open("config.json") as f:
        return json.load(f)["macadd"]


BUDS_MAC = load_mac()                 #REPLACE THIS WITH YOUR OWN MAC ADDRESS!!
RFCOMM_CHANNEL = 15

HELLO = bytes([0xAA, 0x07, 0x00, 0x00, 0x00, 0x01, 0x66, 0x00, 0x00])
REGISTER = bytes(
    [0xAA, 0x0C, 0x00, 0x00, 0x00, 0x85, 0x6A, 0x05, 0x00, 0x00, 0xA2, 0x5E, 0xEE, 0x69]
)
ANC_ON = bytes([0xAA, 0x0A, 0x00, 0x00, 0x04, 0x04, 0x26, 0x03, 0x00, 0x01, 0x01, 0x02])
ANC_OFF = bytes([0xAA, 0x0A, 0x00, 0x00, 0x04, 0x04, 0x26, 0x03, 0x00, 0x01, 0x01, 0x05])
TRANSPARENCY = bytes([0xAA, 0x0A, 0x00, 0x00, 0x04, 0x04, 0x24, 0x03, 0x00, 0x01, 0x01, 0x04])
ADAPTIVE = bytes([0xAA, 0x0B, 0x00, 0x00, 0x04, 0x04, 0x85, 0x04, 0x00, 0x01, 0x01, 0x00, 0x08])

MODES = {
    "on": ("ANC On", ANC_ON),
    "off": ("ANC Off", ANC_OFF),
    "t": ("Transparency", TRANSPARENCY),
    "a": ("Adaptive", ADAPTIVE),
}



def recv_packet(sock, timeout=3.0):
    sock.settimeout(timeout)
    try:
        return sock.recv(256)
    except socket.timeout:
        return None


def switch_mode(mode_key):
    mode_name, command = MODES[mode_key]
    sock = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
    try:
        sock.connect((BUDS_MAC, RFCOMM_CHANNEL))
        sock.sendall(HELLO)
        recv_packet(sock)
        sock.sendall(REGISTER)
        recv_packet(sock)
        sock.sendall(command)
        recv_packet(sock)
    finally:
        sock.close()
    print(f"{mode_name} activated.")



def main():
    if(len(sys.argv)<2):
        print("Enter something bruh")
        return
    mode = sys.argv[1].lower()
    if(mode not in MODES.keys()):
        print("Enter a valid mode : on/off/a/t")
        return
    switch_mode(mode)

if __name__ == "__main__":
    main()
