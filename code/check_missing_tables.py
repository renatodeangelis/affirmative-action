import os

def check_missing_tables(pdf_folder, output_folder, section_keywords):
    missing_combinations = []

    # Get list of PDF files
    pdf_files = [f for f in os.listdir(pdf_folder) if f.endswith(".pdf")]

    # Get list of saved CSV files
    saved_csv_files = [f for f in os.listdir(output_folder) if f.endswith(".csv")]

    for pdf_file in pdf_files:
        college_year = pdf_file.replace(".pdf", "")
        for section_keyword in section_keywords:
            expected_csv = f"{college_year}_{section_keyword}.csv"
            if expected_csv not in saved_csv_files:
                missing_combinations.append(f"{college_year}-{section_keyword}")

    if missing_combinations:
        print("Missing college-year-section keyword combinations:")
        for combination in missing_combinations:
            print(combination)
    else:
        print("No missing combinations found.")

pdf_folder = "/Users/macbook/affirmative-action/data/cds"
output_folder = "/Users/macbook/affirmative-action/data/tables"
section_keywords = ["B1", "B2", "C1", "C9", "G1", "H2"]

check_missing_tables(pdf_folder, output_folder, section_keywords)