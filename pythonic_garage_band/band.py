
class Band:
    """
    create Band_List (Instances!)
    """
    instances = []

    def __init__(self, name=None, members=None):
        self.name = name
        self.members = members
        self.instances.append(self)
        # print(self.instances)

    def __str__(self):
        return f"The band {self.name}"

    def __repr__(self):
        return f"Band instance. name={self.name}, members={self.members}"

    def play_solos(self):
        solos = []
        for member in self.members:
            solos.append(member.play_solo())
        return solos
#         OR
#       return [member.play_solo() for member in self.members]

    @classmethod
    def to_list(cls):
        return cls.instances


class Musician:
    """
    Super class otherr classes(like Guitarist,Drumer,Bassist) inherit from...
    """

    def __init__(self, name, instrument):
        self.name = name
        self.instrument = instrument

    def __repr__(self):
        return f"{self.__class__.__name__} instance. Name = {self.name}"

    def __str__(self):
        return f"My name is {self.name} and I play {self.instrument}"


class Guitarist(Musician):
    """
    sub class Inherits from super class Musician
    """

    def __init__(self, name):
        super().__init__(name, "guitar")

    def get_instrument(self):
        return self.instrument

    def play_solo(self):
        return "face melting guitar solo"


class Bassist(Musician):
    """
    sub class Inherits from super class Musician
    """

    def __init__(self, name):
        super().__init__(name, "bass")

    def get_instrument(self):
        return "bass"

    def play_solo(self):
        return "bom bom buh bom"


class Drummer(Musician):
    """
    sub class Inherits from super class Musician
    """

    def __init__(self, name):
        super().__init__(name, "drums")

    def get_instrument(self):
        return "drums"

    def play_solo(self):
        return "rattle boom crash"
