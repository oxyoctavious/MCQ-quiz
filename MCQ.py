import csv

def split_pipe(x):
    return [i.strip() for i in x.split("|")] if x and x.strip() else []

def load_questions(csv_file):
    questions = []
    with open(csv_file, newline='', encoding="utf-8") as f:
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
