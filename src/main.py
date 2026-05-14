import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("left", type=int)
    parser.add_argument("right", type=int)

    args = parser.parse_args()

    result = args.left + args.right

    print(f"{args.left} + {args.right} = {result}")


if __name__ == "__main__":
    main()
