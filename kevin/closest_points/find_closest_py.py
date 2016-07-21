"""This module is the python implemntation of find closes points"""

import math


def find_closest_points(all_points):
    """
       This method goes through the list of points given to it and finds
       the two closest ones. 
    """
    min_distance = 10000000
    point1 = "" 
    point2 = ""
    for oindex, opoint in enumerate(all_points):
        for iindex, ipoint in enumerate(all_points):
            if iindex <= oindex:
                continue
            else:
                distance = math.sqrt((ipoint.latitude - opoint.latitude) ** 2 \
                         + (ipoint.longitude - opoint.longitude) ** 2)
                if distance < min_distance:
                    point1, point2 = ipoint.point_id, opoint.point_id
                    min_distance = distance

    return point1, point2, min_distance
