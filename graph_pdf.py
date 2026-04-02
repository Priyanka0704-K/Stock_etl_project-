import matplotlib.pyplot as plt
import pandas as pd
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader

# Load CSV
df = pd.read_csv("data/aapl_stock_data.csv")

# Plot graph
plt.figure(figsize=(10,5))
plt.plot(df["Date"], df["Close"], marker='o', color='blue')
plt.title("AAPL Last 5 Days Close Price")
plt.xlabel("Date")
plt.ylabel("Close Price ($)")
plt.grid(True)
plt.tight_layout()
graph_image = "aapl_stock_trend.png"
plt.savefig(graph_image)
plt.close()

# Create PDF
pdf_file = "aapl_stock_graph.pdf"
c = canvas.Canvas(pdf_file, pagesize=letter)
width, height = letter
c.setFont("Helvetica-Bold", 16)
c.drawCentredString(width/2, height-50, "AAPL Stock Trend")
img = ImageReader(graph_image)
c.drawImage(img, 50, height/2 - 100, width=500, height=300)
c.showPage()
c.save()
print("PDF Created:", pdf_file)
