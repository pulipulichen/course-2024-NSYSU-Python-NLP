""""
準備翻譯工具
"""

# Install Google Translator package `deep-translator` version 1.11.4.
# Package detail: https://pypi.org/project/deep-translator/
!pip install deep-translator==1.11.4

# Import GoogleTranslator from `deep-translator` package
from deep_translator import GoogleTranslator

# Defind the target language.
# Language code list: https://stackoverflow.com/questions/75826605/my-python-discord-bot-which-is-supposed-to-automatically-translate-messages-does
target_lang_code = 'zh-TW'