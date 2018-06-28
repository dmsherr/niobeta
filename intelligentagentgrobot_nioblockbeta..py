from nio.block.base import Block
from nio.properties import VersionProperty


class IAgrobot(Block):

    version = VersionProperty('0.0.1')

    def process_signals(self, signals):
        for signal in signals:
            pass
        self.notify_signals(signals)

    def guarded_commands(self,signals):
  		for signal in signals:
            if {{$msgtype="deviceinfo"}}
            # TODO guard conditions per each Operational and Safety threshold, temp, velocity, etc.
            pass
        self.notify_signals(signals)
