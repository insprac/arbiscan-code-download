# Arbiscan Code Download

A small utility script for downloading code from
[Arbiscan](https://arbiscan.io) to make reviewing and exploration easier.

### Setup

Install dependencies:

```bash
pip3 install -r requirements.txt
```

### Usage

You will need to provide the script with a contract address and an output
directory, the output directory must exist or an error will be raised.

To see the usage:

```bash
./arbiscan-download.py -h
```

Example usage:

```bash
./arbiscan-download.py <contract address> --out <output directory>
```

### Note

This is a very quick and experimental script and wont cover edge-cases.
