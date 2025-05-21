"""
Base router interface for all routing protocol implementations.

This module defines the base interface that all routing protocol
implementations should adhere to.
"""

from abc import ABC, abstractmethod
from typing import Dict, Any


class Router(ABC):
    """Base router interface for all routing protocol implementations."""
    
    @abstractmethod
    def __init__(self, router_id: str) -> None:
        """
        Initialize a router with a unique identifier.
        
        Args:
            router_id (str): Unique ID of the router.
        """
        pass
        
    @abstractmethod
    def add_neighbor(self, neighbor_id: str, cost: int = 1) -> None:
        """
        Add a direct neighbor and initialize routing entry.
        
        Args:
            neighbor_id (str): The ID of the neighbor.
            cost (int): Cost to reach the neighbor.
        """
        pass
        
    @abstractmethod
    def generate_routing_update(self) -> Dict[str, Any]:
        """
        Create a routing update for broadcasting to neighbors.
        
        Returns:
            Dict[str, Any]: Protocol-specific update format.
        """
        pass
        
    @abstractmethod
    def receive_update(self, from_router: str, update_table: Dict[str, Any]) -> None:
        """
        Process a routing update from a neighbor and update own table.
        
        Args:
            from_router (str): The neighbor sending the update.
            update_table (Dict[str, Any]): The neighbor's routing update.
        """
        pass
        
    @abstractmethod
    def print_table(self) -> None:
        """Print the current routing table of the router."""
        pass 