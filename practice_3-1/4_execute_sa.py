""""
執行SA分析
"""

# Declare an empty list for storing the result
result = []

# PProcess each `text`` string within the `text_list`.
for text_idx, text in enumerate(text_list):

   # Remote symbols and convert Traditional Chinese text to Simplified Chinese
   preprocessed_text = preprocess_text(text)

   # Conduct the sentiment pretiction of the text.
   probabilities, prediction = predict_sentiment(preprocessed_text)

   # Convert the sentiment prediction index to the label.
   predicted_sentiment = sentiment_labels[prediction]

   # Display the sentiment prediction result of the text.
   print(f"Text: {text}")
   print(f"Preprocessed text: {preprocessed_text}")
   print(f"Predicted sentiment: {predicted_sentiment}")
   print(f"Probability: {probabilities[0][prediction].item()}")

   # Store the result in the `result` list.
   result.append([text_idx, predicted_sentiment, probabilities[0][prediction].item()])