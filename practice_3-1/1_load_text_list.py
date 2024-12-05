"""
讀取text_list
"""

# Import the `pandas` package needed for loading CSV.
import pandas as pd

# Read the text_list from a CSV file
df_text = pd.read_csv('text_list.csv', encoding='utf-8')

# Convert the DataFrame to a list of strings
text_list = df_text['title'].tolist()