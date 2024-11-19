import os
import pdfplumber
import pandas as pd

directory = "../data/cds"

keywords = ["African American"]

def extract_tables_with_keywords(pdf_path, keywords):
    tables = []
    with pdfplumber.open(pdf_path) as pdf:
        for page_number, page in enumerate(pdf.pages):
            text = page.extract_text()
            if text and any(keyword.lower() in text.lower() for keyword in keywords):
                page_tables = page.extract_tables()
                for table in page_tables:
                    tables.appen({
                        'page_number': page_number + 1
                        'table': table
                    })
    return tables

all_tables = []
for filename in os.listdir(directory):
    if filename.endswith('.pdf'):
        pdf_path = os.path.join(directory, filename)
        tables = extract_tables_with_keywords(pdf_path, keywords)
        if tables:
            for item in tables:
                df = pd.DataFrame(item['table'])
                csv_filename = f"{os.path.splitext(filename)[0]}_page_{item['page_number']}.csv"
                csv_path = os.path.join(directory, csv_filename)
                df.to_csv(csv_path, index = False)
                print(f"Extracted table from {filename} (Page {item['page_number']}) and
                      saved as {csv_filename}")
                
print("Table extract completed")