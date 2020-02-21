from pathlib import Path
import json
import logging


class Config(object):
    def __init__(self, config_dict, flask_config_values=None):
        self.config = config_dict
        for k, v in self.config.items():
            setattr(self, k, v)

        if isinstance(flask_config_values, dict):
            for k, v in flask_config_values.items():
                setattr(self, k, v)

        self._verify_fields()

    @classmethod
    def from_file(cls, config_path, flask_config_values=None):
        with open(Path(config_path)) as fp:
            config = json.load(fp)
        return cls(config_dict=config, flask_config_values=flask_config_values)

    @classmethod
    def from_string(cls, string, flask_config_values=None):
        config = json.loads(string)
        return cls(config_dict=config, flask_config_values=flask_config_values)

    @property
    def required_fields(self):
        return {
            "api_url",
            "db_username",
            "db_password",
            "db_name",
            "db_port",
            "db_host",
            "api_tokens",
        }

    def _verify_fields(self):
        given_keys = set(self.config)
        extra_keys = given_keys - self.required_fields
        missing_keys = self.required_fields - given_keys
        if missing_keys:
            raise ValueError(f"The following configuration is missing key(s): {', '.join(missing_keys)}")
        if extra_keys:
            logger = logging.getLogger("{module_path}".format(module_path=__name__))
            logger.info("Configuration has non-required key(s): {keys}" "".format(keys=", ".join(extra_keys)))

    def __eq__(self, other):
        return isinstance(other, Config) and hash(self) == hash(other)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __str__(self):
        result = ""
        for v in self.required_fields:
            field_value = getattr(self, v)
            result += str(field_value)
        return result

    def __hash__(self):
        return hash(str(self))

    # needed for flask interface
    def __getitem__(self, item):
        return getattr(self, item)

    # needed for flask interface
    def get(self, item):
        try:
            return getattr(self, item)
        except AttributeError:
            return None

    def __setitem__(self, key, value):
        return setattr(self, key, value)
