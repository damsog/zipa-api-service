from pydantic import BaseModel
from typing import Optional

class SkillSummonBaseDTO(BaseModel):
    skill_id: str
    unit_id: str
    duration: Optional[str] = None
    conditions: Optional[str] = None

class SkillSummonCreateDTO(SkillSummonBaseDTO):
    pass

class SkillSummonUpdateDTO(SkillSummonBaseDTO):
    skill_id: Optional[str]
    unit_id: Optional[str]
    duration: Optional[str] = None
    conditions: Optional[str] = None

class SkillSummonDTO(SkillSummonBaseDTO):
    id: int
    created_at: str
    updated_at: str
    class Config:
        orm_mode = True