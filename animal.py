class Animal:
    """
    A class used to represent an Animal

    ...

    Attributes
    ----------
    name : str
        the name of the animal
    representation : ascii str
        An image of the animal in ascii art

    Methods
    -------
    """
    
    def __init__(self, name, representation):
        """
        Parameters
        ----------
        name : str
            The name of the animal
        representation : ascii str
            An image of the animal in ascii art
        """

        self.name = name
        self.representation = representation

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.representation
