#!/usr/bin/env python3
""" Task 12. Log stats"""


from pymongo import MongoClient


def nginx_logs_stats():
    """
        This is a function that Connect to the MongoDB server
        Get the total number of logs, Get the number of logs by HTTP method
        lastl it has a Get the number of logs with method=GET and path=/status
    """
    client = MongoClient('mongodb://localhost:27017')
    db = client['logs']
    collection = db['nginx']
    total_logs = collection.count_documents({})
    print(f"{total_logs} logs")
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")
    status_check_count = collection.
    count_documents({"method": "GET", "path": "/status"})
    print(f"{status_check_count} status check")


if __name__ == "__main__":
    nginx_logs_stats()
