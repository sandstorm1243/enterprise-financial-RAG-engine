
from pathlib import Path
import asyncio
import os
# pyrefly: ignore [missing-import]
from dotenv import load_dotenv
# pyrefly: ignore [missing-import]
from llama_cloud import AsyncLlamaCloud

# Explicitly load .env from the server root
env_path = Path(__file__).resolve().parents[2] / ".env"
load_dotenv(dotenv_path=env_path)

client = AsyncLlamaCloud(api_key=os.getenv("LLAMA_API_KEY"))


async def main():
    file_obj = await client.files.create(
        file=r"D:\enterprise-financial-RAG-engine\server\data\PDF Solutions_Typeset Proxy_v2_Host.pdf",
        purpose="parse",
    )

    result = await client.parsing.parse(
        file_id=file_obj.id,
        tier="agentic",
        version="latest",
        expand=["markdown_full"],
    )

    print(result.markdown_full)


if __name__ == "__main__":
    asyncio.run(main())

#comment