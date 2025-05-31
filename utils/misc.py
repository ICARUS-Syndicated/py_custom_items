from enum import Enum


class BukkitColor(Enum):
    BLACK = "black"
    DARK_BLUE = "dark_blue"
    DARK_GREEN = "dark_green"
    DARK_AQUA = "dark_aqua"
    DARK_RED = "dark_red"
    DARK_PURPLE = "dark_purple"
    GOLD = "gold"
    GRAY = "gray"
    DARK_GRAY = "dark_gray"
    BLUE = "blue"
    GREEN = "green"
    AQUA = "aqua"
    RED = "red"
    LIGHT_PURPLE = "light_purple"
    YELLOW = "yellow"
    WHITE = "white"
    RESET = "reset"

class Enchantment:
    def __init__(self,registery_name:str,level:int) -> None:
        self.registery_name:str = registery_name
        self.level:int = level

    def __str__(self) -> str:
        return f"{self.registery_name}:{self.level}"