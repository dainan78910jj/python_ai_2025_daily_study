# Download images from URLs
# Read in all the image urls from *_urls.txt
# Loop through all urls
# Use curl command to download each image and save to local folder of images/
# If the url is a webp, save it as jpg
# if the file has no extention and the url contains 'fm' query parameter, save it with extention from 'fm' query parameter

import os
import subprocess
from urllib.parse import urlparse, parse_qs
import time
import hashlib
import glob
from PIL import Image

# Create images directory if it doesn't exist
os.makedirs("images", exist_ok=True)

def download_image(url, folder="images"):
    try:
        
        # Parse the URL to get the filename
        parsed_url = urlparse(url)
        filename = os.path.basename(parsed_url.path)
        
        # If no filename in URL path or filename is too long, create a hash-based name
        if not filename or len(filename) > 150:
            filename = hashlib.md5(url.encode()).hexdigest() + ".jpg"
        
        # Handle file extension based on 'fm' query parameter if no extension in filename
        if '.' not in filename and parsed_url.query:
            query_params = parse_qs(parsed_url.query)
            if 'fm' in query_params:
                fm_value = query_params['fm'][0]
                filename = filename + '.' + fm_value.lower()
        
        # Full path for the image
        filepath = os.path.join(folder, filename)
        
        # If file already exists, append a counter
        counter = 1
        original_filepath = filepath
        while os.path.exists(filepath):
            name, ext = os.path.splitext(original_filepath)
            filepath = f"{name}_{counter}{ext}"
            counter += 1
        
        # Use curl to download the image
        curl_command = ["curl", "-L", "--retry", "3", "--retry-delay", "1", "-o", filepath, url]
        result = subprocess.run(curl_command, capture_output=True, text=True)
        
        if result.returncode != 0:
            print(f"Failed to download {url}: {result.stderr}")
            return False

        # Check if the image is WebP and convert to JPG if needed
        if filepath.lower().endswith('.webp'):
            # Convert WebP to JPG
            image = Image.open(filepath)
            rgb_image = image.convert('RGB')
            
            # Change extension to .jpg
            filepath = os.path.splitext(filepath)[0] + '.jpg'
            
            # Change extension to .jpg
            jpg_filepath = os.path.splitext(filepath)[0] + '.jpg'

            # Save as JPG
            rgb_image.save(jpg_filepath, 'JPEG')

            # Remove the original WebP file
            os.remove(filepath)

            filepath = jpg_filepath
        
        print(f"Downloaded: {url} -> {filepath}")
        return True
        
    except Exception as e:
        print(f"Failed to download {url}: {str(e)}")
        return False

def read_urls_from_files():
    """Read URLs from all files matching the pattern *_urls.txt"""
    urls = []
    url_files = glob.glob("*_urls.txt")
    
    if not url_files:
        print("No *_urls.txt files found")
        return urls
    
    for file_path in url_files:
        try:
            with open(file_path, "r") as f:
                file_urls = [line.strip() for line in f if line.strip()]
                urls.extend(file_urls)
                print(f"Read {len(file_urls)} URLs from {file_path}")
        except Exception as e:
            print(f"Error reading {file_path}: {str(e)}")
    
    return urls

if __name__ == "__main__":
    # Read URLs from all *_urls.txt files
    urls = read_urls_from_files()
    
    if not urls:
        print("No URLs found in *_urls.txt files")
        exit(1)
    
    print(f"Found {len(urls)} URLs to download")
    
    # Counter for downloaded images
    downloaded = 0
    failed = 0
    
    # Loop through all urls
    for i, url in enumerate(urls):
        print(f"Processing {i+1}/{len(urls)}: {url}")
        
        # Download each image and save to local folder of images/
        if download_image(url):
            downloaded += 1
        else:
            failed += 1
        
        # Add a small delay to be respectful to the server
        time.sleep(0.1)
    
    print(f"\nDownload complete. Successfully downloaded: {downloaded}, Failed: {failed}")