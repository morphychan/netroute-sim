"""
RIP Simulation Engine

This module defines a Simulator class that runs RIP protocol updates
across a network of routers over multiple time steps.
"""

from typing import Dict, List
from rip_simulator.core.router import Router


class Simulator:
    def __init__(self) -> None:
        """
        Initialize an empty simulator.
        """
        self.routers: Dict[str, Router] = {}  # router_id -> Router instance
        self.neighbor_map: Dict[str, List[str]] = {}  # router_id -> list of neighbor_ids

    def add_router(self, router: Router) -> None:
        """
        Add a router to the simulation.

        Args:
            router (Router): Router instance to add.
        """
        self.routers[router.id] = router
        self.neighbor_map[router.id] = list(router.neighbors.keys())

    def run(self, rounds: int = 5) -> None:
        """
        Run the simulation for a fixed number of update rounds.

        Args:
            rounds (int): Number of time steps to simulate.
        """
        print(f"[simulator] Starting simulation for {rounds} rounds...\n")

        for step in range(1, rounds + 1):
            print(f"--- Round {step} ---")
            updates: Dict[str, Dict[str, int]] = {}

            # Step 1: Collect updates from each router
            for router_id, router in self.routers.items():
                updates[router_id] = router.generate_routing_update()

            # Step 2: Deliver updates to neighbors
            for router_id, router in self.routers.items():
                for neighbor_id in router.neighbors:
                    if neighbor_id in self.routers:
                        router.receive_update(
                            from_router=neighbor_id,
                            update_table=updates[neighbor_id]
                        )

            # Step 3: Print routing tables
            print(f"\n[simulator] Routing tables after round {step}:\n")
            for router in self.routers.values():
                router.print_table()

        print("\n[simulator] Final routing tables:\n")
        for router in self.routers.values():
            router.print_table()
