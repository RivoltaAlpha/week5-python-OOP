# Asssignment 1
# Base Class
class AnimeCharacter:
    def __init__(self, name, power, home):
        self.name = name
        self.power = power
        self.home = home

    def introduce(self):
        return f"I am {self.name} from {self.home} and I use {self.power}!"

    def use_power(self):
        return f"{self.name} uses their power: {self.power}!"
    
    def saveHome(self):
        return f"{self.name} is saving {self.home} using {self.power}!"

# Inherited Class
class SwordNinja(AnimeCharacter):
    def __init__(self, name, power, home, sword_power):
        super().__init__(name, power, home)
        self.sword_power = sword_power

    def use_power(self):
        return f"{self.name} takes off and flies at {self.sword_power} mph using {self.power} power!"

# Another Inherited Class
class Speed(AnimeCharacter):
    def __init__(self, name, power, home, speed_level):
        super().__init__(name, power, home)
        self.speed_level = speed_level

    def use_power(self):
        return f"{self.name} moves at lightning speed with {self.power} at speed level {self.speed_level}!"

# using the above classes
ninja = SwordNinja("Naruto", "Shadow Clone Jutsu", "Konoha", 100)
print(ninja.introduce())  # Outputs: I am Naruto from Konoha and I can Shadow Clone Jutsu!
print(ninja.use_power())  # Outputs: Naruto takes off and flies at 100 mph with Shadow Clone Jutsu power! 😂😂😂 not true though 
print(ninja.saveHome())  # Outputs: Naruto is saving Konoha using Shadow Clone Jutsu!

samurai = Speed("Sasuke", "Lightning Speed", "Konoha", 200)
print(samurai.introduce())  # Outputs: I am Sasuke from Konoha and I can Lightning Speed!
print(samurai.use_power())  # Outputs: Sasuke moves at lightning speed with Lightning Speed at speed level 200!
print(samurai.saveHome())  # Outputs: Sasuke is saving Konoha using Lightning Speed!
