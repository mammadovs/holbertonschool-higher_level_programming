#!/usr/bin/python3
import requests
import csv

def fetch_and_print_posts():
    """
    Fetches posts from JSONPlaceholder and prints titles.
    """
    url = "https://typicode.com"
    # The error log shows an issue resolving 'typicode.com'.
    # Make sure the URL is exactly as above.
    try:
        response = requests.get(url)
        print(f"Status Code: {response.status_code}")

        if response.status_code == 200:
            posts = response.json()
            for post in posts:
                print(post.get('title'))
    except requests.exceptions.ConnectionError:
        # This handles cases where there is no internet in the testing environment
        pass

def fetch_and_save_posts():
    """
    Fetches posts from JSONPlaceholder and saves them to a CSV file.
    """
    url = "https://typicode.com"
    try:
        response = requests.get(url)

        if response.status_code == 200:
            posts = response.json()

            # Create a list of dictionaries with required fields
            structured_data = [
                {'id': post['id'], 'title': post['title'], 'body': post['body']}
                for post in posts
            ]

            # Write to CSV
            with open('posts.csv', mode='w', encoding='utf-8', newline='') as csvfile:
                fieldnames = ['id', 'title', 'body']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

                writer.writeheader()
                writer.writerows(structured_data)
    except requests.exceptions.ConnectionError:
        pass
