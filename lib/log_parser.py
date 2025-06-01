import re

def parse_msg3_logs(log_path):
    success_pattern = re.compile(r"type\s+MSG3.*?status\s+success", re.IGNORECASE)
    failure_pattern = re.compile(r"type\s+MSG3.*?status\s+(?!success)\w+", re.IGNORECASE)
    time_pattern = re.compile(r"(\d{4}-\d{2}-\d{2} \d{2})")

    total_success = total_failure = 0
    hourly_data = {}  # Regular dictionary

    with open(log_path) as f:
        for line in f:
            time_match = time_pattern.match(line)
            if not time_match:
                continue

            hour = time_match.group(1)

            # Ensure the hour entry exists
            if hour not in hourly_data:
                hourly_data[hour] = {"success": 0, "failure": 0}

            if success_pattern.search(line):
                total_success += 1
                hourly_data[hour]["success"] += 1
            elif failure_pattern.search(line):
                total_failure += 1
                hourly_data[hour]["failure"] += 1

    total = total_success + total_failure
    success_rate = (total_success / total * 100) if total else 0

    return round(success_rate, 2), hourly_data
