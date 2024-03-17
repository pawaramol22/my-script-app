import shlex
import subprocess
from exceptions import ScriptExecutionError


# === COMMAND PATTERN ===
class ScriptCommand:
    def __init__(self, command, output_handler=None, user=None):
        self.command = command
        self.output_handler = output_handler
        self.user = user

    def execute(self, args, last_output): 
        if self.user:
            command = shlex.split(f"sudo -u {self.user} {self.command.format(args=args, last_output=last_output)}")
        else:
            command = shlex.split(self.command.format(args=args, last_output=last_output))

        try:
            process = subprocess.run(command, capture_output=True, check=True, text=True)
            output = process.stdout.strip()

            if self.output_handler:
                output = self.output_handler(output)

            return output
        except subprocess.CalledProcessError as e:
            raise ScriptExecutionError(f"Script failed: {e.stderr}") from e