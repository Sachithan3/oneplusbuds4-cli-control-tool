# OnePlus Buds 4 CLI Controller (Linux only)
 
Control ANC modes of OnePlus Buds 4 directly from the terminal using Bluetooth RFCOMM and reverse-engineered packets.

---

## Features

- Toggle ANC On/Off/Adaptive/Transparency modes
- Lightweight CLI tool (no external dependencies)

---

## Requirements

- Linux (with Bluez Bluetooth stack)
- Python 3
- Paired OnePlus Buds 4
- RFCOMM support

> Not supported on Windows (Python lacks Bluetooth RFCOMM socket support)

---

## Setup

1. Clone the repo

```bash
git clone https://github.com/<your-username>/oneplusbuds4-cli-control-tool.git
cd oneplusbuds4-cli-control-tool
#make sure buds are paired
python3 main.py a/t/on/off