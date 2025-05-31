class CustomObject:
    def __init__(self, registery_name:str):
        self.registery_name:str = registery_name
    
    def __str__(self) -> str:
        return self.registery_name