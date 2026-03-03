class Trainer:
    def __init__(
        self,
        trainer_id: TrainerId,
        name: TrainerName,
        team: tuple[Pokemon, ...],
        money: Money,
        badges: tuple[Badge, ...],
    ):
        self.__trainer_id = trainer_id
        self.__name = name
        self.__team = team
        self.__money = money
        self.__badges = badges
