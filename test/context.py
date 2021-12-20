import os
import sys
sys.path.insert(
    0,
    os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    )

from generators.markov_chain import MarkovChain  # noqa: F401, E402
from generators.epithet_chain_collection \
 import EpithetChainCollection  # noqa: F401, E402
