import os
import re
import pdfplumber
import pandas as pd

pdf_folder = "/Users/macbook/affirmative-action/data/cds"
output_folder = "/Users/macbook/affirmative-action/data/tables"

section_keywords = ["B1", "B2", "C1", "C9", "G1", "H2"]

def extract_and_save_tables(pdf_folder, output_folder):    
    for pdf_file in os.listdir(pdf_folder):
        if pdf_file.endswith(".pdf"):
            pdf_path = os.path.join(pdf_folder, pdf_file)
            
            extracted_tables = {}
            
            with pdfplumber.open(pdf_path) as pdf:
                for page in pdf.pages:
                    text = page.extract_text()
                    for section_keyword in section_keywords:
                        if re.search(rf"\b{section_keyword}\b", text):
                            tables = page.extract_tables()
                            for table in tables:
                                if section_keyword not in extracted_tables:
                                    df = pd.DataFrame(table)
                                    extracted_tables[section_keyword] = df
                            break
            
            for section, df in extracted_tables.items():
                output_file = os.path.join(output_folder, f"{pdf_file.replace('.pdf', '')}_{section}.csv")
                df.to_csv(output_file, index=False)
                print(f"Saved: {output_file}")

def extract_and_save_african_tables(pdf_folder, output_folder):
    for pdf_file in os.listdir(pdf_folder):
        if pdf_file.endswith(".pdf"):
            pdf_path = os.path.join(pdf_folder, pdf_file)
            
            extracted_tables = {}
            
            with pdfplumber.open(pdf_path) as pdf:
                for page in pdf.pages:
                    tables = page.extract_tables()
                    for table in tables:
                        flat_table = "\n".join([" ".join(str(cell) if cell is not None else "" for cell in row) for row in table if row])
                        if re.search(r"\bAfrican\b", flat_table):
                            df = pd.DataFrame(table)
                            extracted_tables[pdf_file] = df
                            break
            
            for section, df in extracted_tables.items():
                output_file = os.path.join(output_folder, f"{pdf_file.replace('.pdf', '')}_African.csv")
                df.to_csv(output_file, index=False)
                print(f"Saved: {output_file}")

extract_and_save_tables(pdf_folder, output_folder)
extract_and_save_african_tables(pdf_folder, output_folder)