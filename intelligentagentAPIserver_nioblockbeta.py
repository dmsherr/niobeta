from nio.block.base import Block
from nio.properties import VersionProperty


class IAAPIserver(Block):

    version = VersionProperty('0.0.1')

    def process_signals(self, signals):
        for signal in signals:
            pass
        self.notify_signals(signals)

# TODO import python flask API server here after testing with Python 3.6.5

