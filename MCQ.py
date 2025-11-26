import csv
import random


def split_pipe(x):
    """Takes the strings like "Option A|Option B" and truns it into a list:
    ['Option A', 'Option B' ]"""
    
    return [i.strip() for i in x.split("|")] if x and x.strip() else[]


# ---------------------------------------------------------
# LOAD CSV
# ---------------------------------------------------------
def load_questions(csv_file):
    data = []
    try:
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
                
    except FileNotFoundError:
        print(f"Error: The file '{csv_file}' was not found.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
        
    return data

# ----------------------------------
#  shuffel question and test user
# ----------------------------------

def ask_mcq(q):
    print(f"\n{q['question']}")
    print(f"\n{q['label']}")
    for i, opt in enumerate(q["options"], 1):
        print(f"    {i}. {opt}")
        input("\n Press ENTER to show answer: ")
        print(f"Correct Answer: {q['answer']}\n")
        
def ask_fill(q):
    print(f"\n{q['label']}")
    input("Your Answer: ")
    print(f"Correct Answer: {q['answer']}\n")
    
    
def ask_true(q):
    print(f"\n{q['label']}")
    input("True / False? : ")
    print(f"Correct Answer: {q['answer']}\n")
    
def ask_match(q):
    print(f"\n{q['question']}")
    
    
    txt_a = q['columnA'][0] if q['columnA'] else q['label']
    
            
            
    print(f"   {txt_a:<40}")


    input("\n Press ENTER to show answer: ")
    print(f"Correct Answer: {q['answer']}\n")


def shuffle_and_show_one_by_one(questions):
    print("\n shufffling questions.....")
    shuffled_questions = list(questions)
    random.shuffle(shuffled_questions)
    
    print(f"Starting study mode with {len(shuffled_questions)} questions. \n")
    
    for q in shuffled_questions:
        print("-----------------------------------------")
        
        if q["type"]=="mcq":
            ask_mcq(q)
        elif q["type"] == "fill":
            ask_fill(q)
        elif q["type"] == "truefasle":
            ask_true(q)
        elif q["type"] == "match":
            ask_match(q)
            
            print("---End of shuffled questions---")
            
            
# ============== Test user : ===============
  
def test_user(questions):
    
    print(f"\n{q['lable']}")
    
   
    
# =====================================
# Display_question_by_id (TEXTBOOK FORMAT)
# =====================================
def display_question_by_id(questions):
    qid = input("Enter question ID: ").strip()

    if not qid.isdigit():
        print("Invalid ID.\n")
        input("press ENTER to continue...")
        return

    qid = int(qid)
    
    
    group = [q for q in questions if q["id"] == qid]

    if not group:
        print("No question with this ID.\n")
        input("Press ENTER to continue...")
        return

    print("\n====================================================")
    
    
    main_text = group[0]["question"]
    print(f"Q. {qid}. {main_text}\n")

    
    if group[0]["type"] == "match":
        
       
        print(f"   {'Column A':<40}Column B")
        print(f"   {'-'*35}     {'-'*30}") 

        
        for q in group:
            
            txt_a = q['columnA'][0] if q['columnA'] else q['label']
            txt_b = q['columnB'][0] if q['columnB'] else ""
            
            
            print(f"   {txt_a:<40}{txt_b}")

        
        print("\n   [ Answer Key ]")
        for q in group:
             
             
             source_text= q['label'] if q['label'] else (q['columnA'][0] if q['columnA'] else "")
             
             label_part = source_text.split(' ')[0]          
             
             print(f"   {label_part} -> {q['answer']}")
             
            
    
    else:
        for q in group:
            print(f"{q['label']}") 
            
            if q["type"] == "mcq":
                for i, opt in enumerate(q["options"], 1):
                    print(f"    {i}. {opt}")
                    
            print(f"   Answer: {q['answer']} \n")

    print("=========================================\n")
    
    input("Press ENTER to return to menue...")

# ---------------------------------------------------------
# MENU & MAIN LOOP 
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
    # ======= Main loop ========      
    

    # ---------------------------------------------------------
# MAIN EXECUTION
# ---------------------------------------------------------

if __name__ == "__main__":
    
    
    csv_path = r"C:\Users\CSH\Desktop\Engeneering Economics\Mcq.csv"
    questions = load_questions(csv_path)
    
    # --- CHECKPOINT B ---
    if questions:
        print(f"SUCCESS: Loaded {len(questions)} questions.")
        
        
        first_id = questions[0]["id"]
        print(f"DEBUG: The first loaded question has ID: {first_id}")
        
        # --- CHECKPOINT C ---
        print("Starting Menu...")
        start_quiz(questions) 
    else:
        print("FAILURE: Questions is None. Exiting.")