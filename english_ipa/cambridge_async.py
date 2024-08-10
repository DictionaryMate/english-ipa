import aiohttp
from bs4 import BeautifulSoup

from english_ipa.model.word import Word
from english_ipa.utils import _get_ipa


class AsyncCambridgeDictScraper:
    def __init__(self):
        self.base_url = "https://dictionary.cambridge.org/dictionary/english/"
        self.header = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
            "Accept-Encoding": "gzip, deflate, br, zstd",
            "Accept-Language": "en-US,en;q=0.9",
        }

    async def _get_html(self, word: str):
        url = self.base_url + word
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=self.header) as response:
                if response.status == 200:
                    response_text = await response.text()
                    return BeautifulSoup(response_text, "html.parser")

                return None

    async def get_ipa(self, word: str):
        html = await self._get_html(word)
        if html is not None:
            return Word(word=word, ipas=_get_ipa(html))

        return Word(word=word, ipas=[])

    async def get_ipa_in_dict(self, word: str):
        ipa = await self.get_ipa(word)
        return ipa.model_dump()

    async def get_ipa_in_json(self, word: str):
        ipa = await self.get_ipa(word)
        return ipa.model_dump_json()

    async def get_ipa_in_str(self, word: str):
        ipa = await self.get_ipa(word)
        return ipa.model_dump_str()
