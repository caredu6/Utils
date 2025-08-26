import requests
import pandas as pd

# Step 1: Make the HTTP GET request
url = "https://jsonplaceholder.typicode.com/users"  # Example API endpoint
response = requests.get(url)

# Step 2: Check for successful response
if response.status_code == 200:
    data = response.json()  # Parse JSON response

    # Step 3: Convert JSON to DataFrame
    df = pd.json_normalize(data)  # flattens nested fields

    # Step 4: Export to CSV
    output_file = "output.csv"
    df.to_csv(output_file, index=False)

    print(f"Data successfully written to {output_file}")
else:
    print(f"Request failed with status code: {response.status_code}")
