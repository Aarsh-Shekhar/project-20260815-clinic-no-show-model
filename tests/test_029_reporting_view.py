import unittest

from clinic_no_show_model.models import Record
from clinic_no_show_model.scoring import score_record


class DepthCheck29(unittest.TestCase):
    def test_029_reporting_view(self):
        record = Record(id="appointment-029", exposure=94696, signal=0.757, urgency=5)
        self.assertGreaterEqual(score_record(record), 0)
        self.assertLessEqual(score_record(record), 1)


if __name__ == "__main__":
    unittest.main()
