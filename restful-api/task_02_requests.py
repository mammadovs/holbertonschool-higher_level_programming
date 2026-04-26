#!/usr/bin/python3
import requests
import csv

def fetch_and_print_posts():
    """
    Fetches posts from JSONPlaceholder, prints the status code,
    and displays the titles of all posts in the console.
    """
    url = "https://typicode.com"
    response = requests.get(url)

    # Print the status code of the HTTP response
    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        # Parse the response data into a JSON object (list of dictionaries)
        posts = response.json()

        # Iterate through the list and print only the titles
        for post in posts:
            print(post.get('title'))

def fetch_and_save_posts():
    """
    Fetches posts from JSONPlaceholder and saves specific fields
    (id, title, body) into a CSV file named posts.csv.
    """
    url = "https://typicode.com"
    response = requests.get(url)

    if response.status_code == 200:
        posts = response.json()

        # Structure the data into a list of dictionaries with specific keys
        structured_data = [
            {'id': post['id'], 'title': post['title'], 'body': post['body']}
            for post in posts
        ]

        # Define the filename and column headers
        filename = 'posts.csv'
        fieldnames = ['id', 'title', 'body']

        # Write the structured data to a CSV file
        with open(filename, mode='w', encoding='utf-8', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            # Write the header row
            writer.writeheader()
            # Write all post data rows
            writer.writerows(structured_data)
