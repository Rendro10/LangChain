from sentence_transformers import SentenceTransformer
from dotenv import load_dotenv

load_dotenv()

sentences = ["This is an example sentence", "Each sentence is converted"]

model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
embeddings = model.encode(sentences)
print(embeddings)
