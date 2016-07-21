class Point(object):
    """
    creates an n-dimensional point object. The dimension is determined by
    how many arguments beyond the id are given to the object instantiation.

    Examples:
    >>> x = Point(19, 4, 3)
    >>> x.point_id
    19
    >>> x.coordinates
    (4, 3)
    >>> print(x)
    <id: 19 (4,3)>
    """

    def __init__(self, shape_id, *args):
        self.__id = shape_id
        self.__data = args

    def dimension(self):
        """returns the dimension of the point"""
        return len(self.__data)

    @property
    def coordinates(self):
        """returns the values of the coordinates for the point"""
        return tuple(value for value in self.__data)

    @property
    def point_id(self):
        """returns the id of the point"""
        return self.__id

    def __str__(self):
        """pretty print for this class"""
        coord = [str(x) for x in self.__data]
        point_id = str(self.__id)
        return "<" + "id: " + point_id + " (" + ",".join(coord) + ")" + ">"
