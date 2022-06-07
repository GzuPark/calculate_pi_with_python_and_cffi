from inspect import getfile
from functools import wraps
from os.path import split
from time import perf_counter
from typing import Any


def timer(fn) -> Any:
    @wraps(fn)
    def measure_time(*args, **kwargs) -> float:
        start = perf_counter()
        result = fn(*args, **kwargs)
        end = perf_counter()
        print(f"@timer: [{split(getfile(fn))[1]}] {fn.__name__} ( {end - start:.6f} seconds )")
        return result
    return measure_time
