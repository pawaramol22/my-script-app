import argparse

from orchestrator import ScriptOrchestrator
from registries import CommandRegistryFactory
from myscript.registry import script_registry


if __name__ == "__main__":
    # Command-line argument parsing
    parser = argparse.ArgumentParser(description="Script Orchestrator")
    parser.add_argument("script_name", help="Name of the script to execute")
    parser.add_argument("args", nargs=argparse.REMAINDER, help="Arguments for the script")
    parser.add_argument("--restart_from", help="Restart from a specific point in the script", default=None)
    args = parser.parse_args()

    factory = CommandRegistryFactory()
    my_script_registry = factory.get_series(args.script_name)

    # Create script object
    script_orchestrator = ScriptOrchestrator(my_script_registry)

    # Execute series of scripts
    script_orchestrator.execute_series(args.script_name, args.args, restart_from=args.restart_from)
