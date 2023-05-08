from fpdf import FPDF
import pandas as pd
df = pd.read_csv('topics (1).csv')
pdf =FPDF(orientation="p",unit="mm",format="A4")
pdf.set_auto_page_break(auto=False)
for index,row in df.iterrows():
    for i in range(row['Pages']):
        pdf.add_page()
        pdf.set_font(family="Times",style="B",size=24)
        pdf.set_text_color(100, 100, 100)
        pdf.cell(w=0, h=12, txt=row["Topic"], ln=1, align="L")
        for i in range(20,298,10):
            pdf.line(10, i, 200, i)
        pdf.ln(265)
        pdf.set_font(family="Times", style="I", size=10)
        pdf.set_text_color(100, 100, 100)
        pdf.cell(w=0, h=12, txt=row["Topic"], ln=1, align='R')
pdf.output('output.pdf')