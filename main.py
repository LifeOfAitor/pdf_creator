import pandas as pd
from fpdf import FPDF
import pandas

pdf = FPDF(orientation="P", unit="mm", format="a4")
pdf.set_auto_page_break(auto=False, margin=0)

df = pd.read_csv("topics.csv")

pagecount = 0
for index, row in df.iterrows():
    pdf.add_page()
    # set header
    pdf.set_font(family="Times", style="B", size=12)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="l", ln=1)
    # add lines
    for i in range(21, 290, 10):
        pdf.line(10, i, 200, i)

    # footer - add 265 breaklines
    pdf.ln(265)
    pdf.set_font(family="Times", style="I", size=8)
    pdf.cell(w=0, h=5, txt=row["Topic"], align="C", ln=1)
    pdf.cell(w=0, h=5, txt=f"{pagecount + 1}", align="C")
    pagecount+=1

    # add extra pages
    for i in range(row["Pages"]-1):
        pdf.add_page()
        # add lines
        for i in range(21, 290, 10):
            pdf.line(10, i, 200, i)
        # footer - add 277 breaklines
        pdf.ln(277)
        pdf.set_font(family="Times", style="I", size=8)
        pdf.cell(w=0, h=5, txt=row["Topic"], align="C", ln=1)
        pdf.cell(w=0, h=5, txt=f"{pagecount + 1}", align="C")
        pagecount += 1

pdf.output("output.pdf")