from utils.timer import timer


@timer
def calculate_pi(n_iter: int) -> float:
    result = 0.0
    numerator = 4.0
    denominator = 1.0
    operation = 1.0

    for _ in range(n_iter):
        result += operation * (numerator / denominator)
        denominator += 2.0
        operation *= -1.0
    
    return result


if __name__ == "__main__":
    n = 100_000_000
    pi = calculate_pi(n)
    print(f"pi = {pi}")
