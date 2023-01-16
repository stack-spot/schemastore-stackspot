import sys
from enum import Enum
from os import chmod
from pathlib import Path


class TypeEnum(Enum) :
    APP = "app"
    INFRA = "infra"

def get_template(type_enum: TypeEnum, schema_version: str = "v1"):
        if getattr(sys, "frozen", False):
            template_path = Path(sys._MEIPASS) / type_enum.value / schema_version
            if sys.platform != "win32":
                chmod(template_path / "templates" / "templates" / "README.md", 0o644)
                chmod(template_path / "templates" / f"plugin-{type_enum.value}.stk.yaml", 0o644)
        else:
            template_path = (
                Path(__file__).parent / type_enum.value / schema_version
            )
        return template_path

    
