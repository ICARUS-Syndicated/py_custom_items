from utils.bukkit_material import BukkitMaterial
from utils.custom_item import CustomItem, Blank
from utils.base_classes import CustomObject

class CustomRecipe(CustomObject):
    __slots__ = ["registery_name", "ingredients", "result", "is_shapeless"]
    def __init__(
        self,
        registery_name: str,
        ingredients: list[BukkitMaterial | CustomItem | Blank],
        result: BukkitMaterial | CustomItem,
        is_shapeless: bool = False,
    ):
        if len(ingredients) > 9:
            raise ValueError("The number of ingredients must be less than or equal to 9.")
        elif len(ingredients) < 9:
            for i in range(9 - len(ingredients)):
                ingredients.append(Blank())

        super().__init__(registery_name)
        self.ingredients: list[BukkitMaterial | CustomItem | Blank] = ingredients
        self.result: BukkitMaterial | CustomItem = result
        self.is_shapeless: bool = is_shapeless

    def __str__(self) -> str:
        return self.registery_name
    
    def __list__(self) -> list[str]:
        return [
            self.registery_name,
            str(self.ingredients),
            str(self.result),
            str(self.is_shapeless),
        ]
    
    def draw_pattern(self) -> list[str]:
        _:list[BukkitMaterial | CustomItem | Blank] = list(set(self.ingredients))
        pattern:str = ""
        for i in self.ingredients:
            if isinstance(i, Blank):
                pattern += " "
            elif isinstance(i, CustomItem):
                pattern += chr(ord('a') + _.index(i))
            elif isinstance(i, BukkitMaterial):
                pattern += chr(ord('a') + _.index(i))
        return [pattern[i:i+3] for i in range(0, len(pattern), 3)]