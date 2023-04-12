#!/usr/bin/env python3
"""Module definitiom"""


def list_all(mongo_collection):
    """ lists all documents in a collection """
    documents = mongo_collection.find()

    return list(documents)
