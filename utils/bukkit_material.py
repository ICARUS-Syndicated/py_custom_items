from atexit import register


class BukkitMaterial:
    """
    Represents a Bukkit material. \n
    Notice that the material name is not the same as the in-game registery name. \n
    For example, the in-game registery name for diamond sword is "diamond_sword", but the material name is "DIAMOND_SWORD". \n
    """
    __slots__ = ["registery_name"]

    def __init__(self, registery_name: str) -> None:
        if registery_name == "":
            raise ValueError("The registery name cannot be empty.")
        self.registery_name: str = registery_name

    def __str__(self) -> str:
        return self.registery_name.replace("_", " ").lower()
