class Missing(Exception):
    def __init__(self, msg: str, *args) -> None:
        super().__init__(*args)
        self.msg = msg


class Duplicate(Exception):
    def __init__(self, msg: str, *args) -> None:
        super().__init__(*args)
        self.msg = msg
