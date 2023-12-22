import csv

# APACHE LOG PROCESSOR
log = open("example_log.txt")


def parse_log(log):
    for line in log:
        split_line = line.split()
        remote_addr = split_line[0]
        time_local = split_line[3] + " " + split_line[4]
        request_type = split_line[5]
        request_path = split_line[6]
        status = split_line[8]
        body_bytes_sent = split_line[9]
        http_referrer = split_line[10]
        http_user_agent = " ".join(split_line[11:])
        yield (
            remote_addr,
            time_local,
            request_type,
            request_path,
            status,
            body_bytes_sent,
            http_referrer,
            http_user_agent,
        )


first_line = next(parse_log(log))


def count_unique_request(csv_file):
    reader = csv.reader(csv_file)
    header = next(reader)
    idx = header.index("request_type")

    uniques = {}
    for line in reader:
        if not uniques.get(line[idx]):
            uniques[line[idx]] = 0
        uniques[line[idx]] += 1
    return uniques


log = open("example_log.txt")
parsed = parse_log(log)
file = open("temporary.csv", "r+")


def build_csv(parsed, header, file):
    pass


csv_file = build_csv(
    parsed,
    header=[
        "ip",
        "time_local",
        "request_type",
        "request_path",
        "status",
        "bytes_sent",
        "http_referrer",
        "http_user_agent",
    ],
    file=file,
)
uniques = count_unique_request(csv_file)


def count_unique_request(csv_file):
    reader = csv.reader(csv_file)
    header = next(reader)
    idx = header.index("request_type")

    uniques = {}
    for line in reader:
        if not uniques.get(line[idx]):
            uniques[line[idx]] = 0
        uniques[line[idx]] += 1
    return ((k, v) for k, v in uniques.items())


log = open("example_log.txt")
parsed = parse_log(log)
file = open("temporary.csv", "r+")

csv_file = build_csv(
    parsed,
    header=[
        "ip",
        "time_local",
        "request_type",
        "request_path",
        "status",
        "bytes_sent",
        "http_referrer",
        "http_user_agent",
    ],
    file=file,
)
