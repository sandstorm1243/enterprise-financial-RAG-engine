#ingestion.py
from server.src.services.ingestion import main
import asyncio
from . import ingestion


async def main():
    ingestion.main()

if __name__ == "__main__":
    asyncio.run(main())
