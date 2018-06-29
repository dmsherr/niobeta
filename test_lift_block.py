from unittest.mock import patch

from nio.testing.block_test_case import NIOBlockTestCase
from nio import Signal

from ..filter_block import Filter


class LiftSignal(Signal):

    def __init__(self, val):
        super().__init__()
        self.val = val


class TestFilter(NIOBlockTestCase):

    def test_pass_all(self):
        signals = [1, 2, 3, 4]
        blk = Filter()
        self.configure_block(blk, {})
        blk.start()
        blk.process_signals(signals)
        self.assert_num_signals_notified(4, blk, 'true')
        self.assert_num_signals_notified(0, blk, 'false')
        blk.stop()

    def test_pass_any(self):
        signals = [1, 2, 3, 4]
        blk = Filter()
        self.configure_block(blk, {'operator': 'ANY'})
        blk.start()
        blk.process_signals(signals)
        self.assert_num_signals_notified(0, blk, 'true')
        self.assert_num_signals_notified(4, blk, 'false')
        blk.stop()

    def test_filter_odd(self):
        signals = [
            LiftSignal(1),
            LiftSignal(2),
            LiftSignal(3),
            LiftSignal(4)
        ]
        blk = Filter()
        self.configure_block(blk, {
            'conditions': [
                {'expr': '{{$val % 2 == 0}}'}
            ]
        })
        blk.start()
        blk.process_signals(signals)
        self.assert_num_signals_notified(2, blk, 'true')
        self.assert_num_signals_notified(2, blk, 'false')
        blk.stop()

    def test_access_signal_attrs(self):
        signals = [LiftSignal(23)]
        blk = Filter()
        self.configure_block(blk, {
            'conditions': [
                {'expr': '{{$val != 23}}'}
            ]
        })
        blk.start()
        blk.process_signals(signals)
        self.assert_num_signals_notified(0, blk, 'true')
        self.assert_num_signals_notified(1, blk, 'false')
        blk.stop()

    def test_regex(self):
        signals = [LiftSignal("alert")]
        blk = Filter()
        self.configure_block(blk, {
            'conditions': [
                {'expr': '{{re.match("alert", $val) is not None}}'}
            ]
        })
        blk.start()
        blk.process_signals(signals)
        self.assert_num_signals_notified(1, blk, 'true')
        self.assert_num_signals_notified(0, blk, 'false')
        blk.stop()

