from llama_cloud import AsyncLlamaCloud

client = AsyncLlamaCloud(api_key="<your-api-key>")

file_obj = await client.files.create(file="./my_document.pdf", purpose="parse")

result = await client.parsing.parse(
    file_id=file_obj.id,
    tier="agentic",
    expand=["markdown_full"],
)

print(result.markdown_full)