from iconservice import *

TAG = 'Apple'

class Apple(IconScoreBase):

    def __init__(self, db: IconScoreDatabase) -> None:
        super().__init__(db)
        self.Apple = DictDB('Apple', db, str)

    def on_install(self) -> None:
        super().on_install()

    def on_update(self) -> None:
        super().on_update()

    @external
    def enroll(self, Apple: str):
        self.Apple[self.msg.sender] = Apple

    @external(readonly=True)
    def Apple(self) -> str:
        return self.Apple[self.msg.sender]
