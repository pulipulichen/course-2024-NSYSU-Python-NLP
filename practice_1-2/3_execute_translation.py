# 執行翻譯

# Translate input_string to language code
# Language code list: https://cloud.google.com/translate/docs/languages
output_result = translator.translate(input_string, dest=dest_lang_code)

# Get the text of the result of translation
output_string = output_result.text

# Check the result of translation
output_string