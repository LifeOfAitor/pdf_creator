import pandas as pd
from fpdf import FPDF
import pandas

pdf = FPDF(orientation="P", unit="mm", format="a4")
df = pd.read_csv("topics.csv")

for index, row in df.iterrows():
    pdf.add_page()
    pdf.set_font(family="Times", style="B", size=12)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="l", ln=1)
    pdf.line(10,21,200,21)
    for i in range(row["Pages"]-1):
        pdf.add_page()
pdf.output("output.pdf")