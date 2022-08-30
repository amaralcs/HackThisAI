import sys
from argparse import ArgumentParser
import requests

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("fpath", help="Path to file with model input text")
    args = parser.parse_args(sys.argv[1:])
    fpath = args.fpath

    with open(fpath, "r") as f:
        txt = "".join(f.readlines())
    # print(txt)

    r = requests.post("http://localhost:5000/check", json={"text": txt})
    response = r.text
    print(response)
    if "FLAG" in response:
        flag = response.split(" ")[-1]
        with open("flag.txt", "w") as f:
            f.write(flag)
