import argparse
import time


def main(args: argparse.Namespace):
    tmp_len = 0
    while True:
        for i in range(args.excercise, -1, -1):
            info = f"excercise: {i}"
            print(" " * tmp_len, end="\r")
            print(info, end="\r")
            tmp_len = len(info)
            time.sleep(1)

        for i in range(args.rest, -1, -1):
            info = f"rest: {i}"
            print(" " * tmp_len, end="\r")
            print(info, end="\r")
            tmp_len = len(info)
            time.sleep(1)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-r",
        "--rest-time",
        type=int,
        dest="rest",
        help="rest time per cycle, default to 15s",
        default=15,
    )
    parser.add_argument(
        "-e",
        "--excercise-time",
        type=int,
        dest="excercise",
        help="excercise time per cycle, default to 45s",
        default=45,
    )
    args = parser.parse_args()
    main(args)
