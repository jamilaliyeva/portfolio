import dataclasses
import json

house_data = [
    {
        "year": 2024,
        "room_count": 3,
        "address": "sdfdsf"
    },
    {}
]


@dataclasses.dataclass
class HouseData:
    name: str
    surname: str
    year: int
    room_count: int
    address: str

def load_houses_from_json(path: str):
    with open(path, "r") as f:
        reader = json.load(f)


houses = [
    HouseData(year=2024, room_count=3, address="sdfdsf"),
    HouseData(year=2000, room_count=3, address="asdfdfasdf")
]


