import sys
from time import time

from cirq.contrib import paulistring
from cirq.contrib.paulistring import recombine
from cirq.contrib.qasm_import import QasmCircuitParser

import logging

logger = logging.getLogger("root")
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler(stream=sys.stdout)
logger.addHandler(handler)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.info("reading qasm file...")

qasm = open('/Users/balintp/dev/proj/benchmarq/circuit_library/files/'
            'hubbard_sim_5.qasm').read()
c = QasmCircuitParser().parse(qasm)

logger.info("parsed qasm file: {} ops".format(len(list(c.all_operations()))))
start = time()

c2 = paulistring.optimize.optimized_circuit(
    c, repeat=10, merge_interactions=True)

dur = time() - start
logger.info("optimized circuit: {} ops in {} ".format(len(list(c2.all_operations())), dur))
