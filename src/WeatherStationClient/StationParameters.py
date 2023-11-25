from dataclasses import dataclass


class StationParameters(dict):
    pass


@dataclass
class RegisterStationParameters:
    external_id: str = None
    name: str = None
    latitude: float = None
    longitude: float = None
    altitude: float = None
