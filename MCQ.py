import csv
import random


def split_pipe(x):
    """Takes the strings like "Option A|Option B" and truns it into a list:
    ['Option A', 'Option B' ]"""
    
    return [i.strip() for i in x.split("|")] if x and x.strip() else[]


def load_questions(csv_path):
    """Loads the csv file and returs a list of dictionaries."""
    
    
    data=[]
    try:
        with open(csv_path, newline='', encoding="cp1252") as f:
        
            reader = csv.DictReader(f)
        
            for row in reader:
            
                q={"id": int(row["id"]),
                "type": row["type"].strip().lower(),
                "lable": row["label"].strip(),
                "question": row["question"].strip(),
                "options": split_pipe(row["options"]),
                "column A": split_pipe(row["left"]),
                "column B": split_pipe(row["right"]),
                }
            data.append(q) 
            
    except FileNotFoundError:
        print(f"Error: The file '{csv_path}' was not found.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
        
    return data

# ----------------------------------
#  shuffel question and test user
# ----------------------------------

def shuffle_and_show_one_by_one(questions):
    print("shufffling not emplemented")
    
def test_user(questions):
    print("testing not implemented")
    
# =====================================
# Display_question_by_id
# =====================================

def display_question_by_id(questions):
    qid = input("Eneter question ID: ").strip()
    
    if not qid.isdigit():
        print("Invalid ID.\n")

    qid = int(qid)
    
    
    group = [q for q in questions if q["id"] == qid]

    if not group:
        print("No question with this ID.\n")
        return
    
    print("\n====================================================")
    
    main_text = group[0]["question"]
    print(f"Q. {qid}. {main_text}\n")
    
    for q in group:
        print(f"{q['lable']}")
        
        if q["type"] == "mcq":
            for i, opt in enumerate(q["options"], 1):
                print(f"    {i}. {opt}")
                
        elif q["type"] == "match":
            print("\n Column A:")
            for a in q["columnA"]:
                print("      ", a)
            
            print("\n Column B :")
            for b in q["columnB"]:
                print("       ", b)
                
                
        print(f"  Answer: {q['answer']} \n")
    print("=========================================\n")
        
   

# ---------------------------------------------------------
# MENU & MAIN LOOP (Check Indentation Carefully!)
# ---------------------------------------------------------
def show_menu():
    print("\n===== QUIZ MENU =====")
    print("1. Shuffle questions and show one by one")
    print("2. Display a question by ID")
    print("3. Test yourself")
    print("4. Exit")


def start_quiz(questions):
    while True: # <--- All code below must be indented once
        show_menu()
        choice = input("Enter choice: ").strip()

        if choice == "1": # <--- All code below must be indented twice
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