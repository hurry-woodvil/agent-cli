import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("left", type=int)
    parser.add_argument("right", type=int)

    args = parser.parse_args()

    print(args.left)
    print(args.right)


if __name__ == "__main__":
    main()
