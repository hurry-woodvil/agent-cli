import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("prompt", type=str)

    args = parser.parse_args()

    prompt = args.prompt

    print(f"prompt: {prompt}")


if __name__ == "__main__":
    main()
