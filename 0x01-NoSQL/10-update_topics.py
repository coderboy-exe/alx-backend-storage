#!/usr/bin/env python3
"""Module definition"""


def update_topics(mongo_collection, name, topics):
    """Changes all topics on a school document based on the name"""
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
