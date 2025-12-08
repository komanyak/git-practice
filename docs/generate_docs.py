import os
import utils

DOC_FILE = "docs/documentation.txt"

def generate_docs():
    content = [
        "=== Project Documentation ===",
        "Files in project: data.py, feature2.py, main.py, utils.py",
        "Main functions:",
        " - pretty_print_person(person) in main.py",
        " - save_summary(person) and read_summary() in utils.py",
        " - feature2() in feature2.py",
        " - hello_world() in utils.py (development branch)"
    ]
    
    os.makedirs(os.path.dirname(DOC_FILE), exist_ok=True)
    with open(DOC_FILE, "w", encoding="utf-8") as f:
        f.write("\n".join(content))
    print(f"Documentation generated: {DOC_FILE}")

if __name__ == "__main__":
    generate_docs()
