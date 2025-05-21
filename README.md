# Netroute-Sim

A network routing protocol simulator for studying the behavior of various routing protocols (RIP, and more to come) under dynamic network conditions.

## Getting Started

```bash
git clone https://github.com/yourname/netroute-sim.git
cd netroute-sim
python -m venv .venv && source .venv/bin/activate
pip install -e .
python -m netroute_sim --help
```

## Available Protocols

- RIP (Routing Information Protocol) - a simple distance-vector routing protocol
- More protocols coming soon!

## Examples

```bash
# Run a RIP simulation with the default topology
python -m netroute_sim simulate

# Specify a custom topology file and protocol
python -m netroute_sim simulate --topology config/custom_topology.json --protocol rip
``` 