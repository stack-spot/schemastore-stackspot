import sys
from enum import Enum
from os import chmod
from pathlib import Path


class TypeEnum(Enum) :
    APP = "app"
    INFRA = "infra"

def get_template(type_enum: TypeEnum, schema_version: str = "v1"):
        return Path(__file__).parent / type_enum.value / schema_version
            

    
