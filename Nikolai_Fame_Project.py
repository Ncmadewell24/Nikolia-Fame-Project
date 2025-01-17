Python 3.12.8 (tags/v3.12.8:2dc476b, Dec  3 2024, 19:30:04) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import requests
... 
... # Function to fetch content from Unsplash API
... def fetch_unsplash_content(api_key, count=5, query="trending"):
...     url = f"https://api.unsplash.com/photos/random"
...     headers = {"Authorization": f"Client-ID {api_key}"}
...     params = {"count": count, "query": query}
...     
...     try:
...         response = requests.get(url, headers=headers, params=params)
...         if response.status_code == 200:
...             return response.json()  # Return the JSON response containing photos
...         else:
...             print(f"Error: {response.status_code}, {response.text}")
...             return None
...     except Exception as e:
...         print(f"Exception occurred: {e}")
...         return None
... 
... # Replace with your Unsplash API key
... UNSPLASH_API_KEY = "rl4A1PxPFET3_cfrAJa4BVa4gE1k_jAV_RWTd7oyzeM"
... 
... # Fetch sample content (e.g., trending photos)
... sample_content = fetch_unsplash_content(UNSPLASH_API_KEY, count=5, query="trending")
... 
... # Display sample content for verification
... print(sample_content)
