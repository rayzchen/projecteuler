import os
import sys
import time
import subprocess

parent = os.path.dirname(os.path.abspath(__file__))

files = []
for folder in os.listdir(parent):
    if not os.path.isdir(folder):
        continue

    if "-" not in folder:
        print("Invalid folder:", folder)
        continue
    parts = folder.split("-")
    if len(parts) != 2 or not parts[0].isdigit() or not parts[1].isdigit():
        print("Invalid folder:", folder)
        continue
    lower = int(parts[0])
    upper = int(parts[1])

    for file in os.listdir(os.path.join(parent, folder)):
        if file.startswith("q") and file.endswith(".py"):
            number = file[1:-3]
            if not number.isdigit() or int(number) < lower or int(number) > upper:
                print("Invalid file:", os.path.join(folder, file))
                continue
            files.append((folder, int(number)))

files.sort(key=lambda pair: pair[1])

skip = 0
if len(sys.argv) > 1 and sys.argv[1].isdigit():
    skip = int(sys.argv[1])
    print("Skipping past", skip)

checked = 0
docstring_count = 0
for folder, number in files:
    if number <= skip:
        continue

    print("Checking", number, end="", flush=True)
    checked += 1

    path = os.path.join(parent, folder, f"q{number}.py")
    start = time.perf_counter()
    proc = subprocess.Popen([sys.executable, path], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    stdout, stderr = proc.communicate()
    end = time.perf_counter()

    message = f"\rChecked {number} in {round(end - start, 3)} seconds - answer "
    error = ""
    if stderr:
        print(message)
        print(f"    Output found in stderr")
        continue

    returned_answer = stdout.rstrip()

    with open(path) as f:
        lines = f.read().rstrip().split("\n")

    if " # " not in lines[-1]:
        message += "MISSING"
    else:
        answer_comment = lines[-1].split(" # ")[1]
        if answer_comment != returned_answer:
            message += "\u2718"
        else:
            message += "\u2714"

    if lines[0] == '"""':
        answer_line = lines[lines.index('"""', 1) - 2]
        if " = " in answer_line:
            message += " - docstring "
            docstring_count += 1
            answer_docstring = answer_line.split(" = ")[-1]
            if answer_docstring != returned_answer:
                message += "\u2718"
            else:
                message += "\u2714"

    print(message)

print()
print("Checked", checked, "solutions")
print("Found", docstring_count, "docstrings")

