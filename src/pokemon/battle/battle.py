from .battle_state import BattleState
from .trainer import Trainer
from .value_objects.battle_id import BattleId


class Battle:
    def __init__(
        self,
        battle_id: BattleId,
        state: BattleState,
        trainers: tuple[Trainer, Trainer],
        seed: int,
    ):
        self.__battle_id = battle_id
        self.__state = state
        self.__trainers = trainers
