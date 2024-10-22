import sys
import re

def initialize_log():
    status_code = [200, 301, 400, 401, 403, 404, 405, 500]

    log = {"file_size": 0, "code_list":{str(code): 0 for code in status_code} }
    print(f"{log = }")
    return log

def parse_line(line, regex, log):
    match = regex.fullmatch(line)

    if match:
        start_code, file_size = match.group(1, 2)

        log["file_size"] += int(file_size)

        if start_code.indecimal():
            log["code_list"][start_code] +=1

def print_code(log):
    print("file size: {}".format(log['file_size']))

    sorted_code_list = sorted(log["code_list"])

    for code in sorted_code_list:
        if log["code_list"][code]:
            print(f"{code}:{log['code_list'][code]}")

def main():
    regex = re.compile(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.d{1,3} - \[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d+\]"GET /projects/260 HTTP/1.1" (.{3}) (\d+)')

    log = initialize_log()

    line_count = 0

    for line in sys.stdin:
        line = line.rstrip()

        line_count = line_count +1

        parse_line(line, regex, log)

        if line_count % 10 == 0:
            print_codes(parsed_log)

if __name__ == "__main__":
    main()
    initialize_log