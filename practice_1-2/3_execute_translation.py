"""
執行翻譯
"""

# Translate input_string to language code
# Language code list: https://cloud.google.com/translate/docs/languages
output_string = GoogleTranslator(source='auto', target=dest_lang_code).translate(text=input_string)

# Check the result of translation
output_string