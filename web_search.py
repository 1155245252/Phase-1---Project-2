import requests
import sys

# Replace with your own Google Custom Search API key and Search Engine ID
API_KEY = 'YOUR_API_KEY'
SEARCH_ENGINE_ID = 'YOUR_SEARCH_ENGINE_ID'


def google_search(query, api_key=API_KEY, cse_id=SEARCH_ENGINE_ID, num=5):
    """Perform a Google search and return the results."""
    url = 'https://www.googleapis.com/customsearch/v1'
    params = {
        'q': query,
        'key': api_key,
        'cx': cse_id,
        'num': num
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()


def print_results(results):
    items = results.get('items', [])
    if not items:
        print('No results found.')
        return
    for i, item in enumerate(items, 1):
        title = item.get('title')
        link = item.get('link')
        snippet = item.get('snippet')
        print(f"{i}. {title}\n{link}\n{snippet}\n")


def main():
    if len(sys.argv) < 2:
        print('Usage: python web_search.py "search query"')
        sys.exit(1)
    query = ' '.join(sys.argv[1:])
    try:
        results = google_search(query)
        print_results(results)
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
        if http_err.response is not None:
            print(f"Status code: {http_err.response.status_code}")
            print(f"Response content: {http_err.response.text}")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == '__main__':
    main()

"""
Setup Instructions:
1. Get a Google Custom Search API key: https://developers.google.com/custom-search/v1/overview
2. Create a Custom Search Engine and get the Search Engine ID: https://cse.google.com/cse/all
3. Replace 'YOUR_API_KEY' and 'YOUR_SEARCH_ENGINE_ID' with your credentials above.
4. Install requests if not already: pip install requests
5. Run: python web_search.py "your search query"
"""
