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
... UNSPLASH_API_KEY = "6FQMhDULc6p7_I9AVVCpFir2TOavJsCrI9TDN1QKV7E"
... 
... # Fetch sample content (e.g., trending photos)
... sample_content = fetch_unsplash_content(UNSPLASH_API_KEY, count=5, query="trending")
... 
... # Display sample content for verification
... print(sample_content)
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Nikolai's Fame Project</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            text-align: center;
            background-color: #f4f4f9;
            margin: 0;
            padding: 0;
        }
        header {
            background-color: #6200ea;
            color: white;
            padding: 1rem;
        }
        section {
            margin: 2rem;
        }
        img {
            max-width: 100%;
            height: auto;
        }
    </style>
</head>
<body>
    <header>
        <h1>Welcome to Nikolai's Daily Fame</h1>
    </header>
    <section>
        <h2>Today's Inspiration</h2>
        <div id="daily-photo">
            <p>Loading daily photo...</p>
        </div>
    </section>
    <footer>
        <p>&copy; 2025 Nikolai Fame Project</p>
    </footer>
    <script>
        const accessKey = "rl4A1PxPFET3_cfrAJa4BVa4gE1k_jAV_RWTd7oyzeM"; // Your Unsplash API Key
        const apiUrl = `https://api.unsplash.com/photos/random?client_id=${accessKey}&count=1`;

        async function fetchDailyPhoto() {
            try {
                const response = await fetch(apiUrl);
                const data = await response.json();
                const photo = data[0]; // Get the first photo
                document.getElementById("daily-photo").innerHTML = `
                    <img src="${photo.urls.regular}" alt="${photo.alt_description}">
                    <p>${photo.alt_description || "Daily inspiration from Unsplash"}</p>
                `;
            } catch (error) {
                document.getElementById("daily-photo").innerHTML = `<p>Failed to load photo.</p>`;
            }
        }

        fetchDailyPhoto();
    </script>
</body>
</html>
