#!/usr/bin/env python3
""" Module definition """
from pymongo import MongoClient


if __name__ == "__main__":
    # Connect to MongoDB
    client = MongoClient()
    logs_collection = client.logs.nginx

    # Get number of documents in collection
    num_logs = logs_collection.count_documents({})

    # Get number of documents for each method
    num_get = logs_collection.count_documents({"method": "GET"})
    num_post = logs_collection.count_documents({"method": "POST"})
    num_put = logs_collection.count_documents({"method": "PUT"})
    num_patch = logs_collection.count_documents({"method": "PATCH"})
    num_delete = logs_collection.count_documents({"method": "DELETE"})

    # Get number of documents with method=GET and path=/status
    num_checks = logs_collection.count_documents({
        "method": "GET", "path": "/status"})

    # Print results
    print(f"{num_logs} logs")
    print("Methods:")
    print(f"\tmethod GET: {num_get}")
    print(f"\tmethod POST: {num_post}")
    print(f"\tmethod PUT: {num_put}")
    print(f"\tmethod PATCH: {num_patch}")
    print(f"\tmethod DELETE: {num_delete}")
    print(f"{num_checks} status check")
