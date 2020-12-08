# TODO(balintp): this needs to be moved to cirq.google.experimental
import networkx as nx

import cirq_google
from cirq.contrib.routing import gridqubits_to_graph_device


def xmon_device_to_graph(device: cirq_google.XmonDevice) -> nx.Graph:
    """Gets the graph of an XmonDevice."""
    return gridqubits_to_graph_device(device.qubits)
