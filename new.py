from colorama import Fore, Style, init
init(autoreset=True)

# ===== QUIZ DATA =====
questions = [
    
    {
        "type": "fill",
        "question": """Q. 1. Fill in the blanks:
        (i) Particles larger than …… size are considered to be suspended solids in an aqueous media.""",
        "answer": "H2O"
    },
    {
        "type": "fill",
        "question": """(ii) The abbreviation TCU stands for …… colour unit.""",
        "answer": "H2O"
    },
    {
        "type": "fill",
        "question": """(iii) Iron may cause colour problem even at a low concentration like …… mg/l""",
        "answer": "H2O"
    },
    {
        "type": "truefalse",
        "question": """Q. 2. Indicate whether the following statements are True or False:
        (i) If alkalinity is much higher than the total hardness, non-carbonate hardness is expected to be absent.""",
        "answer": "False"
    },
    {
        "type": "truefalse",
        "question": "(iii) Total dissolved solids concentrations are usually very high in surface waters.",
        "answer": "True"
    },
     {
        "type": "truefalse",
        "question": "(iv) In any unpolluted natural system, the alkalinity is caused mostly by the bicarbonates.",
        "answer": "True"
    },
      {
        "type": "truefalse",
        "question": "(v) Lead, chromium, cadmium, zinc, copper, etc., are known as heavy metals, as their atomic numbers are more than 23.",
        "answer": "True"
    },
    {
        "type": "fill",
        "question": """Q. 3. Fill in the blanks:
        (i) Lead, chromium, cadmium, zinc, copper, iron, etc., are known as heavy metals because their atomic numbers are more than ……""",
        "answer": "H2O"
    },
    {
        "type": "fill",
        "question": """(ii) Most common rate of filtration in rapid sand filters is …… m/h.""",
        "answer": "H2O"
    },
    {
        "type": "fill",
        "question": """(iii) Part of the total hardness, which is equivalent to alkalinity, is known as …… hardness.""",
        "answer": "H2O"
    },
    {
        "type": "match",
        "question": """Q. 4. Match the following sets:""",
        "left": ["(i) Mottled teeth", "(ii) Methaemoglobinemia", "(iii) Schmutzdecke"],
        "right": ["(a) Nitrate", "(b) Slow sand filters", "(c) Fluoride"],
        "answer": {"Dog": "Bark", "Cat": "Meow", "Cow": "Moo"}
    },
    {
        "type": "truefalse",
        "question": """Q. 5. Indicate whether the following statements are True or False:
        (i) Chlorine existing in the form of HOCl and/or OCl⁻ is defined as free available chlorine.""",
        "answer": "False"
    },
    {
        "type": "truefalse",
        "question": "(ii) Ferrule is one of the important appurtenances installed in a combined sewage system.",
        "answer": "True"
    },
    {
        "type": "mcq",
        "question": """Q. 6. Choose the correct statement in the following:
        (i) The microorganism group E. Coli is used as an indicator of faecal contamination of water because:""",
        "options": ["(a) E. Coli is a known pathogen", "(b) It is very easy to detect", "(c) They are discharged along with faeces in large number", "(d) All of the above"],
        "answer": "Paris"
    },
    {
        "type": "mcq",
        "question": "(ii) Pathogenic organisms may be found in contaminated waters and are responsible for diseases like:",
        "options": ["(a) Typhoid fever", "(b) Infectious hepatitis", "(c) Gastro-enteritis", "(d) All of the above"],
        "answer": "Paris"
    },
    {
        "type": "mcq",
        "question": "(iii) If the chlorine fed and chlorine demand of water is 1.5 mg/l and 1.3 mg/l respectively, the residual chlorine in g/m³ is:",
        "options": ["(a) 0.2 ", "(b) 2.0", "(c) 20 ", "(d) 0.02"],
        "answer": "Paris"
    },
    {
        "type": "match",
        "question": """3. Match the following:""",
        "left": ["Dog", "Cat", "Cow"],
        "right": ["Meow", "Moo", "Bark"],
        "answer": {"Dog": "Bark", "Cat": "Meow", "Cow": "Moo"}
    },
    
    {
        "type": "fill",
        "question": "6. Fill in the blank: The Earth revolves around the ____.",
        "answer": "Sun"
    },
    {
        "type": "mcq",
        "question": "7. Which programming language is used for AI?",
        "options": ["C", "Java", "Python", "HTML"],
        "answer": "Python"
    }
]

# ===== QUIZ LOGIC =====
score = 0

def get_input_with_double_enter(prompt, correct_answer=None):
    """
    Custom input function that tracks double Enter.
    If user presses Enter twice consecutively, reveals the correct answer.
    """
    blank_count = 0
    while True:
        user_input = input(prompt).strip()
        if user_input == "":
            blank_count += 1
            if blank_count == 2:
                if correct_answer:
                    print(Fore.YELLOW + f"💡 The correct answer is: {correct_answer}")
                return None  # reveal answer, stop input
        else:
            return user_input

def ask_mcq(q):
    print(Fore.CYAN + q["question"])
    for i, opt in enumerate(q["options"], 1):
        print(f"  {i}. {opt}")
    choice = get_input_with_double_enter(Fore.YELLOW + "\nEnter your choice (1-4): ", q["answer"])
    if choice is None:
        return 0
    if not choice.isdigit() or int(choice) not in range(1, len(q["options"]) + 1):
        print(Fore.RED + "Invalid input. Skipping this question.")
        return 0
    if q["options"][int(choice) - 1].lower() == q["answer"].lower():
        print(Fore.GREEN + "✅ Correct!")
        return 1
    else:
        print(Fore.RED + f"❌ Wrong! Correct answer is: {q['answer']}")
        return 0

def ask_fill(q):
    print(Fore.CYAN + q["question"])
    ans = get_input_with_double_enter(Fore.YELLOW + "Your answer: ", q["answer"])
    if ans is None:
        return 0
    if ans.lower() == q["answer"].lower():
        print(Fore.GREEN + "✅ Correct!")
        return 1
    else:
        print(Fore.RED + f"❌ Wrong! Correct answer is: {q['answer']}")
        return 0

def ask_match(q):
    print(Fore.CYAN + q["question"])
    left = q["left"]
    right = q["right"]

    print("\nLeft Side:")
    for i, l in enumerate(left, 1):
        print(f"  {i}. {l}")

    print("\nRight Side:")
    for j, r in enumerate(right, 1):
        print(f"  {j}. {r}")

    print(Fore.YELLOW + "\nEnter your matches like: 1-3, 2-1, 3-2 (Press Enter twice to show answers)")
    user_input = get_input_with_double_enter("Your matches: ", ", ".join([f"{k}→{v}" for k, v in q["answer"].items()]))
    if user_input is None:
        return 0

    pairs = user_input.replace(" ", "").split(",")
    correct_pairs = q["answer"]
    user_correct = 0

    try:
        for pair in pairs:
            l_idx, r_idx = map(int, pair.split("-"))
            l_item = left[l_idx - 1]
            r_item = right[r_idx - 1]
            if correct_pairs[l_item].lower() == r_item.lower():
                user_correct += 1
    except Exception:
        print(Fore.RED + "⚠️ Invalid format! Skipping question.")
        return 0

    if user_correct == len(left):
        print(Fore.GREEN + "✅ All correct matches!")
        return 1
    else:
        print(Fore.RED + f"❌ {user_correct}/{len(left)} matches correct.")
        print("Correct matches:")
        for k, v in correct_pairs.items():
            print(Fore.BLUE + f"  {k} → {v}")
        return 0

def ask_truefalse(q):
    print(Fore.CYAN + q["question"])
    ans = get_input_with_double_enter(Fore.YELLOW + "Enter True or False: ", q["answer"])
    if ans is None:
        return 0
    ans = ans.capitalize()
    if ans not in ["True", "False"]:
        print(Fore.RED + "⚠️ Invalid input! Must be True or False.")
        return 0
    if ans == q["answer"]:
        print(Fore.GREEN + "✅ Correct!")
        return 1
    else:
        print(Fore.RED + f"❌ Wrong! Correct answer is: {q['answer']}")
        return 0


# ===== MAIN QUIZ LOOP =====
print(Style.BRIGHT + Fore.MAGENTA + "\n===== TERMINAL QUIZ GAME =====\n")

for q in questions:
    print(Style.BRIGHT + "-" * 60)
    q_type = q["type"]
    if q_type == "mcq":
        score += ask_mcq(q)
    elif q_type == "fill":
        score += ask_fill(q)
    elif q_type == "match":
        score += ask_match(q)
    elif q_type == "truefalse":
        score += ask_truefalse(q)
    input(Fore.WHITE + "\nPress Enter to continue to the next question...")

print("\n" + "-" * 60)
print(Style.BRIGHT + Fore.GREEN + f"🎯 Final Score: {score}/{len(questions)}")
print(Style.BRIGHT + Fore.CYAN + "Thanks for playing!")
