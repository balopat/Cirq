import cirq.contrib.routing as ccr
import cirq_google
import cirq_google.experimental.routing as routing


def test_xmon_device_to_graph():
    foxtail_graph = routing.xmon_device_to_graph(cirq_google.Foxtail)
    two_by_eleven_grid_graph = ccr.get_grid_device_graph(2, 11)
    assert foxtail_graph.nodes == two_by_eleven_grid_graph.nodes
    assert foxtail_graph.edges() == two_by_eleven_grid_graph.edges()


def test_nx_qubit_layout():
    foxtail_graph = routing.xmon_device_to_graph(cirq_google.Foxtail)
    pos = ccr.nx_qubit_layout(foxtail_graph)
    assert len(pos) == len(foxtail_graph)
    for k, (x, y) in pos.items():
        assert x == k.col
        assert y == -k.row
