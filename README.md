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

ipa_in_str = scraper.get_ipa_in_str("hello")
# returned value
# uk: ['/heˈləʊ/']; us: ['/heˈloʊ/']
```

### Async Version
```python
import asyncio

from english_ipa.cambridge_async import AsyncCambridgeDictScraper


async def main():
    scraper = AsyncCambridgeDictScraper()
    ipa_in_dict = await scraper.get_ipa_in_dict("apple")
    print(ipa_in_dict)


asyncio.run(main())

# printed value
# {'word': 'apple', 'ipas': [{'region': 'uk', 'ipas': ['/ˈæp.əl/']}, {'region': 'us', 'ipas': ['/ˈæp.əl/']}]}
```