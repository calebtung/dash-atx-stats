import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
data = pd.read_csv('csv_uploads/data.csv')

# Create a bar chart
plt.figure(figsize=(8, 6))
plt.bar(data['Category'], data['Value'], color='skyblue')
plt.xlabel('Category')
plt.ylabel('Value')
plt.title('Bar Chart Example')

# Save the chart as a JPG
plt.savefig('static/assets/charts/bar_chart.jpg', format='jpg')
