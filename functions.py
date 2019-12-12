import random

class Pet:
    texture = ["Fluffy", "Slimey", "Rubbery", "Slippery", "Smooth", "Hairy","Gritty"]
    smell = ["Citrusy, like a peeled orange",
             "Warm, like cinnamon",
             "Like rain and wet asphalt",
             "Like coffee",
             "Floral",
             "Musty",
             "Fishy"]
    fun_fact = ["Careful, this boy Bites... unless you're looking to lose a few fingers...",
                "This little buddy is looking for some love... and a place to molt",
                "This little girl eats anything! And when we say anything, we mean anything."]
    
    def __init__(self):
        self.texture = random.choice(self.__class__.texture)
        self.smell = random.choice(self.__class__.smell)
        self.fun_fact = random.choice(self.__class__.fun_fact)
        return
    
    def get_fun_fact(self):
        """
        This is a function that returns your pet's random fun_fact
        """
        return self.fun_fact

    def get_smell(self):
        """
        This is a function that returns your pet's random smell
        """
        return self.smell

    def get_texture(self):
        """
        This is a function that returns your pet's random texture
        """
        return self.texture

    def get_pet_info(self):
        """
        This is a function that informs you of your pet's info such as: fun fact, smell, and texture
        """ 
        print("Texture: " + self.texture)
        print("Smell: " + self.smell)
        print("Fun Fact: " + self.fun_fact )