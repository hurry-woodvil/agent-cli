import argparse


def add(left: int, right: int) -> int:
    return left + right


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("left", type=int)
    parser.add_argument("right", type=int)

    args = parser.parse_args()

    left = args.left
    right = args.right

    result = add(left, right)

    print(f"{left} + {right} = {result}")


if __name__ == "__main__":
    main()
