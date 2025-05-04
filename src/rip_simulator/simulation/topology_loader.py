from rip_simulator.core.router import Router
from rip_simulator.simulation.simulator import Simulator
import json

def load_topology(path: str) -> Simulator:
    with open(path, "r") as f:
        data = json.load(f)

    sim = Simulator()
    routers = {}

    for rid in data["routers"]:
        router = Router(rid)
        routers[rid] = router
        sim.add_router(router)

    for src, dst in data["links"]:
        routers[src].add_neighbor(dst)
        routers[dst].add_neighbor(src)

    return sim
