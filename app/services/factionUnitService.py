from prisma import Prisma
from ..models.factionUnitDTO import FactionUnitDTO, FactionUnitUpdateDTO, FactionUnitCreateDTO
from typing import List

class FactionUnitService:
    def __init__(self, database):
        self.database = database

    async def get_all(self) -> List[FactionUnitDTO]:
        return await self.database.factionunitspecialization.find_many()

    async def get_by_id(self, id: str) -> FactionUnitDTO:
        return await self.database.factionunitspecialization.find_unique( 
            where={"id": id} 
        )

    async def create(self, faction: FactionUnitCreateDTO) -> FactionUnitDTO:
        data = faction.dict() if isinstance(faction, FactionUnitCreateDTO) else faction

        return await self.database.factionunitspecialization.create( 
            data=data
        )

    async def delete(self, id: str) -> FactionUnitDTO:
        return await self.database.factionunitspecialization.delete(
            where={"id": id}
        )
    
    async def delete_by_ids(self, faction_id: str, unit_specialization_id: str) -> FactionUnitDTO:
        faction_unit = await self.database.factionunitspecialization.find_first(
            where={"faction_id": faction_id, "unit_specialization_id": unit_specialization_id}
        )

        if(faction_unit):
            return await self.database.factionunitspecialization.delete(
                where={"id": faction_unit.id}
            )