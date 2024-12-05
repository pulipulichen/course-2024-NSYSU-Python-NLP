""""
準備前處理工具
"""

# Install `opencc` package.
# Package detail: https://pypi.org/project/OpenCC/
!pip install opencc==1.1.9

# Import OpenCC package for conversion.
import opencc

# Remote symbols and convert Traditional Chinese text to Simplified Chinese.
def preprocess_text(text: str) -> str:
    
    # Remove special symbols.
    text = re.sub(r"[^\u4e00-\u9fff\d.a-zA-Z%+\-。！？，、；：（）【】《》“”‘’]", '', text)

    # Initialize OpenCC converter.
    converter = opencc.OpenCC('t2s')  # 't2s' stands for Traditional to Simplified

    # Convert the text to Simplified Chinese.  
    result = converter.convert(text)

    # Returns a string.
    return result

