""""
執行NER分析
"""

# Perform NER on text_array and store the result in the ner variable.
ner = ner_driver(text_array)

# Show results.
for sentence, sentence_ner in zip(text_array, ner):
   print(sentence)
   for entity in sentence_ner:
      print(entity)