from colorama import Fore, Style, init
init(autoreset=True)

# Quiz Data
questions = [
    {
        "type": "fill",
        "question": """Q. 1. Fill in the blanks:
(i) Particles larger than …… size are considered to be suspended solids in an aqueous media.
""",
        "answer": "1 μm (micron)"
    },
    {
        "type": "fill",
        "question": "(ii) The abbreviation TCU stands for …… colour unit.",
        "answer": "True"
    },
    {
        "type": "fill",
        "question": "(iii) Iron may cause colour problem even at a low concentration like …… mg/l.",
        "answer": "0.3"
    },
    {
        "type": "True or false",
        "question": """Q. 2. Indicate whether the following statements are True or False:
(i) If alkalinity is much higher than the total hardness, non-carbonate hardness is expected to be absent.
""",
        "answer": "True"
    },
    
    {
        "type": "True or false",
        "question": """(ii) Mottled and discoloured teeth occur when drinking water supply contains excessive fluorides.""",
        "answer": "True"
    },
    {
        "type": "True or false",
        "question": """(iii) Total dissolved solids concentrations are usually very high in surface waters.
""",
        "answer": "False"
    },
    
    {
        "type": "True or false",
        "question": """(iv) In any unpolluted natural system, the alkalinity is caused mostly by the bicarbonates.
""",
        "answer": "True"
    },
    {
        "type": "True or false",
        "question": """(v) Lead, chromium, cadmium, zinc, copper, etc., are known as heavy metals, as their atomic numbers are more than 23.""",
        "answer": "True"
    },
    
    {
        "type": "match",
        "question": "3. Match the following:",
        "left": ["Dog", "Cat", "Cow"],
        "right": ["Meow", "Moo", "Bark"],
        "answer": {"Dog": "Bark", "Cat": "Meow", "Cow": "Moo"}
    },
    {
        "type": "mcq",
        "question": "4. Which programming language is mainly used for AI?",
        "options": ["C", "Java", "Python", "HTML"],
        "answer": "Python"
    },
    {
        "type": "fill",
        "question": "5. Fill in the blank: The Earth revolves around the ____.",
        "answer": "Sun"
    }
]

score = 0

def ask_mcq(q):
    print(Fore.CYAN + q["question"])
    for i, opt in enumerate(q["options"], 1):
        print(f"  {i}. {opt}")
    choice = input(Fore.YELLOW + "\nEnter your choice (1-4): ").strip()
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
    ans = input(Fore.YELLOW + "Your answer: ").strip()
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

    print(Fore.YELLOW + "\nEnter your matching pairs in the format '1-3, 2-1, 3-2'")

    user_input = input("Your matches: ").replace(" ", "")
    pairs = user_input.split(",")

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

# Main Quiz Loop
print(Style.BRIGHT + Fore.MAGENTA + "\n===== WELCOME TO THE TERMINAL QUIZ =====\n")

for q in questions:
    print(Style.BRIGHT + "-" * 50)
    if q["type"] == "mcq":
        score += ask_mcq(q)
    elif q["type"] == "fill":
        score += ask_fill(q)
    elif q["type"] == "match":
        score += ask_match(q)
    input(Fore.WHITE + "\nPress Enter to continue to the next question...")

print("\n" + "-" * 50)
print(Style.BRIGHT + Fore.GREEN + f"🎯 Your final score: {score}/{len(questions)}")
print(Style.BRIGHT + Fore.CYAN + "Thanks for playing!")
