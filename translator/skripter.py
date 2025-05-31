from io import TextIOWrapper
from utils.bukkit_material import BukkitMaterial
from utils.misc import Enchantment
from utils.custom_item import CustomItem
from utils.custom_recipe import CustomRecipe

import json
import tomllib
import yaml

ACCEPTABLE_EXTENSIONS = ('.json', '.toml', '.yml', '.yaml')

def read_file(file: TextIOWrapper):
    """
    Reads a file and returns its content as a dictionary.
    Supports JSON, TOML, and YAML formats.
    """
    # TODO: 不知道要写什么
    pass