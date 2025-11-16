import csv

# ---------------------------------------------------------
# HELPERS
# ---------------------------------------------------------
def split_pipe(x):
    return [i.strip() for i in x.split("|")] if x and x.strip() else []


# ---------------------------------------------------------
# LOAD CSV
# ---------------------------------------------------------
def load_questions(csv_file):
    data = []
    with open(csv_file, newline='', encoding="cp1252") as f:
        reader = csv.DictReader(f)
        for row in reader:
            q = {
                "id": int(row["id"]),
                "type": row["type"].strip().lower(),
                "label": row["label"].strip(),
                "question": row["question"].strip(),
                "answer": row["answer"].strip(),
                "options": split_pipe(row["options"]),
                "columnA": split_pipe(row["left"]),
                "columnB": split_pipe(row["right"])
            }
            data.append(q)
    return data


# ---------------------------------------------------------
# QUIZ QUESTION FUNCTIONS
# ---------------------------------------------------------

def ask_mcq(q):
    print(f"\n{q['label']} {q['question']}")
    for i, opt in enumerate(q["options"], 1):
        print(f"  {i}. {opt}")

    input("\nPress ENTER to show answer...")
    print("Correct Answer:", q["answer"], "\n")


def ask_fill(q):
    print(f"\n{q['label']} {q['question']}")
    input("Your answer: ")
    print("Correct Answer:", q["answer"], "\n")


def ask_truefalse(q):
    print(f"\n{q['label']} {q['question']}")
    input("True / False? ")
    print("Correct Answer:", q["answer"], "\n")


def ask_match(q):
    print(f"\n{q['label']} {q['question']}\n")

    print("Column A:")
    for a in q["columnA"]:
        print(" ", a)

    print("\nColumn B:")
    for b in q["columnB"]:
        print(" ", b)

    input("\nPress ENTER to show answers...")

    print("\nCorrect Answers:")
    for a, b in zip(q["columnA"], q["columnB"]):
        print(f"{a} → {b}")
    print()


def run_quiz(questions):
    for q in questions:
        print("\n---------------------------------------")
        if q["type"] == "mcq":
            ask_mcq(q)
        elif q["type"] == "fill":
            ask_fill(q)
        elif q["type"] == "truefalse":
            ask_truefalse(q)
        elif q["type"] == "match":
            ask_match(q)


# ---------------------------------------------------------
# DISPLAY QUESTION BY ID
# ---------------------------------------------------------
def display_question_by_id(questions):
    qid = input("Enter question ID: ").strip()

    if not qid.isdigit():
        print("Invalid ID.\n")
        return

    qid = int(qid)

    # get all rows with same ID
    group = [q for q in questions if q["id"] == qid]

    if not group:
        print("No question with this ID.\n")
        return

    print("\n====================================")

    # Extract main question (remove sub-label)
    main_text = group[0]["question"]
    main_text = main_text.replace(group[0]["label"], "").strip()

    print(f"Q. {qid}. {main_text}\n")

    # Print each sub-question
    for q in group:
        qtext = q["question"].replace(q["label"], "").strip()

        print(f"{q['label']} {qtext}")

        if q["type"] == "mcq":
            for i, opt in enumerate(q["options"], 1):
                print(f"   {i}. {opt}")

        elif q["type"] == "match":
            print("\n   Column A:")
            for a in q["columnA"]:
                print("     ", a)

            print("\n   Column B:")
            for b in q["columnB"]:
                print("     ", b)

        print(f"   Answer: {q['answer']}\n")

    print("====================================\n")

# ---------------------------------------------------------
# DUMMY placeholder until you write real shuffle/test logic
# ---------------------------------------------------------
def shuffle_and_show_one_by_one(questions):
    print("\nShuffling not implemented yet.\n")


def test_user(questions):
    print("\nTesting not implemented yet.\n")


# ---------------------------------------------------------
# MENU
# ---------------------------------------------------------
def show_menu():
    print("\n===== QUIZ MENU =====")
    print("1. Shuffle questions and show one by one")
    print("2. Display a question by ID")
    print("3. Test yourself")
    print("4. Exit")


def start_quiz(questions):
    while True:
        show_menu()
        choice = input("Enter choice: ").strip()

        if choice == "1":
            shuffle_and_show_one_by_one(questions)

        elif choice == "2":
            display_question_by_id(questions)

        elif choice == "3":
            test_user(questions)

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")


# ---------------------------------------------------------
# MAIN EXECUTION
# ---------------------------------------------------------
csv_path = r"C:\Users\CSH\Desktop\Engeneering Economics\Mcq.csv"
questions = load_questions(csv_path)

start_quiz(questions)
