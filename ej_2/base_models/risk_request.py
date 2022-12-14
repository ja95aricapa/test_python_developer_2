from pydantic import BaseModel, Field

from ej_2.enums.risk_enum import RiskEnum


# fix: import all required modules
class RiskRequest(BaseModel):
    user_id: int = Field(gt=-1)
    product_name: RiskEnum = Field()
    input_data: dict
