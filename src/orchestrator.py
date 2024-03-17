import subprocess
from commands import ScriptCommand


# === ORCHESTRATOR ===
class ScriptOrchestrator:
    def __init__(self, script_registry):
        self.script_registry = script_registry
        self.last_output = None

    def execute_series(self, script_name, args, restart_from=None):
        script = self.script_registry.get(script_name)
        if not script:
            raise ValueError(f"Script '{script_name}' not found in registry")

        if restart_from:
            # Validate restart_from
            if restart_from not in script.dependencies:
                raise ValueError(f"Invalid restart point '{restart_from}' for script '{script_name}'")
                    
        command_obj = ScriptCommand(script.command, output_handler=script.output_handler)  # Create ScriptCommand

        try:
            output = command_obj.execute(args, self.last_output)
            self.last_output = output
            print(f"Script '{script_name}' (restart_from: {restart_from}) completed successfully.")
            print(f"Output: {self.last_output}")

            # Execute dependencies after successful execution
            for dep in script.dependencies.get(restart_from, []):
                self.execute_series(dep, args, restart_from=dep)  # Pass restart point

        except subprocess.CalledProcessError as e:
            print(f"Script '{script_name}' failed (restart_from: {restart_from}):")
            print(f"Error: {e.stderr}")