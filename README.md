## Installation

### 1. System Dependencies

#### libpcap/Npcap

Half Diamond uses [Scapy](https://scapy.net/) for network packet manipulation. Depending on your operating system, install one of the following:

- **Linux/MacOS**: Install [libpcap](https://www.tcpdump.org/). Refer to the [Scapy documentation](https://scapy.readthedocs.io/en/latest/installation.html#platform-specific-instructions) for more details.
- **Windows**: Install [Npcap](https://npcap.com/).

#### Nmap

Half Diamond also uses [python-nmap](https://pypi.org/project/python-nmap/), a Python wrapper that requires [Nmap](https://nmap.org/) to be installed locally. Download and install it from [here](https://nmap.org/download.html).

### 2. Python Requirements

Before installing the requirements, it's recommended to create a virtual environment:

```bash
python3 -m venv env
source env/bin/activate  # On Windows, use `env\Scripts\activate`
```

After activating the virtual environment, install the requirements:

```bash
pip install -r requirements.txt
```

### 3. Running the server

Once all dependencies are installed, start the development server:

```bash
cd src
uvicorn main:app --reload
```
