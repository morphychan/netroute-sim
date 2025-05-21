"""
Network Routing Simulator CLI

This module provides a command-line interface to run simulations of
various network routing protocols.
"""

import argparse
import sys
from netroute_sim.simulation.topology_loader import load_topology


def simulate(topology_path: str, protocol: str, rounds: int) -> None:
    """
    Run a single simulation with the given topology and protocol.

    Args:
        topology_path (str): Path to the topology JSON file.
        protocol (str): Routing protocol to simulate.
        rounds (int): Number of simulation rounds to run.
    """
    print(f"[simulate] Running {protocol} simulation using topology file: {topology_path}")
    sim = load_topology(topology_path, protocol=protocol)
    sim.run(rounds=rounds)


def build_parser() -> argparse.ArgumentParser:
    """
    Build the CLI argument parser with subcommands.

    Returns:
        argparse.ArgumentParser: Configured parser instance.
    """
    parser = argparse.ArgumentParser(
        description="Network Routing Simulator: Emulate routing protocol behavior in networks."
    )
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Subcommand: simulate
    simulate_parser = subparsers.add_parser(
        "simulate", help="Run a single simulation with a given topology"
    )
    simulate_parser.add_argument(
        "--topology",
        type=str,
        default="config/sample_topology.json",
        help="Path to the topology JSON file (default: config/sample_topology.json)"
    )
    simulate_parser.add_argument(
        "--protocol",
        type=str,
        choices=["rip"],
        default="rip",
        help="Routing protocol to simulate (default: rip)"
    )
    simulate_parser.add_argument(
        "--rounds",
        type=int,
        default=5,
        help="Number of simulation rounds to run (default: 5)"
    )

    return parser


def main():
    """
    Entry point for the CLI interface.
    """
    parser = build_parser()
    args = parser.parse_args()

    if args.command == "simulate":
        simulate(args.topology, args.protocol, args.rounds)
    else:
        parser.print_help()
        sys.exit(1) 