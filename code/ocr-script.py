import pdfplumber
import pandas as pd

def extract_text_from_pdf(pdf_path, section_keyword = "B2"):
    with `pdfplumber.open(pdf_path) as pdf:
        tables = page.extract_tables()
        for table in tables:
            flat_table = "\n".join([" ".join(row) for row in table])
            if section_keyword in flat_table:
                df = pd.DataFrame
                return df
    return None