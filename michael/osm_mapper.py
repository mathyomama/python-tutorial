#!/usr/bin/env python3

"""
Script which prints all the nodes from a map.osm file which is in the current
directory.
"""

import lxml.etree

import shapes


def osm_get_nodes(filename):
    """
    function for parsing the given xml file and returning a list of nodes from
    the file. Each node is stored as a Point object.
    """
    doc = lxml.etree.parse(filename)
    points = list()
    for elem in doc.xpath("//node"):
        point_id = elem.get("id")
        lat = elem.get("lat")
        lon = elem.get("lon")
        points.append(shapes.Point(point_id, lat, lon))
    return points

if __name__ == "__main__":
    for node in osm_get_nodes("map.osm"):
        print(node)
