#!/usr/bin/python3
"""
Script that reads stdin line by line and computes metrics.
"""
import sys


def print_stats(total_size, status_codes):
    """Prints the accumulated statistics."""
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))


if __name__ == "__main__":
    total_size = 0
    status_codes = {
        "200": 0, "301": 0, "400": 0, "401": 0,
        "403": 0, "404": 0, "405": 0, "500": 0
    }
    line_count = 0

    try:
        for line in sys.stdin:
            line_count += 1
            parts = line.split()

            # Parse file size (last element)
            try:
                total_size += int(parts[-1])
            except (IndexError, ValueError):
                pass

            # Parse status code (second to last element)
            try:
                code = parts[-2]
                if code in status_codes:
                    status_codes[code] += 1
            except (IndexError, ValueError):
                pass

            # Print every 10 lines
            if line_count % 10 == 0:
                print_stats(total_size, status_codes)

    except KeyboardInterrupt:
        print_stats(total_size, status_codes)
        raise

    print_stats(total_size, status_codes)
