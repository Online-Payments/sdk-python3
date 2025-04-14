import unittest
from datetime import date, datetime, timedelta, timezone

from onlinepayments.sdk.domain.data_object import DataObject


class DateObjectTest(unittest.TestCase):

    def test_parse_date(self):
        params = [('2023-09-20', date(2023, 9, 20)), ('2024-02-29', date(2024, 2, 29))]
        for s, expected in params:
            self.assertEqual(expected, DataObject.parse_date(s))

    def test_format_date(self):
        params = [(date(2023, 9, 20), '2023-09-20'), (date(2024, 2, 29), '2024-02-29')]
        for d, expected in params:
            self.assertEqual(expected, DataObject.format_date(d))

    def test_format_and_parse_date(self):
        params = [date(2023, 9, 20), date(2024, 2, 29)]
        for d in params:
            s = DataObject.format_date(d)
            self.assertEqual(d, DataObject.parse_date(s))

    def test_parse_datetime(self):
        params = [
            ('2023-10-10T08:00+02:00', datetime(2023, 10, 10, 8, 0, tzinfo=timezone(timedelta(hours=2)))),
            ('2023-10-10T08:00Z', datetime(2023, 10, 10, 8, 0, tzinfo=timezone.utc)),
            ('2020-01-01T12:00:00Z', datetime(2020, 1, 1, 12, 0, second=0, tzinfo=timezone.utc)),
            ('2023-10-10T08:00:01.234+02:00', datetime(2023, 10, 10, 8, 0, second=1, microsecond=234000, tzinfo=timezone(timedelta(hours=2)))),
            ('2023-10-10T08:00:01.234Z', datetime(2023, 10, 10, 8, 0, second=1, microsecond=234000, tzinfo=timezone.utc)),
            ('2020-01-01T12:00:00.123456Z', datetime(2020, 1, 1, 12, 0, second=0, microsecond=123456, tzinfo=timezone.utc)),
        ]
        for s, expected in params:
            self.assertEqual(expected, DataObject.parse_datetime(s))

    def test_format_datetime(self):
        params = [
            (datetime(2023, 10, 10, 8, 0, tzinfo=timezone(timedelta(hours=2))), '2023-10-10T08:00:00.000+02:00'),
            (datetime(2023, 10, 10, 8, 0, tzinfo=timezone.utc), '2023-10-10T08:00:00.000+00:00'),
            (datetime(2020, 1, 1, 12, 0, second=0, tzinfo=timezone.utc), '2020-01-01T12:00:00.000+00:00'),
            (datetime(2023, 10, 10, 8, 0, second=1, microsecond=234000, tzinfo=timezone(timedelta(hours=2))), '2023-10-10T08:00:01.234+02:00'),
            (datetime(2023, 10, 10, 8, 0, second=1, microsecond=234000, tzinfo=timezone.utc), '2023-10-10T08:00:01.234+00:00'),
            (datetime(2020, 1, 1, 12, 0, second=0, microsecond=123456, tzinfo=timezone.utc), '2020-01-01T12:00:00.123+00:00'),
        ]
        for dt, expected in params:
            self.assertEqual(expected, DataObject.format_datetime(dt))

    def test_format_and_parse_datetime(self):
        params = [
            datetime(2023, 10, 10, 8, 0, tzinfo=timezone(timedelta(hours=2))),
            datetime(2023, 10, 10, 8, 0, tzinfo=timezone.utc),
            datetime(2020, 1, 1, 12, 0, second=0, tzinfo=timezone.utc),
            datetime(2023, 10, 10, 8, 0, second=1, microsecond=234000, tzinfo=timezone(timedelta(hours=2))),
            datetime(2023, 10, 10, 8, 0, second=1, microsecond=234000, tzinfo=timezone.utc),
            datetime(2020, 1, 1, 12, 0, second=0, microsecond=123456, tzinfo=timezone.utc),
        ]
        for dt in params:
            s = DataObject.format_datetime(dt)
            self.assertEqual(int(dt.timestamp() * 1000), int(DataObject.parse_datetime(s).timestamp() * 1000))

    def test_format_and_parse_datetime_no_timezone(self):
        params = [
            datetime(2023, 10, 10, 8, 0),
            datetime(2020, 1, 1, 12, 0, second=0),
            datetime(2023, 10, 10, 8, 0, second=1, microsecond=234000),
        ]
        for dt in params:
            s = DataObject.format_datetime(dt)
            self.assertEqual(dt.timestamp(), DataObject.parse_datetime(s).timestamp())


if __name__ == '__main__':
    unittest.main()
