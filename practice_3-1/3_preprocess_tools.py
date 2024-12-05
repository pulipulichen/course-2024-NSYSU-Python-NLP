""""
準備前處理工具
"""

# Install Google Translator package `googletrans` version 3.1.0a0.
# Package detail: https://pypi.org/project/googletrans/
!pip install googletrans==3.1.0a0

# Import Google Translator package.
from googletrans import Translator

# Initialize the translator object.
# translator = Translator(service_urls=['translate.google.com'])
translator = Translator()

# Defind the destination language.
# Language code list: https://cloud.google.com/translate/docs/languages
dest_lang_code = 'zh-cn'

# Remote symbols and convert Traditional Chinese text to Simplified Chinese.
def preprocess_text(text: str) -> str:
    
    # Remove special symbols.
    text = re.sub(r"[^\u4e00-\u9fff\d.a-zA-Z%+\-。！？，、；：（）【】《》“”‘’]", '', text)

    # Translate input_string to language code
    # Language code list: https://cloud.google.com/translate/docs/languages
    output_result = translator.translate(text, dest=dest_lang_code)

    # Get the text of the result of translation
    output_string = output_result.text

    # Returns a string.
    return output_string

