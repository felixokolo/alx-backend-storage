#!/usr/bin/env python3
"""
Gets all documents in a collection
"""


def list_all(mongo_collection):
    """
    Returns a list of documents in mongo_collection

    Paramenters:
        mongo_collection (collection): collection
        to query

    Returns:
        List of documents in mongo_collection
    """

    return mongo_collection.find()
