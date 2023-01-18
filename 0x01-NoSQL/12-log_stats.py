#!/usr/bin/env python3
"""
Provides stats about nginx logs
"""


def update_topics(mongo_collection, name, topics):
    """
    Updates topics in a document
    Parameters:
    mongo_collection (collection): collection to insert
    a new document
    name (str): name of schools to update topics
    topics (list): new topics

    Returns:
    Id of new document
    """

    mongo_collection.update_one({'name': name},
                                {'$set': {'topics': topics}})
