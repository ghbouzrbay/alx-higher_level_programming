#!/usr/bin/python3

import sys
from collections import defaultdict

def compute_metrics():
    total_size = 0
    status_codes = defaultdict(int)

    try:
        line_count = 0
        for line in sys.stdin:
            line_count += 1
            ip_address, _, _, _, status_code, file_size = line.split()[0], line.split()[3], line.split()[5], line.split()[8], line.split()[10], line.split()[11]
            total_size += int(file_size)
            status_codes[status_code] += 1

            if line_count % 10 == 0:
                print_statistics(total_size, status_codes)

    except KeyboardInterrupt:
        print_statistics(total_size, status_codes)

def print_statistics(total_size, status_codes):
    print(f"Total file size: {total_size}")
    for status_code in sorted(status_codes.keys()):
        print(f"{status_code}: {status_codes[status_code]}")

if __name__ == "__main__":
    compute_metrics()
