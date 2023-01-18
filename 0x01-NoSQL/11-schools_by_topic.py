#!/usr/bin/env python3
"""
Returns a list of schools with specific topic
"""


def schools_by_topic(mongo_collection, topic):
    """
    Returns a list of schools with specific topic
    Parameters:
    mongo_collection (collection): collection to insert
    a new document
    topic (str): name of topic to find
    Returns:
    list of schools
    """

    return mongo_collection.find()
