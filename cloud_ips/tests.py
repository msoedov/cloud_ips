import timeit

from cloud_ips.network import is_cloud
from cloud_ips.network import is_cloud_v0

if __name__ == "__main__":
    is_cloud
    is_cloud_v0
    print(
        timeit.timeit(
            'is_cloud("95.67.89.122")', "from __main__ import is_cloud", number=1000,
        )
    )
    print(
        timeit.timeit(
            'is_cloud_v0("95.67.89.122")',
            "from __main__ import is_cloud_v0",
            number=1000,
        )
    )
    print(
        timeit.timeit(
            'is_cloud_v0("95.67.89.122")',
            "from __main__ import is_cloud_v0",
            number=10,
        )
    )
