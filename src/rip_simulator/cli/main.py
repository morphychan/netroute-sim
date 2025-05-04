"""
RIP Simulator CLI

This module provides a command-line interface to run simulations of
the Routing Information Protocol (RIP).
"""

import argparse
import sys


def simulate(topology_path: str) -> None:
    """
    Run a single RIP simulation with the given topology.

    Args:
        topology_path (str): Path to the topology JSON file.
    """
    print(f"[simulate] Running simulation using topology file: {topology_path}")
    # TODO: Load topology and invoke Simulator class


def build_parser() -> argparse.ArgumentParser:
    """
    Build the CLI argument parser with subcommands.

    Returns:
        argparse.ArgumentParser: Configured parser instance.
    """
    parser = argparse.ArgumentParser(
        description="RIP Simulator: Emulate RIP protocol behavior in dynamic networks."
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

    return parser


def main():
    """
    Entry point for the CLI interface.
    """
    parser = build_parser()
    args = parser.parse_args()

    if args.command == "simulate":
        simulate(args.topology)
    else:
        parser.print_help()
        sys.exit(1)
