from bs4 import BeautifulSoup

from english_ipa.model.IPA import IPA
from english_ipa.model.region import Region


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
                us_ipas.append(sibling.text) if is_in_us_ipa_list else uk_ipas.append(
                    sibling.text
                )
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
