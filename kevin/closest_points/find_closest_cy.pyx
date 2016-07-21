"""This module is the python implemntation of find closes points"""

import math


def find_closest_points(all_points):
    """
       This method goes through the list of points given to it and finds
       the two closest ones. 
    """
    cdef distance, min_distance, x1, x2, y1, y2
    min_distance = 10000000
    point1 = "" 
    point2 = ""
    for oindex, opoint in enumerate(all_points):
        x1, y1 = opoint.latitude, opoint.longitude
        for iindex, ipoint in enumerate(all_points):
            x2, y2 = ipoint.latitude, ipoint.longitude
            if iindex <= oindex:
                continue
            else:
                distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
                if distance < min_distance:
                    point1, point2 = ipoint.point_id, opoint.point_id
                    min_distance = distance

    return point1, point2, min_distance
