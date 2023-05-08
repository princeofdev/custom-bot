# Import necessary packages
from llama_index import GPTSimpleVectorIndex, Document, SimpleDirectoryReader
import os

os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY')

# Loading from a directory
documents = SimpleDirectoryReader('./').load_data()

# Loading from strings, assuming you saved your data to strings text1, text2, ...
text_list = [text1, text2, ...]
documents = [Document(t) for t in text_list]

# Construct a simple vector index
index = GPTSimpleVectorIndex(documents)

# Save your index to a index.json file
index.save_to_disk('index.json')
# Load the index from your saved index.json file
index = GPTSimpleVectorIndex.load_from_disk('index.json')

# Querying the index
response = index.query("What features do users want to see in the app?")
print(response)