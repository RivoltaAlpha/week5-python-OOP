import sys
sys.stdout.reconfigure(encoding='utf-8') ## this helped print emojis in the terminal

# Base Class
class AnimeCharacter:
    def use_power(self):
        raise NotImplementedError("Subclasses must implement this method.")
    

# sub classes of AnimeCharacter
# Each subclass represents a different anime character with their own unique power
class Naruto(AnimeCharacter):
    def use_power(self):
        return "Naruto uses Shadow Clone Jutsu as his special Jutsu! 🍜👥"

class Gojo(AnimeCharacter):
    def use_power(self):
        return "Gojo uses Infinite Domain and unleashes a powerful attack! �✨"

class Luffy(AnimeCharacter):
    def use_power(self):
        return "Luffy stretches his arm and hits with Gomu Gomu no Pistol while advocating for freedom and chasing his dream of being Pirate King! 🥊🧡"


class Deku(AnimeCharacter):
    def use_power(self):
        return "Deku unleashes One For All and charges at full speed! 💚⚡"

class Tanjiro(AnimeCharacter):
    def use_power(self):
        return "Tanjiro performs Water Breathing: Tenth Form while protecting his friends! 🌊🗡️"


def activate_power(character: AnimeCharacter):
    print(character.use_power())


# Example usage
characters = [Naruto(), Gojo(), Luffy(), Tanjiro()]

for hero in characters:
    activate_power(hero)


