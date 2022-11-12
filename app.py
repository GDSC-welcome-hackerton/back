import os
from dataclasses import dataclass
from random import *
from typing import List

from flask import Flask, jsonify, request
from flask_cors import CORS


@dataclass
class Location:
    Latitude: float
    Longitude: float


os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

app = Flask(__name__)

app.secret_key = "secret_key"

CORS(app)


def random_location(x: Location, y: Location) -> Location:
    if x.Latitude > y.Latitude:
        x, y = y, x
    return Location(round(uniform(x.Latitude, y.Latitude), 6), round(uniform(x.Longitude, y.Longitude), 6))


def object_to_list(object: Location) -> List[float]:
    return list(object.__dict__.values())


def is_best_path(percent: int):
    if percent >= randint(1, 100):
        return True
    return False


def objects_to_json(locations: List[Location]):
    result = {}
    result["checkBestPath"] = is_best_path(20)
    result["randomLocation"] = list(map(lambda x: object_to_list(x), locations))
    return jsonify(result)


def get_locations(count: int, x: Location, y: Location) -> List[Location]:
    return [random_location(x, y) for _ in range(count)]


@app.route("/", methods=["GET"])
def get_main():
    return "Hello World"


@app.route("/random-location", methods=["POST"])
def post_random_location():
    location_count = request.json["LoactionCount"]
    _seoul = Location(37.532600, 127.024612)
    _busan = Location(35.166668, 129.066666)
    return objects_to_json(get_locations(location_count, _seoul, _busan))


if __name__ == "__main__":
    app.run(debug=True, use_reloader=False, host="0.0.0.0", port=5001)
