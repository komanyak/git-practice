from data import PERSON
import utils

def pretty_print_person(person):
    print("=== Person ===")
    print(f"Name: {person['name']}")
    print(f"Age: {person['age']}")
    print(f"Faculty: {person['faculty']}")
    print("Courses:")
    for c in person['courses']:
        print(" -", c)
    print("================\n")

def main():
    # Печатаем данные в консоль
    pretty_print_person(PERSON)

    # Сохраняем в текстовый файл
    utils.save_summary(PERSON)
    print("Saved summary to file:", utils.OUTPUT_FILE)

    # Считываем и показываем содержимое файла
    txt = utils.read_summary()
    print("\n--- Summary file content ---")
    print(txt)
    print("----------------------------")
    
    print("Release version 1.0")

if __name__ == "__main__":
    main()
