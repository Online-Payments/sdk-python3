from datetime import date, datetime, timezone


class DataObject(object):
    def to_dictionary(self) -> dict:
        return {}

    def from_dictionary(self, dictionary: dict) -> 'DataObject':
        if not isinstance(dictionary, dict):
            raise TypeError('value \'{}\' is not a dictionary'.format(dictionary))
        return self

    @staticmethod
    def parse_date(s: str) -> date:
        return date.fromisoformat(s)

    @staticmethod
    def format_date(d: date) -> str:
        return d.isoformat()

    @staticmethod
    def parse_datetime(s: str) -> datetime:
        if s.endswith('Z'):
            s = s[:-1] + '+00:00'
        return datetime.fromisoformat(s)

    @staticmethod
    def format_datetime(dt: datetime) -> str:
        # isoformat(timespec='milliseconds') works fine, as long as there is a timezone
        # if there isn't one, add the current timezone
        if dt.tzinfo is None:
            zone = datetime.fromtimestamp(dt.timestamp(), timezone.utc).astimezone().tzinfo
            dt = datetime.fromtimestamp(dt.timestamp(), zone)
        return dt.isoformat(timespec='milliseconds')
