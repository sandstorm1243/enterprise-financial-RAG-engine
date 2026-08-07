
import os
# pyrefly: ignore [missing-import]
from dotenv import load_dotenv
# pyrefly: ignore [missing-import]
from qdrant_client import QdrantClient

# Load environment variables from .env file
load_dotenv()

qdrant_client = QdrantClient(
    url=os.getenv("CLUSTER_URL"), 
    api_key=os.getenv("QDRANT_API_KEY"),
)

print(qdrant_client.get_collections())
