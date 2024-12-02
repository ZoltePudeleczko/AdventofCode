from common import *

DAY_NUMBER = 2
USE_EXAMPLE = False

with get_data(DAY_NUMBER, USE_EXAMPLE) as f:
    reports = [
        [int(x) for x in report] for report in (line.split() for line in f.readlines())
    ]


def is_safe(report):
    return all(
        0 < report[i] - report[i + 1] < 4 for i in range(len(report) - 1)
    ) or all(-4 < report[i] - report[i + 1] < 0 for i in range(len(report) - 1))


number_of_safe_reports = 0
number_of_safe_reports_with_tolerance = 0
for report in reports:
    if is_safe(report):
        number_of_safe_reports += 1
        number_of_safe_reports_with_tolerance += 1
    elif any(is_safe(report[:i] + report[i + 1 :]) for i in range(len(report))):
        number_of_safe_reports_with_tolerance += 1


print_result(DAY_NUMBER, 1, number_of_safe_reports)
print_result(DAY_NUMBER, 2, number_of_safe_reports_with_tolerance)
