# scripts/update_readme.py

from pathlib import Path
import re

CURRENT = Path(__file__).resolve().parent
README = CURRENT / "README.md"
PYTHON_DIR = CURRENT / "python"

# Match:
# p0217_contains_duplicate.py
PROBLEM_PATTERN = re.compile(r"^p\d{4}_.+\.py$")

easy = 0
medium = 0
hard = 0

# Scan all directories
for path in PYTHON_DIR.rglob("*.py"):

    if not PROBLEM_PATTERN.match(path.name):
        continue

    path_str = str(path)

    if "d1_easy" in path_str:
        easy += 1
    elif "d2_medium" in path_str:
        medium += 1
    elif "d3_hard" in path_str:
        hard += 1

total = easy + medium + hard

stats_section = f"""
<!-- STATS_START -->
## Progress

- Total Problems Solved: {total}
- Easy: {easy}
- Medium: {medium}
- Hard: {hard}

<!-- STATS_END -->
"""

content = README.read_text(encoding="utf-8")

start = "<!-- STATS_START -->"
end = "<!-- STATS_END -->"

# Replace existing section if present
if start in content and end in content:
    pattern = re.compile(
        rf"{re.escape(start)}.*?{re.escape(end)}",
        re.DOTALL,
    )

    content = pattern.sub(stats_section.strip(), content)

else:
    # Append section at end
    content += "\n\n" + stats_section.strip() + "\n"

README.write_text(content, encoding="utf-8")

print("README.md updated successfully.")