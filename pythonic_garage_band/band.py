class Band():
    
    instances=[] 

    def __init__(self, name, members):
        
        self.name = name 
        
        self.members = members
        
        Band.instances.append(self)
    
    def play_solos(self):
        solo_musican = []
        
        for x in self.members:
            solo_musican.append(x.play_solos())
        return solo_musican
    
    
    
    @classmethod
    def to_list(cls):
        return cls.instances
    
class Musician():
    """
    this class is a base class!
    """

    def __init__(self, name):
        self.name = name
    
    def play_solos(self):
        pass 
    
    def __str__(self):
        return f"My name is {self.name} and I play {self.get_instrument()}"

    def __repr__(self):
        return f"{self.__class__.__name__} instance. Name = {self.name}"

    def get_instrument(self):
        pass 

    def play_solo(self):
        return self.play_solos()


class Guitarist(Musician):
    """
    Guitar Class
    """
    def __init__(self, name):
        self.name = name
   
    
    def get_instrument(self):  
        return "guitar"

    def play_solos(self):  
        return "face melting guitar solo"

class Bassist(Musician):
    """
    Bass Class
    """
    def __init__(self,name):
        self.name=name
    
    
    
    def get_instrument(self): 
        return "bass"

    def play_solos(self): 
        return "bom bom buh bom"

class Drummer(Musician):
    """
    Drum Class
    """
    def __init__(self,name):
        self.name=name
    
    
    def get_instrument(self): 
        return "drums"
    
    def play_solos(self): 
        return "rattle boom crash"