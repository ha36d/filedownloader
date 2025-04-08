import os
import requests
from bs4 import BeautifulSoup
import urllib.parse

# Base URL
base_url = "https://example.com/"
pattern = "folder/"

# Directory to save files
output_dir = "output"
extension = ".pdf"
os.makedirs(output_dir, exist_ok=True)

def get_one_level_urls(base_url):
    """Fetch all one-level URLs matching the pattern."""
    response = requests.get(base_url)
    if response.status_code != 200:
        print(f"Failed to fetch the base URL: {base_url}")
        return []

    soup = BeautifulSoup(response.text, "html.parser")
    urls = []

    # Find all <a> tags with href matching the pattern
    for a_tag in soup.find_all("a", href=True):
        href = a_tag["href"]
        if href.startswith(pattern) and href.count("/") == 2:
            full_url = urllib.parse.urljoin(base_url, href)
            urls.append(full_url)

    return urls

def download_file(url):
    """Download the extension file from the given URL if it exists."""
    try:
        response = requests.get(url)
        if response.status_code != 200:
            print(f"Failed to fetch URL: {url}")
            return

        soup = BeautifulSoup(response.text, "html.parser")

        # Find all <a> tags with href ending in extension
        for a_tag in soup.find_all("a", href=True):
            href = a_tag["href"]
            if href.endswith(extension):
                file_url = urllib.parse.urljoin(url, href)
                file_response = requests.get(file_url)
                if file_response.status_code == 200:
                    file_name = os.path.join(output_dir, os.path.basename(href))
                    with open(file_name, "wb") as file_file:
                        file_file.write(file_response.content)
                    print(f"Downloaded: {file_name}")
                else:
                    print(f"Failed to download file: {file_url}")
    except Exception as e:
        print(f"Error processing URL {url}: {e}")

def rename_files(folder):
    """Rename files in the folder by decoding URL-encoded characters."""
    for filename in os.listdir(folder):
        # Decode URL-encoded characters in the filename
        decoded_name = urllib.parse.unquote(filename)
        if filename != decoded_name:
            old_path = os.path.join(folder, filename)
            new_path = os.path.join(folder, decoded_name)
            os.rename(old_path, new_path)
            print(f"Renamed: {filename} -> {decoded_name}")
        else:
            print(f"No changes needed for: {filename}")

def main():
    print("Fetching one-level URLs...")
    urls = get_one_level_urls(base_url)
    print(f"Found {len(urls)} URLs.")

    for url in urls:
        print(f"Processing URL: {url}")
        download_file(url)
        
    rename_files(output_dir)

if __name__ == "__main__":
    main()