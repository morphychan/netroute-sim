"""
Topology loader for network simulations.

This module provides utilities to load network topologies
from configuration files.
"""

import json
from typing import Type, Dict

from netroute_sim.protocols.base import Router
from netroute_sim.protocols.rip import RIPRouter
from netroute_sim.simulation.simulator import Simulator


def load_topology(path: str, protocol: str = "rip") -> Simulator:
    """
    Load a network topology from a JSON file.
    
    Args:
        path (str): Path to the topology JSON file.
        protocol (str): Routing protocol to use ("rip", etc.)
        
    Returns:
        Simulator: Configured simulator instance.
    """
    with open(path, "r") as f:
        data = json.load(f)
    
    # Select router implementation based on protocol
    router_classes: Dict[str, Type[Router]] = {
        "rip": RIPRouter,
    }
    
    if protocol not in router_classes:
        raise ValueError(f"Unsupported protocol: {protocol}. Available protocols: {list(router_classes.keys())}")
    
    router_class = router_classes[protocol]
    sim = Simulator(protocol_name=protocol)
    routers = {}

    for rid in data["routers"]:
        router = router_class(rid)
        routers[rid] = router
        sim.add_router(router)

    for src, dst in data["links"]:
        routers[src].add_neighbor(dst)
        routers[dst].add_neighbor(src)

    return sim 