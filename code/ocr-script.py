import os
import pdfplumber
import pandas as pd

pdf_folder = "/Users/macbook/affirmative-action/data/cds"
output_folder = "/Users/macbook/affirmative-action/data/tables"

section_keywords = ["B1", "B2", "C1", "C9", "G1", "H2"]

def extract_and_save_tables(pdf_folder, output_folder):
    for pdf_file in os.listdir(pdf_folder):
        if pdf_file.endswith(".pdf"):
            pdf_path = os.path.join(pdf_folder, pdf_file)
            with pdfplumber.open(pdf_path) as pdf:
                for page_number, page in enumerate(pdf.pages, start=1):
                    tables = page.extract_tables()
                    for table_number, table in enumerate(tables, start=1):
                        flat_table = "\n".join([" ".join(str(cell) if cell is not None else "" for cell in row) for row in table if row])
                        for section_keyword in section_keywords:
                            if section_keyword in flat_table:
                                df = pd.DataFrame(table)

                                pdf_name = os.path.splitext(pdf_file)[0]
                                output_filename = f"{pdf_name}_{section_keyword}_page{page_number}_table{table_number}.csv"
                                output_path = os.path.join(output_folder, output_filename)

                                df.to_csv(output_path, index=False, header=False)
                                print(f"Saved: {output_path}")

extract_and_save_tables(pdf_folder, output_folder)