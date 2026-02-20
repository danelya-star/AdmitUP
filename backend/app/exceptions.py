class BaseAppException(Exception):
    """Base exception for the application"""
    pass

class UserAlreadyExistsException(BaseAppException):
    def __init__(self, name: str):
        self.name = name
        super().__init__(f"User with name '{name}' already exists")

class DatabaseConnectionException(BaseAppException):
    def __init__(self, detail: str):
        self.detail = detail
        super().__init__(f"Database error: {detail}")