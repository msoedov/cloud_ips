import csv
import ipaddress
from functools import lru_cache
from ipaddress import IPv4Network
from ipaddress import IPv6Network
import black
import requests


@lru_cache
def aws_range():
    try:
        aws_url = "https://ip-ranges.amazonaws.com/ip-ranges.json"
        aws_ips = requests.get(aws_url, allow_redirects=True).json()
        return aws_ips["prefixes"]
    except Exception as e:
        print(f"Error: {e}")
    return []


def match_do():
    # This is the file linked from the digitalocean platform documentation website:
    # https://www.digitalocean.com/docs/platform/
    do_url = "http://digitalocean.com/geo/google.csv"
    do_ips_request = requests.get(do_url, allow_redirects=True)

    do_ips = csv.DictReader(
        do_ips_request.content.decode("utf-8").splitlines(),
        fieldnames=["range", "country", "region", "city", "postcode"],
    )

    for item in do_ips:
        yield ipaddress.ip_network(item["range"])


tml = """

aws_cloud = {aws_cloud}

gcp_cloud = {gcp_cloud}

do_cloud = {do_cloud}
"""


def to_net():
    return [ipaddress.ip_network(str(item["ip_prefix"])) for item in aws_range()]


def match_gcp():
    gcp_url = "https://www.gstatic.com/ipranges/cloud.json"
    gcp_ips = requests.get(gcp_url, allow_redirects=True).json()
    for item in gcp_ips["prefixes"]:
        yield ipaddress.ip_network(str(item.get("ipv4Prefix", item.get("ipv6Prefix"))))


def match_aws(target_ip):
    matched = False
    for item in aws_range():
        if target_ip in ipaddress.ip_network(str(item["ip_prefix"])):
            matched = True
            print(
                f"Match for AWS range "
                f'"{item["ip_prefix"]}", region "{item["region"]}" and service "{item["service"]}"'
            )
    return matched


if __name__ == "__main__":
    print(
        black.format_str(
            tml.format(
                aws_cloud=to_net(),
                gcp_cloud=list(match_gcp()),
                do_cloud=list(match_do()),
            ),
            mode=black.Mode(),
        )
    )
