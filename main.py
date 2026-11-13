FILE_NAME = "results.txt"


def calculate_total(maths, physics, chemistry):
    return maths + physics + chemistry


def calculate_percentage(total):
    return total / 3


def calculate_result(maths, physics, chemistry):
    if maths >= 40 and physics >= 40 and chemistry >= 40:
        return "Pass"
    return "Fail"


def load_records():
    records = []

    try:
        with open(FILE_NAME, "r") as file:
            for line in file:
                line = line.strip()
                if line:
                    # Each line contains one saved student dictionary.
                    import ast
                    records.append(ast.literal_eval(line))
    except FileNotFoundError:
        pass

    return records


def save_records(records):
    with open(FILE_NAME, "w") as file:
        for student in records:
            file.write(str(student) + "\n")


def add_student(records):
    roll = input("Enter roll number: ").strip()

    # Roll numbers must be unique.
    for student in records:
        if student["roll"] == roll:
            print("Roll number", roll, "already exists.")
            return

    name = input("Enter student name: ").strip()
    if not name:
        print("Name cannot be empty.")
        return

    try:
        maths = int(input("Enter Maths marks: "))
        physics = int(input("Enter Physics marks: "))
        chemistry = int(input("Enter Chemistry marks: "))
    except ValueError:
        print("Marks must be numbers between 0 and 100.")
        return

    if not (0 <= maths <= 100 and 0 <= physics <= 100
            and 0 <= chemistry <= 100):
        print("Marks must be between 0 and 100.")
        return

    total = calculate_total(maths, physics, chemistry)
    percentage = calculate_percentage(total)
    result = calculate_result(maths, physics, chemistry)

    student = {
        "roll": roll,
        "name": name,
        "maths": maths,
        "physics": physics,
        "chemistry": chemistry,
        "total": total,
        "percentage": percentage,
        "result": result
    }

    records.append(student)
    save_records(records)

    print("Record added:", roll, "|", name)
    print("Total:", total, "| Percentage: {:.2f}% | Result: {}".format(
        percentage, result
    ))


def view_all(records):
    if not records:
        print("No student records found.")
        return

    for student in records:
        print(
            student["roll"], "|", student["name"],
            "| Total:", student["total"],
            "| Percentage: {:.2f}%".format(student["percentage"]),
            "| Result:", student["result"]
        )


def show_rank_list(records):
    if not records:
        print("No student records found.")
        return

    ranked_records = sorted(
        records, key=lambda student: student["total"], reverse=True
    )

    for rank, student in enumerate(ranked_records, start=1):
        print(
            "Rank", rank, "|",
            student["roll"], "|",
            student["name"], "|",
            student["total"], "|",
            "{:.2f}%".format(student["percentage"]), "|",
            student["result"]
        )


def main():
    records = load_records()

    while True:
        print("\n===== Exam Result Management System =====")
        print("1. Add student")
        print("2. View all")
        print("3. Rank list")
        print("4. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_student(records)
        elif choice == "2":
            view_all(records)
        elif choice == "3":
            show_rank_list(records)
        elif choice == "4":
            print("Thank you!")
            break
        else:
            print("Invalid menu option. Please choose 1 to 4.")


if __name__ == "__main__":
    main()
