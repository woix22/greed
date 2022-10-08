class Score():
    """The score is the ammount of points made by the player

    Attributes:
        _score (int): The score to display
        
    """
    def __init__(self):
        self._score = 0

    def add_points(self, points):
        """Add the given points to the score.
        
        Args:
            points (int): The given points.
        """
        self._score += points

    def sub_points(self, points):
        """Substract the given points to the score.
        
        Args:
            points (int): The given points.
        """
        self._score -= points

    def get_score(self):
        """Gets the actual score.
        
        Returns:
            int: The actual score.
        """ 
        return self._score

