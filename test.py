import asyncio

from english_ipa.cambridge_async import AsyncCambridgeDictScraper


async def main():
    scraper = AsyncCambridgeDictScraper()
    ipa_in_dict = await scraper.get_ipa_in_dict("apple")
    print(ipa_in_dict)


asyncio.run(main())
