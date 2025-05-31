from utils.bukkit_material import BukkitMaterial
from utils.misc import Enchantment
from utils.custom_recipe import CustomRecipe
from utils.base_classes import CustomObject

class Blank:
    def __init__(self) -> None:
        pass
    
class CustomItem(CustomObject):
    __slots__ = ["display_name", "registery_name", "lore", "material", "enchantments","custom_recipe"]

    def __init__(
        self,
        display_name: str,
        registery_name: str,
        lore: str,
        material: BukkitMaterial,
        enchantments:list[Enchantment] = []
    ):
        super().__init__(registery_name)
        self.display_name: str = display_name
        self.lore: str = lore
        self.material: BukkitMaterial = material

    def __list__(self) -> list[str]:
        return [
            self.display_name,
            self.registery_name,
            self.lore,
            str(self.material),
        ]

    def get_registery_nbt(self) -> str:
        return "{CustomItem:%s}" % self.registery_name
    
    def set_recipe(self, recipe: CustomRecipe) -> None:
        if recipe.result != self:
            raise ValueError("The recipe result must be the same as the item.")
        self.custom_recipe = recipe