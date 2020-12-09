from typing import List


def get_file_lines(path: str) -> List[str]:
    with open(path) as f:
        lines = f.readlines()
    return [l.strip() for l in lines if l.strip()]
