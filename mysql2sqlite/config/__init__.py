import yaml

from pkg_resources import resource_stream


def load(filename):
    with resource_stream(__name__, filename) as config_file:
        return yaml.load(config_file)


def load_cluster_config(name):
    return load('{0}.yml'.format(name))


_env = load('context.yml')
_configs = {}


def get_config(env):
    if env not in _configs:
        _configs[env] = load_cluster_config(get_cluster_name(env))
        _configs[env].update(_env[env].get("override", {}))
    return _configs[env]


def get_cluster_name(env):
    return _env[env]["cluster"]
