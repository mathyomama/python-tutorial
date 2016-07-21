"""This module reads an OpenMap xml file and plots it"""
from lxml import etree
import find_closest_py
import find_closest_cy
import time

class Point(object):
    """
       Class that stores point latitude and longitude
    """
    def __init__(self, *args):
        """Initializes the Point object
        Args:
            *args: The latitude and longitude of the point
        Returns:
            None
        >>> p = Point(1,2)
        >>> p.latitude == 1
        True
        >>> p.longitude == 2
        True
        """
        self.__lat, self.__lon = args

    @property
    def latitude(self):
        """
           Getter method for attribute latitude
        """
        return self.__lat

    @property
    def longitude(self):
        """
          Getter method for attribute longitude
        """
        return self.__lon


class IdPoint(Point):
    """
       Class that stores point id
    """
    def __init__(self, pointid, lat, lon):
        """Initializes the idPoint object
        Args:
            *args: The id, latitude and longitude of the point
        Returns:
            None
        >>> p = IdPoint("100",1,2)
        >>> p.point_id == "100"
        True
        """
        self.__pointid = pointid
        super(IdPoint, self).__init__(lat, lon)

    @property
    def point_id(self):
        """
          Getter method for attribute id
        """
        return self.__pointid


if __name__ == "__main__":
    DOC = etree.parse("map.osm")

    ALL_POINTS = tuple(IdPoint(elem.get("id"), float(elem.get("lat")),
                               float(elem.get("lon"))) for elem in DOC.xpath("/osm/node"))

    start = time.time()
    p1_id, p2_id, min_dist = find_closest_py.find_closest_points(ALL_POINTS)
    end = time.time()
    print("\n In python")
    print(" Point 1", p1_id, "\n", "Point 2", p2_id, "\n", "Minimum Distance", min_dist, "Time", end - start)

    start = time.time()
    p1_id, p2_id, min_dist = find_closest_cy.find_closest_points(ALL_POINTS)
    end = time.time()
    print("\n In cython")
    print(" Point 1", p1_id, "\n", "Point 2", p2_id, "\n", "Minimum Distance", min_dist, "Time", end - start)
