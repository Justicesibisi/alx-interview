#!/usr/bin/python3
import sys
import re

def initialize_log():
    """Initialize the log dictionary with file size and status code counts."""
    status_codes = [200, 301, 400, 401, 403, 404, 405, 500]
    log = {"file_size": 0, "code_list": {str(code): 0 for code in status_codes}}
    return log

def parse_line(line, regex, log):
    """Parse a single line of log input and update the log dictionary."""
    match = regex.fullmatch(line)
    if match:
        status_code, file_size = match.group(1, 2)
        log["file_size"] += int(file_size)

        if status_code.isdecimal() and status_code in log["code_list"]:
            log["code_list"][status_code] += 1

def print_code(log):
    """Print the file size and status code counts."""
    print(f"File size: {log['file_size']}")
    sorted_code_list = sorted(log["code_list"].keys())
    for code in sorted_code_list:
        if log["code_list"][code] > 0:
            print(f"{code}: {log['code_list'][code]}")

def main():
    """Main function to handle stdin input, parse lines, and print stats."""
    regex = re.compile(
      #  r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} - \[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d+\] "GET /projects/260 HTTP/1.1" (\d{3}) (\d+)$'
        r'^(?P<ip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - \[(?P<date>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d+)\] "GET /projects/260 HTTP/1.1" (?P<status>\d{3}) (?P<size>\d+)$'

    )

    log = initialize_log()
    line_count = 0

    try:
        for line in sys.stdin:
            line = line.rstrip()
            line_count += 1
            parse_line(line, regex, log)

            # Print stats every 10 lines
            if line_count % 10 == 0:
                print_code(log)

    except KeyboardInterrupt:
        print_code(log)
        sys.exit(0)

if __name__ == "__main__":
    main()
