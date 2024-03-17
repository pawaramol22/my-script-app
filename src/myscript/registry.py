
from ..commands import ScriptCommand


# === Script registry ===
script_registry = {
    "script1": ScriptCommand(
        command="some_script1.sh {args} {last_output}",
        dependencies={},
        user='amol'
        output_handler=LogOutputHandler()  # Log output from script1
    ),
    "script2": ScriptCommand(
        command="some_script2.sh {args} {last_output}",
        dependencies={},
        user='root',
        output_handler=TransformOutputHandler()  # Transform output before script3
    ),
    "script3": ScriptCommand(
        command="some_script3.sh {args} {last_output}",
        dependencies={}
    ),
}