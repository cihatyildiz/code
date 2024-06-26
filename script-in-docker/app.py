import requests

def fetch_website():
    url = "http://itsociety.org"
    response = requests.get(url)
    print(f"Status Code: {response.status_code}")
    print(f"Content: {response.text[:200]}") 

if __name__ == "__main__":
    fetch_website()
