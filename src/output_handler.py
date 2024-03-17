# === CHAIN OF RESPONSIBILITY ===
class OutputHandler:
    """Base class for output handlers"""
    def __init__(self, successor=None):
        self.successor = successor

    def handle(self, output):
        if self.successor:
            return self.successor.handle(output)
        return output  # No further handling

class LogOutputHandler(OutputHandler):
    def handle(self, output):
        print(f"Script output: {output}")  # Log the output
        return super().handle(output)

class TransformOutputHandler(OutputHandler):
    def handle(self, output):
        # Example: Transform the output for the next command
        transformed_output = output.upper()
        return super().handle(transformed_output)