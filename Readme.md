# cloud_ips

Fast - microsecond based cloud providers ip address lookup

## Features

- GCP / AWS / Digital ocean ip ranges support
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
