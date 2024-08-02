from pydantic import BaseModel, ConfigDict

from english_ipa.model.region import Region


class IPA(BaseModel):
    model_config = ConfigDict(use_enum_values=True)
    region: Region
    ipas: list[str]
