from llama_cloud import AsyncLlamaCloud

import os
from dotenv import load_dotenv
load_dotenv()


client = AsyncLlamaCloud(api_key=os.getenv("LLAMA_API_KEY"))

file_obj = await client.files.create(file="./my_document.pdf", purpose="parse")

result = await client.parsing.parse(
    file_id=file_obj.id,
    tier="agentic",
    expand=["markdown_full"],
)

print(result.markdown_full)