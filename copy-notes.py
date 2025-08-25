from pathlib import Path
from datetime import datetime

root = Path("./")
notes_path = Path("./BlogArticles/journals/")
output_path = Path("./reymerk-blog/content/posts/")

while not (root / ".git").exists():
    root = root.parent

notes_path = root / notes_path
output_path = root / output_path

for n_file in notes_path.glob("*.md"):
    if n_file.is_file():
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
            date = datetime.strptime(
                n_file.name, '%Y_%M_%d.md'
            )

            out_file = (output_path / n_file.name)
            if out_file.exists():
                continue 

            with open(out_file, "w") as out_f:
                out_f.writelines([
                    "+++",
                    "date='{}'".format(date.strftime('%Y-%m-%dT%H:%M:%S')),
                    "draft=false",
                    "title='{}'".format(title),
                    "+++",
                ])
                out_f.writelines(content[first_line + 1:])
