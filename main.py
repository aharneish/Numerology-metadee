# --- Main script for running numerology and generating a report ---
from numerology import get_numerology_profile
from prompt import build_prompt
from llm_inference import generate_report

def main():
    """
    Command-line interface for the numerology app.
    Prompts user for name and DOB, generates numerology profile and report.
    """
    full_name = input("Enter your full name: ")
    dob = input("Enter your date of birth in the format 'YYYY-MM-DD: ")
    numerology_profile = get_numerology_profile(full_name, dob)
    prompt_resp = build_prompt(numerology_profile)
    report = generate_report(prompt_resp, use_rag=True)

    print("\n Final Devotional Numerology Report:\n")
    print(report)

if __name__ == "__main__":
    main()