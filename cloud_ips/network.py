import ipaddress
from collections import defaultdict

from cloud_ips.const import do_cloud
from cloud_ips.const import aws_cloud
from cloud_ips.const import gcp_cloud


def is_cloud_v0(addr: str) -> bool(...):
    try:
        addr = ipaddress.ip_address(addr)
    except ValueError:
        return False

    for net in aws_cloud:
        if addr in net:
            print(f"{addr=} in block {net=} ")
            return True
    for net in do_cloud:
        if addr in net:
            print(f"{addr=} in block {net=} ")
            return True

    for net in gcp_cloud:
        if addr in net:
            print(f"{addr=} in block {net=} ")
            return True

    return False


tree = defaultdict(list)

for net in sum([aws_cloud, do_cloud, gcp_cloud], []):
    prefix = net.network_address.exploded[:2]
    tree[prefix].append(net)


def is_cloud(addr: str) -> bool(...):
    try:
        addr = ipaddress.ip_address(addr)
    except ValueError:
        return False

    for net in tree[addr.exploded[:2]]:
        if addr in net:
            print(f"{addr=} in block {net=} ")
            return True
    return False
