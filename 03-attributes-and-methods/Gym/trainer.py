class Trainer:
    tr_id = 1

    def __init__(self, name: str):
        self.name = name
        self.id = Trainer.tr_id
        Trainer.tr_id += 1

    def __repr__(self):
        return f"Trainer <{self.id}> {self.name}"

    @staticmethod
    def get_next_id():
        return Trainer.tr_id
