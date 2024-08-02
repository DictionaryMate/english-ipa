from typing import Union

import requests
from bs4 import BeautifulSoup

from english_ipa.model.IPA import IPA
from english_ipa.model.region import Region
from english_ipa.model.word import Word


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
            return Word(word=word, ipas=CambridgeDictScraper._get_ipa(html))

        return Word(word=word, ipas=[])

    def get_ipa_in_dict(self, word: str) -> dict:
        ipa = self.get_ipa(word)
        return ipa.model_dump()

    def get_ipa_in_json(self, word: str) -> str:
        ipa = self.get_ipa(word)
        return ipa.model_dump_json()

    def _get_html(self, word: str) -> Union[BeautifulSoup, None]:
        url = self.base_url + word
        req = requests.get(url, headers=self.header)
        if req.status_code == 200:
            soup = BeautifulSoup(req.text, "html.parser")
            return soup

        return None

    @staticmethod
    def _get_ipa(html: BeautifulSoup) -> list[IPA]:
        ipa_html = html.find("span", {"class": f"{Region.UK.value} dpron-i"})
        if not ipa_html:
            return []

        uk_ipas = []
        us_ipas = []
        first_uk_ipa_ele = ipa_html.find("span", {"class": "pron dpron"})
        if first_uk_ipa_ele:
            uk_ipas.append(first_uk_ipa_ele.text)

        all_siblings = ipa_html.find_next_siblings()
        if len(all_siblings) > 0:
            is_in_us_ipa_list = False
            for sibling in all_siblings:
                if not sibling.has_attr("class"):
                    us_ipas.append(
                        sibling.text
                    ) if is_in_us_ipa_list else uk_ipas.append(sibling.text)
                else:
                    if sibling["class"][0] == f"{Region.US.value}":
                        is_in_us_ipa_list = True
                        first_us_ipa_ele = sibling.find("span", {"class": "pron dpron"})
                        if first_us_ipa_ele:
                            us_ipas.append(first_us_ipa_ele.text)

        ipa_result_list = [
            IPA(region=Region.UK, ipas=uk_ipas) if len(uk_ipas) > 0 else None,
            IPA(region=Region.US, ipas=us_ipas) if len(us_ipas) > 0 else None,
        ]

        return [ipa for ipa in ipa_result_list if ipa is not None]
