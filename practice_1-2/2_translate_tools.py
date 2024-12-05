""""
準備翻譯工具
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
dest_lang_code = 'zh-tw'