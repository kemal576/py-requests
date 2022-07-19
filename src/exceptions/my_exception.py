class MyException(Exception):
    def __init__(self, status: int):
        self.status = status
