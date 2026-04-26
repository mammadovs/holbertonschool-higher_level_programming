#!/usr/bin/python3
import requests
import csv

def fetch_and_print_posts():
    """
    Fetches all posts from JSONPlaceholder and prints the titles to the console.
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    # Print the status code regardless of success
    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        # Parse the JSON response into a Python list
        posts = response.json()

        # Iterate through each post and print its title
        for post in posts:
            print(post.get('title'))

def fetch_and_save_posts():
    """
    Fetches all posts from JSONPlaceholder and saves them into a CSV file.
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    if response.status_code == 200:
        posts = response.json()

        # Transform data into a list of dictionaries with specific keys
        filtered_data = [
            {'id': post['id'], 'title': post['title'], 'body': post['body']}
            for post in posts
        ]

        # CSV Configuration
        filename = "posts.csv"
        fieldnames = ['id', 'title', 'body']

        # Save the data to a CSV file
        with open(filename, mode='w', encoding='utf-8', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            # Write the header and the data rows
            writer.writeheader()
            writer.writerows(filtered_data)
