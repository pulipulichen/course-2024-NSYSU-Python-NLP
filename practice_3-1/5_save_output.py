"""
儲存SA結果到output.csv
"""

# Import the `pandas` package needed for creating tables.
import pandas as pd

# Create the DataFrame.
df = pd.DataFrame(result, columns=["text_idx", "predicted_sentiment", "probabilities"])

# Save the DataFrame to a CSV file.
df.to_csv("output.csv", index=False, encoding="utf-8")

