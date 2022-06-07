def calculate_pi(n_iter: int) -> float:
    return 3.14


if __name__ == "__main__":
    n = 100_000_000
    pi = calculate_pi(n)
    print(f"pi = {pi}")
