from game.casting.actor import Actor

class Artifact(Actor):
    """An artifact is an actor representing a gem or a rock. 
    
    The responsibility of the artifact is to add or substract points depending on whether it's a rock or a gem.

    Attributes:
        _type (string): The type to display
        
    """
    def __init__(self):
        self._type = ""

    def set_type(self, type):
        """Updates the type to the given one.
        
        Args:
            type (string): The given type.
        """
        self._type = type

    def get_type(self):
        """Gets the artifact's type.
        
        Returns:
            string: The artifact's type.
        """ 
        return self._type