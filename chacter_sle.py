class aj:
    def __init__(self):
        self.health = 10
        self.strength = 0
        #regen health 
        self.ability = 0 
        
    def print_stats(self):
        # stats_str = ""
        # stats_str += "Health: " + str(self.health) + "\n"
        # stats_str += "Strength: " + str(self.strength) + "\n"
        # stats_str += "Ability: " + str(self.ability) + "\n"
        # return stats_str

        return """
            Health: %i
            Strength: %i
            Ability: %i
        """ %(self.health, self.strength, self.ability)

class sam:
    def __init__(self):
        self.health = 10
        self.strength = 0
        #res
        self.ability = 0

    def print_stat(self):
        stats_strr =  ""
        stats_strr += "Health: " + str(self.health) + "\n"
        stats_strr += "Strength: " + str(self.strength) + "\n"
        stats_strr += "Ability: " + str(self.ability) + "\n"
        return stats_strr
