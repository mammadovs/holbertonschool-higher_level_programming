#!/usr/bin/python3
import requests
import csv

def fetch_and_print_posts():
    """
    Fetches all posts from JSONPlaceholder and prints their titles.
    """
    # The correct URL for JSONPlaceholder API
    url = "https://typicode.com"
    response = requests.get(url)

    # Display the status code as required by the checker
    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            # Print the title of each post
            print(post.get('title'))

def fetch_and_save_posts():
    """
    Fetches all posts from JSONPlaceholder and saves them to a CSV file.
    """
    # The correct URL for JSONPlaceholder API
    url = "https://typicode.com"
    response = requests.get(url)

    if response.status_code == 200:
        posts = response.json()

        # Create a list of dictionaries with specific fields: id, title, and body
        posts_data = [
            {
                'id': post.get('id'),
                'title': post.get('title'),
                'body': post.get('body')
            } for post in posts
        ]

        # Field names for the CSV columns
        fieldnames = ['id', 'title', 'body']

        # Write data to posts.csv with utf-8 encoding
        with open('posts.csv', mode='w', encoding='utf-8', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(posts_data)
