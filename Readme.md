# cloud_ips

Check if an IP address is in the ranges used by AWS/GCP/DO/Azure. It fast, microsecond based cloud providers lookup by public ip

## Features

- GCP / AWS / Digital ocean ip ranges support
- 1000x faster than a brute force lookup
- Most recent data records
- Fully typed with annotations and checked with `mypy`, [PEP561 compatible](https://www.python.org/dev/peps/pep-0561/)
- Easy to start: has lots of docs, tests, and tutorials

## Usage

```shell
pip install cloud_ips
```

```python
from cloud_ips.network import is_cloud

is_cloud("95.67.109.122")

>> False
```

### Benchmarks

```python

timeit.timeit(
    'is_cloud("95.67.89.122")', "from __main__ import is_cloud", number=1000,
)
>> 0.04331268899999999


timeit.timeit(
    'naive("95.67.89.122")', "from __main__ import naive", number=1000,
)
>> 3.5043050669999998
```
