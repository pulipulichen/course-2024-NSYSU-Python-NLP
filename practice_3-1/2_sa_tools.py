""""
準備SA工具
Source: https://huggingface.co/sanshizhang/Chinese-Sentiment-Analysis-Fund-Direction
"""

# Import packages
import sys
import re
import torch
from transformers import BertTokenizer, BertForSequenceClassification
from torch.nn.functional import softmax

# Configure to use CPU or CUDA.
device = 'cuda' if torch.cuda.is_available() else 'cpu'

# Load the pre-saved model and tokenizer.
model = BertForSequenceClassification.from_pretrained('sanshizhang/Chinese-Sentiment-Analysis-Fund-Direction')
tokenizer = BertTokenizer.from_pretrained('sanshizhang/Chinese-Sentiment-Analysis-Fund-Direction')

# Ensure the model is on the correct device.
model = model.to(device)

# Set the model to evaluation mode.
model.eval()

# Function definition: Predicts and returns the prediction probability.
def predict_sentiment(text):
    
    # Encoding text data.
    encoding = tokenizer.encode_plus(
        text,
        max_length=512,
        add_special_tokens=True,
        return_token_type_ids=False,
        padding='max_length',
        return_attention_mask=True,
        return_tensors='pt',
        truncation=True
    )

    # Retrieve the encoding corresponding to the input.
    input_ids = encoding['input_ids'].to(device)
    attention_mask = encoding['attention_mask'].to(device)

    # Computing without gradients
    with torch.no_grad():
      
      # Generate sentiment prediction logits
      outputs = model(input_ids=input_ids, attention_mask=attention_mask)

      # Convert logits to probabilities using softmax.
      probs = softmax(outputs.logits, dim=1)

    # Return probability and predicted category
    return probs, torch.argmax(probs, dim=1).cpu().numpy()[0]

# Define the labeds of sentiment pretictions.
sentiment_labels = {0: 'negative', 1: 'positive', 2: 'neutral'}