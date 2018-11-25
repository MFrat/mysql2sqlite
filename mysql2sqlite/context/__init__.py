import copy

from config import get_cluster_name, get_config


class Context:
    _cache_by_env = {}

    @classmethod
    def _create(cls, env):
        try:
            context = Context(env)

            return context

        except (AttributeError, KeyError) as err:
            pass

    @classmethod
    def clone(cls, env):
        if env not in cls._cache_by_env:
            cls._cache_by_env[env] = cls._create(env)

        return copy.deepcopy(cls._cache_by_env[env])

    def __init__(self, env):
        self.env = env
        self.cluster = get_cluster_name(env)

        self._settings = get_config(env)

        self.database_host = self._get_setting("DATABASE_HOST")
        self.database_port = self._get_setting("DATABASE_PORT")
        self.database_name = self._get_setting("DATABASE_NAME")
        self.database_username = self._get_setting("DATABASE_USERNAME")
        self.database_password = self._get_setting("DATABASE_PASSWORD")

        self.ignored_tables = self._get_setting("IGNORED_TABLES")
        self.ignored_inserts = self._get_setting("IGNORED_INSERTS")

        self.outputname = self._get_setting("SQLITE_OUTPUT_NAME")

        self.external_tables_script = self._get_setting("OUTER_TABLES_SCRIPT")
        self.custom_select_file = self._get_setting("CUSTOM_SELECT_FILE")

    def _get_setting(self, attribute, cast_function=None):
        result = self._settings.get(attribute)
        if result is None:
            return None
        if str(result).lower() == "none":
            return None
        if cast_function is not None:
            return cast_function(result)
        return result

