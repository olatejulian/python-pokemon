from uuid import UUID

from pydantic import BaseModel


class BattleId(BaseModel):
    value: UUID
