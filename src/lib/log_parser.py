import re
from collections import defaultdict

def parse_msg3_logs(log_path):
    pattern_success = re.compile(r"type\s+MSG3.*?status\s+success", re.IGNORECASE)
    pattern_failure = re.compile(r"type\s+MSG3.*?status\s+(?!success)\w+", re.IGNORECASE)

    total_success = 0
    total_failure = 0
    hourly_data = defaultdict(lambda: {"success": 0, "failure": 0})

    with open(log_path, "r") as f:
        for line in f:
            match_time = re.match(r"(\d{4}-\d{2}-\d{2} \d{2}):\d{2}:\d{2}", line)
            if match_time:
                hour = match_time.group(1)
                if pattern_success.search(line):
                    total_success += 1
                    hourly_data[hour]["success"] += 1
                elif pattern_failure.search(line):
                    total_failure += 1
                    hourly_data[hour]["failure"] += 1

    overall_success_rate = (total_success / (total_success + total_failure) * 100
                             if (total_success + total_failure) else 0)

    return round(overall_success_rate, 2), hourly_data