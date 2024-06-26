import requests
import argparse

def fetch_website(url):
    response = requests.get(url)
    print(f"Status Code: {response.status_code}")
    print(f"Content: {response.text[:200]}") 

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Fetch a website')
    parser.add_argument('url', type=str, help='The URL of the website to fetch')
    args = parser.parse_args()

    fetch_website(args.url)
