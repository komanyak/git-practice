# Функции для записи/чтения текстового файла-резюме

from typing import Dict
import json
import os

OUTPUT_FILE = "person_summary.txt"

def save_summary(person: Dict) -> None:
    """
    Записать краткое текстовое резюме в файл OUTPUT_FILE.
    """
    lines = [
        f"Name: {person.get('name')}",
        f"Age: {person.get('age')}",
        f"Faculty: {person.get('faculty')}",
        "Courses: " + ", ".join(person.get("courses", []))
    ]
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

def read_summary() -> str:
    """
    Вернуть содержимое summary файла, если он существует.
    """
    if not os.path.exists(OUTPUT_FILE):
        return ""
    with open(OUTPUT_FILE, "r", encoding="utf-8") as f:
        return f.read()
    print(f"✅ Summary saved successfully to '{OUTPUT_FILE}'")  # добавили строку
    
    
def hello_world():
    print("Hello from development branch!")