class FileReader:
    \class CustomException(Exception):
    def __init__(self, message="This is a custom exception."):
        self.message = message
        super().__init__(self.message)

class CustomExceptionHandler:
    def handle_exception(self, value):
        if value < 0:
            raise CustomException("Negative values are not allowed.")

# Example usage:
exception_handler = CustomExceptionHandler()

try:
    exception_handler.handle_exception(-5)
except CustomException as ce:
    print(f"CustomException: {ce}")
