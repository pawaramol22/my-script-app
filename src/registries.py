from myscript.registry import registry as myregistry


class CommandRegistryFactory:
    def get_series(self, registry_name):
        series_map = {
            "my": myregistry,
            # ... Add mappings for other series
        }

        try:
            return series_map[registry_name]()
        except KeyError:
            raise ValueError(f"Invalid command series: {registry_name}")