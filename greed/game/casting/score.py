from game.casting.actor import Actor

class Score(Actor):
    """
    The responsibility of a Score is to update and display the user's score.

    Attributes:
        _points: The current user points.
    """
    def __init__(self):
        super().__init__()
        self._points = 0

    def get_points(self):
        """Returns the current score.
        
        Returns:
            int: The current score.
        """
        return self._points

    def add_points(self, points):
        """Updates and displays the points as the user plays.
        
        Args:
            points: The user points.
        """
        self._points += points
        self.set_text(f"Score: {self._points}")