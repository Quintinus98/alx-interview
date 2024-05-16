#!/usr/bin/python3
"""
Log Parsing
"""

import sys
import signal

totalSize = 0
statusCode = {
    200: 0,
    301: 0,
    400: 0,
    401: 0,
    403: 0,
    404: 0,
    405: 0,
    500: 0,
}


def log_stats():
    """Logs the stats"""
    global totalSize, statusCode
    print(f"File size: {totalSize}")
    for code in sorted(statusCode):
        if statusCode[code] > 0:
            print(f"{code}: {statusCode[code]}")


def handler(signal, frame):
    """Signal handler function"""
    log_stats()
    sys.exit(0)


signal.signal(signal.SIGINT, handler)


def main():
    """Execute main program"""
    count = 0
    global totalSize, statusCode
    try:
        for line in sys.stdin:
            parts = line.split()
            if len(parts) < 9:
                continue
            endpoint = parts[4] + " " + parts[5] + " " + parts[6]
            if endpoint != '"GET /projects/260 HTTP/1.1"':
                continue
            try:
                code = int(parts[7])
                size = int(parts[8])
            except ValueError:
                continue
            if code in statusCode:
                statusCode[code] += 1
            totalSize += size
            count += 1
            if count % 10 == 0:
                log_stats()
    except KeyboardInterrupt:
        log_stats()
        sys.exit(0)


if __name__ == "__main__":
    main()
