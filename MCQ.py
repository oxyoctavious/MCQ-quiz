import csv

def split_pipe(x):
    return [i.strip() for i in x.split("|")] if x and x.strip() else []

def load_questions(csv_file):
    questions = []
    with open(csv_file, newline='', encoding="cp1252") as f:
        reader = csv.DictReader(f)
        for row in reader:
            q = {
                "id": int(row["id"]),
                "type": row["type"].strip().lower(),
                "label": row["label"].strip(),
                "question": row["question"].strip(),
                "answer": row["answer"].strip()
            }

            if q["type"] == "mcq":
                q["options"] = split_pipe(row["options"])

            if q["type"] == "match":
                q["left"] = split_pipe(row["left"])
                q["right"] = split_pipe(row["right"])

            questions.append(q)

    return questions


# ============ CSV file: ==============
csv_path = r"C:\Users\CSH\Desktop\Engeneering Economics\Mcq.csv"
questions = load_questions(csv_path)

# ========= Menue ============
def show_menu():
    print("\n===== QUIZ MENU =====")
    print("1. Shuffle questions and show one by one")
    print("2. Display a question by ID")
    print("3. Test yourself")
    print("4. Exit")

def start_quiz():
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


# Start the quiz here
start_quiz()


# ============ MCQ LOgic: =============
def ask_mcq(q):
    print(f"\n{q['label']} {q['question']}")
    for i, opt in enumerate(q["options"], 1):
        print(f"  {i}. {opt}")

    user = input("\nYour answer (1-4): ").strip()
    
    if user.isdigit() and 1 <= int(user) <= len(q["options"]):
        chosen = q["options"][int(user)-1]
    else:
        chosen = ""

    print(f"Correct Answer: {q['answer']}\n")
def ask_fill(q):
    print(f"\n{q['label']} {q['question']}")
    user = input("Your answer: ").strip()
    print(f"Correct Answer: {q['answer']}\n")

# =========== Fill in the blanks Logic ==============
def ask_fill(q):
    print(f"\n{q['label']} {q['question']}")
    user = input("Your answer: ").strip()
    print(f"Correct Answer: {q['answer']}\n")
    
# =============== True or False ==============
def ask_truefalse(q):
    print(f"\n{q['label']} {q['question']}")
    user = input("True / False? ").strip().capitalize()
    print(f"Correct Answer: {q['answer']}\n")
    
# ================ Match The Following logic ==================
def ask_match(q):
    print(f"\n{q['label']} {q['question']}\n")

    print("Column A:")
    for i, item in enumerate(q["left"], 1):
        print(f"  {i}. {item}")

    print("\nColumn B:")
    for i, item in enumerate(q["right"], 1):
        print(f"  {i}. {item}")

    user = input("\nEnter matches (e.g. 1-3, 2-1, 3-2): ").strip()
    print("\nCorrect Answers:")
    for left_item, right_item in zip(q["left"], q["right"]):
        print(f"{left_item} → {right_item}")
    print()
    
    
    
# ============= Main quiz logic ==================
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
