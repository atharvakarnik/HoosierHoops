import os
import pdfplumber
import pandas as pd

data_dir = os.path.join(os.path.dirname(__file__), '..', 'Data')

def display_tables(pdf_file):
    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages:
            tables = page.extract_tables()
            for i, table in enumerate(tables):
                df = pd.DataFrame(table[1:], columns=table[0])
                print(f"Table {i+1}:")
                print(df)
                print("\n")

if __name__ == '__main__':
    pdf_files = [os.path.join(data_dir, f) for f in os.listdir(data_dir) if f.endswith('.pdf')]
    for pdf_file in pdf_files:
        display_tables(pdf_file)