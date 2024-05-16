#!/usr/bin/python3
"""
Log Parsing
"""

import sys


def logstatus(totalSize, statusCode):
    """Logs the stats"""
    print(f"File size: {totalSize}")
    for code in sorted(statusCode):
        if statusCode[code] > 0:
            print(f"{code}: {statusCode[code]}")


def main():
    """Execute main program"""
    count = 0
    totalSize = 0
    statusCode = {
        "200": 0,
        "301": 0,
        "400": 0,
        "401": 0,
        "403": 0,
        "404": 0,
        "405": 0,
        "500": 0,
    }
    try:
        for line in sys.stdin:
            parts = line.split()
            try:
                totalSize += int(parts[-1])
            except ValueError:
                pass
            try:
                if parts[-2] in statusCode:
                    statusCode[parts[-2]] += 1
            except Exception:
                pass
            count += 1
            if count % 10 == 0:
                logstatus(totalSize, statusCode)
        logstatus(totalSize, statusCode)
    except KeyboardInterrupt:
        logstatus(totalSize, statusCode)
        raise


if __name__ == "__main__":
    main()
