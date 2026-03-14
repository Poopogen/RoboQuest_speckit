import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--session", action="store_true")
    args = parser.parse_args()
    if args.session:
        print("Simulated session created")


if __name__ == "__main__":
    main()
