#!/usr/bin/env python3
from pathlib import Path
from datetime import datetime
import re

root = Path("./")
notes_path = Path("./BlogArticles/journals/")
output_path = Path("./reymerk-blog/content/posts/")

while not (root / "BlogArticles/").exists():
    root = root.parent

notes_path = root / notes_path
output_path = root / output_path

print("Notes path:", notes_path)
print("Output path:", output_path)

for n_file in notes_path.glob("*.md"):
    if n_file.is_file():
        print("Processing file:", n_file.name)

        with open(n_file, "r") as file:
            content = file.readlines()

            first_line = 0
            while content[first_line] == "" and first_line < len(content):
                first_line += 1

            if first_line == len(content):
                continue

            elif not content[first_line].startswith("# "):
                continue 

            title = content[first_line][2:].strip()
            date_str = datetime.strptime(
                n_file.name, '%Y_%M_%d.md'
            ).strftime('%Y-%m-%dT%H:%M:%S')

            print("Found title:", title)
            print("Found date:", date_str)

            out_file = (output_path / n_file.name)
            if out_file.exists():
                continue 

            with open(out_file, "w") as out_f:
                out_f.writelines([
                    "+++\n",
                    "date='{}'\n".format(date_str),
                    "draft=false\n",
                    "title='{}'\n".format(title),
                    "+++\n",
                ])
                out_f.writelines([
                    line if not line.startswith("- ") else line[2:]
                    for line in content[first_line + 1:]
                ])
                _ = out_f.write("\n")
