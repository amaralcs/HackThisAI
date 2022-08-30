import sys
from argparse import ArgumentParser
import requests
import json

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("sensor", help="Number of the sensor to modify", default=20)
    args = parser.parse_args(sys.argv[1:])
    sensor = args.sensor

    r = requests.post("http://localhost:5000/check", json={"sensor_value": sensor})

    response = r.text
    print(response)
    if "FLAG" in response:
        flag = response.split(" ")[-1]
        with open("flag.txt", "w") as f:
            f.write(flag)
