import json
from pathlib import Path
from typing import Tuple, Sequence


def read_json(pathname: str) -> Tuple[Sequence[str], Sequence[Sequence[str]]]:
    """
    Read json file to extract people and couples defined as keys of a dictionary.
    """ 
    with open(pathname, 'r') as f:
        data = json.load(f)
    if 'people' not in data or 'couples' not in data:
        raise IncorrectFormatError
    return data['people'], data['couples']


class IncorrectFormatError(Exception):
    pass


class ExtensionNotSupportedError(Exception):
    pass


EXTENSION_MAP = {
    '.json': read_json
}


def read_data(pathname: Path) -> Tuple[Sequence[str], Sequence[Sequence[str]]]:
    """
    Read data depending on the extension of the file.
    """
    extension = Path(pathname).suffix
    if extension not in EXTENSION_MAP:
        raise ExtensionNotSupportedError

    return EXTENSION_MAP[extension](pathname)