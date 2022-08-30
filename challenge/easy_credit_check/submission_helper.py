import sys
from argparse import ArgumentParser
import requests


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("fpath", help="Path to file that will be submitted")
    args = parser.parse_args(sys.argv[1:])
    fpath = args.fpath

    print(f"Sumbitting {fpath}")

    # Replace `your.csv` with a datafile of your choice.
    with open(fpath, "rb") as f:
        r = requests.post("http://localhost:5000/check", files={"data_file": f})
        response = r.text

    if "FLAG" in response:
        print(response)
        flag = response.split(" ")[-1]
        with open("flag.txt", "w") as f:
            f.write(flag)
