import re

def extract_section(text: str) -> str:
    patterns = [
        r"Article\s*\(?\d+\)?",
        r"Section\s*\d+(\.\d+)*",
        r"Rule\s*\d+(\.\d+)*",
        r"Clause\s*\d+(\.\d+)*",
    ]
    for p in patterns:
        match = re.search(p, text)
        if match:
            return match.group(0)
    return "N/A"