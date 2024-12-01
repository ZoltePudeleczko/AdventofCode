import os
from pathlib import Path


def get_data(day_number, use_example=False):
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    filename = f"day{day_number}_ex" if use_example else f"day{day_number}"
    path = Path(f"../inputs/{filename}")

    return open(path)


def print_result(day_number, part, result):
    print(f"{day_number}-{part}: {result}")
