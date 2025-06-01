import pytest

from src.utils.file_utils import save_report
from src.lib.log_parser import parse_msg3_logs

@pytest.mark.smoke
def test_log_success_rate_above_threshold(default_log_file, default_threshold):
    success_rate, hourly_data = parse_msg3_logs(default_log_file)
    save_report("reports/report.txt", f"Success Rate: {success_rate}%\nHourly Breakdown: {dict(hourly_data)}")
    assert success_rate >= default_threshold, (
        f"Success rate {success_rate}% is below threshold {default_threshold}%"
    )