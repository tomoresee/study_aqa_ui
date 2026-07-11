import yaml

DEFAULT_CONFIG_PATH = "utils/config.yaml"


class ConfigReader:
    _instances = {}

    def __new__(cls, file_path=DEFAULT_CONFIG_PATH):
        if file_path not in cls._instances:
            instance = super().__new__(cls)

            with open(file_path, "r") as file:
                instance.config = yaml.safe_load(file)

            cls._instances[file_path] = instance

        return cls._instances[file_path]

    @classmethod
    def get(cls, key, file_path=DEFAULT_CONFIG_PATH):
        instance = cls(file_path)

        value = instance.config
        for item in key.split("."):
            value = value[item]

        return value
