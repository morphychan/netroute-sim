"""
Router model for RIP simulation.

Each router maintains a routing table and exchanges routing updates
with its neighbors according to RIP protocol rules.
"""

from typing import Dict, Tuple, Any
from netroute_sim.protocols.base import Router

MAX_HOP = 16  # RIP considers any route with hop >= 16 as unreachable


class RIPRouter(Router):
    def __init__(self, router_id: str) -> None:
        """
        Initialize a router with a unique identifier.

        Args:
            router_id (str): Unique ID of the router.
        """
        self.id: str = router_id
        self.neighbors: Dict[str, int] = {}  # neighbor_id -> cost (typically 1)
        self.routing_table: Dict[str, Tuple[str, int]] = {}  # dest -> (next_hop, hop_count)

    def add_neighbor(self, neighbor_id: str, cost: int = 1) -> None:
        """
        Add a direct neighbor and initialize routing entry.

        Args:
            neighbor_id (str): The ID of the neighbor.
            cost (int): Cost to reach the neighbor (default is 1).
        """
        self.neighbors[neighbor_id] = cost
        self.routing_table[neighbor_id] = (neighbor_id, cost)

    def generate_routing_update(self) -> Dict[str, int]:
        """
        Create a simplified version of the routing table for broadcasting.

        Returns:
            Dict[str, int]: Mapping of destination -> hop count.
        """
        return {
            destination: hop_count
            for destination, (_, hop_count) in self.routing_table.items()
        }

    def receive_update(self, from_router: str, update_table: Dict[str, Any]) -> None:
        """
        Process a routing update from a neighbor and update own table.

        Args:
            from_router (str): The neighbor sending the update.
            update_table (Dict[str, Any]): The neighbor's routing update.
        """
        for destination, their_hop in update_table.items():
            if destination == self.id:
                continue  # Ignore routes to self

            new_hop = min(their_hop + 1, MAX_HOP)

            # Update if: new destination, or shorter path, or came from same neighbor
            if (
                destination not in self.routing_table
                or new_hop < self.routing_table[destination][1]
                or self.routing_table[destination][0] == from_router
            ):
                self.routing_table[destination] = (from_router, new_hop)

    def print_table(self) -> None:
        """
        Print the current routing table of the router.
        """
        print(f"Routing table for router {self.id}:")
        for destination, (next_hop, hop_count) in sorted(self.routing_table.items()):
            hop_display = f"{hop_count} hops" if hop_count < MAX_HOP else "unreachable"
            print(f"  → {destination} via {next_hop} ({hop_display})") 