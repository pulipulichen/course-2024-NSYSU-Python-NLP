""""
執行NER分析
"""

# Perform NER on text_list and store the result in the ner variable.
ner = ner_driver(text_list)

# Show results.
for sentence, sentence_ner in zip(text_list, ner):
   print(sentence)
   for entity in sentence_ner:
      print(entity)