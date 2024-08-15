# File: dadosinvalidoserror.py
class DadosInvalidosError(Exception):
    """Raised when the data provided is invalid."""
    def __init__(self, message, file_stream):
        message += "\n"
        super().__init__(message)
        file_stream.write(f'Error: {message}')

