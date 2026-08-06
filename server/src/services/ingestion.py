from llama_cloud import AsyncLlamaCloud

import os
from dotenv import load_dotenv
load_dotenv()


client = AsyncLlamaCloud(api_key=os.getenv("LLAMA_API_KEY"))

file_obj = await client.files.create(file="D:\enterprise-financial-RAG-engine\server\data\PDF Solutions_Typeset Proxy_v2_Host.pdf", purpose="parse")

result = await client.parsing.parse(
    file_id=file_obj.id,
    tier="agentic",
    expand=["markdown_full"],
)

print(result.markdown_full)
print(result.markdown_full)