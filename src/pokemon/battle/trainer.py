from .pokemon import Pokemon
from .value_objects.trainer_id import TrainerId


class Trainer:
    def __init__(self, trainer_id: TrainerId, team: tuple[Pokemon, ...]):
        self.__trainer_id = trainer_id
        self.__team = team
