# Compare running time between native Python and C with FFI wrapper

For calculating Pi to use the [rate of convergence](https://en.wikipedia.org/wiki/Pi) like below.

![rate of convergence](https://wikimedia.org/api/rest_v1/media/math/render/svg/e9e3959cd2d0ec735e7a6a1917df784842b76706)

## Build

Move to the `libs` directory, and run `builder.py` script for compiling c code. (_Recommend: back to the root directory_)

```sh
cd libs
python -m builder
```

## Run

Check your current path on the project's root, and run `compare.py` script.

```sh
python -m compare [-n]

# usage: compare.py [-h] [-n NITER]

# optional arguments:
#   -h, --help            show this help message and exit
#   -n NITER, --niter NITER
#                         Number of iteration when calculating (default: 100_000_000)
```

Then, you can get the result like below, _c code with FFI_ is **61.8 faster** than _native python_.

```sh
@timer: [calculate_native_python.py] calculate_pi ( 5.647333 seconds )
        [Native Python] pi = 3.141592643589326
@timer: [calculate_with_cffi.py] calculate_pi ( 0.091362 seconds )
        [C with FFI]    pi = 3.141592643589326
```

## Test

Run `pytest` command or use with verbose option.

```python
pytest -v
```
