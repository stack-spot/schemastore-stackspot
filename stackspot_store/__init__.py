from enum import Enum
from pathlib import Path


class TypeEnum(Enum) :
    APP = "app"
    INFRA = "infra"

def get_template(type_enum: TypeEnum, schema_version: str = "v1", locale: str = "en_US"):
        return Path(__file__).parent / "templates" / "plugin" / schema_version / locale / type_enum.value
            

    
