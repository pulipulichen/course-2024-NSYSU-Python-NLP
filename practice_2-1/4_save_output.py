"""
儲存NER結果到output.csv
"""

# Import the pandas package needed for creating tables.
import pandas as pd

# Create an empty list to store the data.
data = []

# Iterate through sentences and entities.
for sentence_idx, (sentence, sentence_ner) in enumerate(zip(text_list, ner)):
  for entity in sentence_ner:
    word = entity.word
    ner_tag = entity.ner
    start_idx = entity.idx[0]
    end_idx = entity.idx[1]

    # Append the data for each entity to the list
    data.append([sentence_idx, word, ner_tag, start_idx, end_idx])


# Create the DataFrame.
df = pd.DataFrame(data, columns=["text_idx", "word", "ner", "idx_start", "idx_end"])

# Save the DataFrame to a CSV file.
df.to_csv("output.csv", index=False, encoding="utf-8")

