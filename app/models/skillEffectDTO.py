from pydantic import BaseModel
from typing import Optional

class SkillEffectBaseDTO(BaseModel):
    skill_id: str
    effect_id: str
    duration: str
    conditions: Optional[str]

class SkillEffectCreateDTO(SkillEffectBaseDTO):
    pass

class SkillEffectUpdateDTO(SkillEffectBaseDTO):
    skill_id: Optional[str]
    effect_id: Optional[str]
    duration: Optional[str] = None
    conditions: Optional[str] = None

class SkillEffectDTO(SkillEffectBaseDTO):
    id: int
    created_at: str
    updated_at: str
    class Config:
        orm_mode = True