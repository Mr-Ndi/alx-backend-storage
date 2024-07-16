#!/usr/bin/env python3
"""
Provides statistics about Nginx logs stored in MongoDB.
"""
from pymongo import MongoClient
from collections import Counter


def nginx_logs_stats():
    """
    Retrieves and prints statistics about Nginx logs stored in MongoDB.

    The statistics include:
    - Total number of logs
    - Number of logs by HTTP method (GET, POST, PUT, PATCH, DELETE)
    - Number of logs with method=GET and path=/status
    - Top 10 most present IPs in the logs
    """
    # Connect to the MongoDB server
    client = MongoClient('mongodb://localhost:27017')
    db = client['logs']
    collection = db['nginx']

    # Get the total number of logs
    total_logs = collection.count_documents({})
    print(f"{total_logs} logs")

    # Get the number of logs by HTTP method
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    # Get the number of logs with method=GET and path=/status
    status_check_count = collection
    .count_documents({"method": "GET", "path": "/status"})
    print(f"{status_check_count} status check")

    # Get the top 10 most present IPs
    print("IPs:")
    ip_counts = Counter(collection.distinct("ip"))
    top_ips = ip_counts.most_common(10)
    for ip, count in top_ips:
        print(f"\t{ip}: {count}")


if __name__ == "__main__":
    nginx_logs_stats()
