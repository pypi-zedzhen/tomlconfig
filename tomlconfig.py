import tomli
import tomli_w
from dictconfig import error, BaseDictConfig


__all__ = ['TomlConfig']


class TomlConfig(BaseDictConfig):
    def __init__(self, filename, ):
        super().__init__(filename, read, write)


def read(filename):
    try:
        with open(filename, 'rb') as f:
            return tomli.load(f)
    except (OSError, tomli.TOMLDecodeError):
        raise error.ReadError


def write(filename, cfg):
    s = tomli_w.dumps(cfg, multiline_strings=True)
    try:
        tomli.loads(s)
    except tomli.TOMLDecodeError:
        raise error.WriteError

    try:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(s)
    except OSError:
        raise error.WriteError
