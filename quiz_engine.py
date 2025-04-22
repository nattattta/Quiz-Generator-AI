import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_questions(content, num_questions=20):
    prompt = f"""Based on the following content, create {num_questions} multiple-choice quiz questions.
Each question should have 4 options (A, B, C, D) and indicate the correct option.
Return the result in this format:
Question: ...
A: ...
B: ...
C: ...
D: ...
Answer: ...

Content:
{content}
"""
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content.strip()

def save_quiz_to_file(questions_text, filename="quiz"):
    # Create output directory if it doesn't exist
    output_dir = os.path.join(os.getcwd(), "output")
    os.makedirs(output_dir, exist_ok=True)
    
    # Generate a unique filename if none provided
    if filename == "quiz":
        from datetime import datetime
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"quiz_{timestamp}"
    
    # Ensure the filename has .txt extension
    if not filename.endswith(".txt"):
        filename += ".txt"
    
    # Create the full file path
    file_path = os.path.join(output_dir, filename)
    
    # Save the content to the file
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(questions_text)
    
    return file_path

def run_quiz(questions_text):
    questions = questions_text.split("\n\n")
    score = 0
    total = len(questions)

    print("\nWelcome to the AI-powered Quiz!\n")

    for q in questions:
        if not q.strip():
            continue

        lines = q.split("\n")
        correct_line = [line for line in lines if line.startswith("Answer:")][0]
        correct_answer = correct_line.split(":")[1].strip()

        question_without_answer = "\n".join([line for line in lines if not line.startswith("Answer:")])
        print(question_without_answer)

        user_answer = input("Your answer (A/B/C/D): ").strip().upper()

        if user_answer == correct_answer:
            print("✅ Correct!\n")
            score += 1
        else:
            print(f"❌ Incorrect. The correct answer was {correct_answer}\n")

    print(f"Quiz complete! Your score: {score}/{total}")
