from typing import Union

import requests
from bs4 import BeautifulSoup

from english_ipa.model.word import Word
from english_ipa.utils import _get_ipa


class CambridgeDictScraper:
    def __init__(self):
        self.base_url = "https://dictionary.cambridge.org/dictionary/english/"
        self.header = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
            "Accept-Encoding": "gzip, deflate, br, zstd",
            "Accept-Language": "en-US,en;q=0.9",
        }

    def get_ipa(self, word: str) -> Word:
        html = self._get_html(word)
        if html is not None:
            return Word(word=word, ipas=_get_ipa(html))

        return Word(word=word, ipas=[])

    def get_ipa_in_dict(self, word: str) -> dict:
        ipa = self.get_ipa(word)
        return ipa.model_dump()

    def get_ipa_in_json(self, word: str) -> str:
        ipa = self.get_ipa(word)
        return ipa.model_dump_json()

    def get_ipa_in_str(self, word: str) -> str:
        ipa = self.get_ipa(word)
        return ipa.model_dump_str()

    def _get_html(self, word: str) -> Union[BeautifulSoup, None]:
        url = self.base_url + word
        req = requests.get(url, headers=self.header)
        if req.status_code == 200:
            soup = BeautifulSoup(req.text, "html.parser")
            return soup

        return None
