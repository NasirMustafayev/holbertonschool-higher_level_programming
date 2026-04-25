#!/usr/bin/python3
"""
This module contains two functions that interact with a RESTful API
to fetch and print posts, and to fetch and save posts to a CSV file.
"""
import requests
import csv


request = requests.get("https://jsonplaceholder.typicode.com/posts")


def fetch_and_print_posts():
    """Fetches posts from the API and prints their titles."""
    print("Status code: {}".format(request.status_code))

    if request.status_code == 200:

        data = request.json()
        for item in data:
            print(item["title"])


def fetch_and_save_posts():
    """Fetches posts from the API and saves them to a CSV file."""
    if request.status_code == 200:

        data = request.json()

        posts = []
        for item in data:
            posts.append({
                "id": item["id"],
                "title": item["title"],
                "body": item["body"]
            })

        with open("posts.csv", "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=["id", "title", "body"])
            writer.writeheader()
            writer.writerows(posts)
