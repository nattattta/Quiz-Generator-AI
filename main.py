import os
from utils import load_text_file, load_pdf_file, transcribe_audio, extract_audio_from_video
from quiz_engine import generate_questions, run_quiz, save_quiz_to_file

def main():
    print("Select file type:")
    print("1. Text (.txt)")
    print("2. PDF (.pdf)")
    print("3. Audio (.mp3)")
    print("4. Video (.mp4)")

    choice = input("Enter your choice (1/2/3/4): ")

    file_path = input("Enter file path: ")

    if not os.path.exists(file_path):
        print("❌ Error: The file path you entered does not exist. Please check and try again.")
        return

    if choice == "1":
        content = load_text_file(file_path)
    elif choice == "2":
        content = load_pdf_file(file_path)
    elif choice == "3":
        content = transcribe_audio(file_path)
    elif choice == "4":
        audio_path = extract_audio_from_video(file_path)
        content = transcribe_audio(audio_path)
    else:
        print("Invalid choice.")
        return

    print("\nGenerating quiz questions...\n")
    questions_text = generate_questions(content)
    
    # Ask if user wants to provide a custom filename
    custom_filename = input("\nDo you want to provide a custom filename for the quiz? (default: auto-generated): ")
    if custom_filename.strip():
        saved_path = save_quiz_to_file(questions_text, filename=custom_filename)
    else:
        saved_path = save_quiz_to_file(questions_text)
    
    print(f"Quiz saved to: {saved_path}")
    
    run_quiz(questions_text)

if __name__ == "__main__":
    main()
