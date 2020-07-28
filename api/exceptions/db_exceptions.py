class ModelInstanceAlreadyExist(Exception):
    def __init__(self, message="User already exist!"):
        super().__init__(message)