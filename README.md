# English IPA
a python package for getting the IPA of an given English word

## Usage
```python
from english_ipa.cambridge import CambridgeDictScraper

scraper = CambridgeDictScraper()
ipa_in_dict = scraper.get_ipa_in_dict("hello")
# returned value
# {'word': 'hello', 'ipas': [{'region': 'uk', 'ipas': ['/heˈləʊ/']}, {'region': 'us', 'ipas': ['/heˈloʊ/']}]}

ipa_in_json = scraper.get_ipa_in_json("hello")
# returned value
# {"word":"hello","ipas":[{"region":"uk","ipas":["/heˈləʊ/"]},{"region":"us","ipas":["/heˈloʊ/"]}]}
```