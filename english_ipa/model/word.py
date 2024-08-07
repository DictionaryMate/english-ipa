from pydantic import BaseModel

from english_ipa.model.IPA import IPA


class Word(BaseModel):
    word: str
    ipas: list[IPA]

    def model_dump_str(self) -> str:
        # region.value: ipas;
        return "; ".join([f"{ipa.region}: {ipa.ipas}" for ipa in self.ipas])
