import cffi
import os


def build() -> None:
    ffi = cffi.FFI()

    with open(os.path.join(os.path.dirname(__file__), "calculate_pi.h")) as f:
        ffi.cdef(f.read())

    ffi.set_source(
        "lib_calculate_pi",
        '#include "calculate_pi.h"',
        sources=["calculate_pi.c"],
        libraries=["m"],
    )

    ffi.compile(verbose=True)


if __name__ == "__main__":
    build()
