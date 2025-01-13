import os
import pdfplumber
import pandas as pd
import re

pdf_folder = "/Users/macbook/affirmative-action/data/cds"
output_folder = "/Users/macbook/affirmative-action/data/tables"

section_keywords = ["B1", "B2", "C1", "C9", "G1", "H2"]

def extract_and_save_tables(pdf_folder, output_folder):    
    for pdf_file in os.listdir(pdf_folder):
        if pdf_file.endswith(".pdf"):
            pdf_path = os.path.join(pdf_folder, pdf_file)
            
            extracted_tables = {}
            all_tables = []
            
            with pdfplumber.open(pdf_path) as pdf:
                for page in pdf.pages:
                    tables = page.extract_tables()
                    for table in tables:
                        all_tables.append(table)

            for section_keyword in section_keywords:
                for table in all_tables:
                    flat_table = "\n".join([" ".join(str(cell) if cell is not None else "" for cell in row) for row in table if row])
                    
                    if re.search(rf"\b{section_keyword}\b", flat_table):
                        if section_keyword not in extracted_tables:
                            df = pd.DataFrame(table)
                            extracted_tables[section_keyword] = df
                            break
            
            # Save each extracted table to a CSV file
            for section, df in extracted_tables.items():
                output_file = os.path.join(output_folder, f"{pdf_file.replace('.pdf', '')}_{section}.csv")
                df.to_csv(output_file, index=False)
                print(f"Saved: {output_file}")

extract_and_save_tables(pdf_folder, output_folder)