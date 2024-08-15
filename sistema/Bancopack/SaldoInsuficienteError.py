# File: saldoinsuficienteerror.py
class SaldoInsuficienteError(Exception):
    """Raised when there is insufficient balance for a transaction."""
    def __init__(self, message, file_stream):
        message += "\n"
        super().__init__(message)
        file_stream.write(f'Error: {message}')
