import unittest

from clinic_no_show_model.models import Record
from clinic_no_show_model.scoring import score_record


class DepthCheck32(unittest.TestCase):
    def test_032_operator_handoff(self):
        record = Record(id="appointment-032", exposure=88875, signal=0.238, urgency=6)
        self.assertGreaterEqual(score_record(record), 0)
        self.assertLessEqual(score_record(record), 1)


if __name__ == "__main__":
    unittest.main()
