import os
import pdfplumber
import pandas as pd

input_directory = "/Users/macbook/affirmative-action/data/cds"
output_directory = "/Users/macbook/affirmative-action/data/tables"

keyword = "African American"

def extract_tables_with_keyword(pdf_path, keyword):
    tables = []
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if text and keyword.lower() in text.lower():
                page_tables = page.extract_tables()
                for table in page_tables:
                    if any(
                        keyword.lower() in (str(cell).lower() if cell else '')
                        for row in table for cell in row
                    ):
                        tables.append(table)

    return tables

for filename in os.listdir(input_directory):
    if filename.endswith('.pdf'):
        pdf_path = os.path.join(input_directory, filename)
        tables = extract_tables_with_keyword(pdf_path, keyword)
        for i, table in enumerate(tables):
            df = pd.DataFrame(table)
            csv_filename = f"{os.path.splittext(filename)[0]}_table_{i + 1}.csv"
            csv_path = os.path.join(output_directory, csv_filename)
            df.to_csv(csv_path, index = False)
            print(f"Extracted table from {filename} and saved as {csv_filename}")

print("Table extraction completed.")