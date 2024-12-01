import os
import datetime

def get_files():
    for root, dirs, files in os.walk("."):
        for file in files:
            yield os.path.join(root, file)

files = get_files()
files = [file.replace("\\", "/")[2:] for file in files]
files = [file for file in files if not file.startswith(".git")]
ignore = ["generate.py", "index.html", "template.html"]
files = [file for file in files if file not in ignore]

files.sort()

files = "\n".join([f'<a href="{file}">{file}</a><br>' for file in files])

# generate index.html
with open("template.html") as f:
    template = f.read()

with open("index.html", "w+") as f:
    f.write(template.replace("{{files}}", files).replace("{{date}}", str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))))
