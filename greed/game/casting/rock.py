from game.casting.actor import Actor


class Rock(Actor):
    """
    Rocks are items of significant DIS-interest. Avoid them at all costs!!!
    It should give a value of negative 1.

    Attr:
        __point (integer): A value assigned to the rock.
    """

    def __init__(self):
        super().__init__()
        self.__point = -1

    def get_point_value(self):
        """
        Assigns the rock's point value
        Returns:
            point (integer): -1
        """

        return self.__point

    def set_point_value(self, point):
        """
        Updates the colloid value to a given one.
        Args:
            point (integer): The given colloid value.
        """

        self.__point = point