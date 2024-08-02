from pydantic import BaseModel

from english_ipa.model.IPA import IPA


class Word(BaseModel):
    word: str
    ipas: list[IPA]
