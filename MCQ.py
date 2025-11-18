import csv


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


if __name__=="__main__":
    
                #csv file path
        csv_path = r"C:\Users\CSH\Desktop\Engeneering Economics\Mcq.csv"
        
        questions = load_questions(csv_path) 
        
        if questions: 
            print(f"sucessfully loaded {len(questions)} questions.")    
            print("\n---- TEST: PRINTING FIRST QUESTION ----")
            print(questions[0])
            print("-----------------------------------------") 
            
        else:
            print("Failed to load questions. Exiting")
                   


    