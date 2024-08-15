class ContaInexistenteError(Exception):
    def __init__(self, message, file_stream):
            message += "\n"
            super().__init__(message)
            file_stream.write(f'Error: {message}')