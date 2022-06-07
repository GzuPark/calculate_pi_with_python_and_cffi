import argparse

from calculate_native_python import calculate_pi as calculate_python
from calculate_with_cffi import calculate_pi as calculate_cffi


def get_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-n", "--niter",
        type=int,
        default=100_000_000,
        help="Number of iteration when calculating (default: 100_000_000)"
    )
    args = parser.parse_args()
    return args


def main() -> None:
    args = get_args()

    print(f"\t[Native Python] pi = {calculate_python(args.niter)}")
    print(f"\t[C with FFI]    pi = {calculate_cffi(args.niter)}")


if __name__ == "__main__":
    main()
