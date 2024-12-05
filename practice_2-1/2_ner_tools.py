""""
準備NER工具
"""

# Install `ckip-transformers` package.
# Package detail: https://pypi.org/project/ckip-transformers/
!pip install -U ckip-transformers==0.3.4

# Import `CkipNerChunker`
from ckip_transformers.nlp import CkipNerChunker

# Initialize NER driver.
ner_driver = CkipNerChunker(model="bert-base")