from libs import lib_calculate_pi
from utils.timer import timer


@timer
def calculate_pi(n_iter: int) -> float:
    return lib_calculate_pi.lib.calculatePi(n_iter)


if __name__ == "__main__":
    n = 100_000_000
    pi = calculate_pi(n)
    print(f"pi = {pi}")
