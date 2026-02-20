import pdfplumber
import os
import pandas as pd

pdf_path = r"C:\Users\visl2441\workspace\OCR_PRAC\codebase\masterdocs\polycab1.pdf"
output_excel = "extracted_polycab1.xlsx"

rows = []  # will store the extracted data row-wise

print("Running from:", os.getcwd())
print("PDF exists:", os.path.exists(pdf_path))

with pdfplumber.open(pdf_path) as pdf:
    for page_no, page in enumerate(pdf.pages):

        # extract table
        page_table = page.extract_table()
        if not page_table:
            continue

        # only first page is checked
        if page_no == 0:

            start_ind = None #begin here
            

            for i, row in enumerate(page_table):
                row_text = " ".join([str(cell) for cell in row if cell])#join all non-empty cell into a single string

                if "Sr" in row_text and "No" in row_text:
                    start_ind = i
                    break
                
            if start_ind is not None:
                filtered_rows = page_table[start_ind:]
                rows.extend(filtered_rows)

            break  #stop after page 1

df = pd.DataFrame(rows)

df.columns = df.iloc[0]#takes first row of data and use it as col header

df=df[1:]#removes the first row

df = df[df.iloc[:, 0].notna()]#select only where srno is not empty

df.dropna(axis=1, how='all', inplace=True)#drop columns which has all vals as none

df.reset_index(drop=True, inplace=True)#reset the index




print(df)
df.to_excel(output_excel, index=False)

# print(rows)
