import os
import re
from bs4 import BeautifulSoup

# Create the code in abstract_getty.py to abstract all the image urls from the html files in getty_pages folder.
# The urls should be found from <picture> / <source> tag with attribute of "src"
# and need to convert the "&amp;" into "&" in each url
# save all the urls to the output file called "getty_urls.txt".

def extract_image_urls():
    # Directory containing HTML files
    html_dir = 'getty_pages'
    output_file = 'getty_urls.txt'
    
    # List to store all URLs
    urls = []
    
    # Process each HTML file in the directory
    for filename in os.listdir(html_dir):
        if filename.endswith('.html'):
            file_path = os.path.join(html_dir, filename)
            
            # Read the HTML file
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
            
            # Parse HTML content
            soup = BeautifulSoup(content, 'html.parser')
            
            # Find all picture tags
            picture_tags = soup.find_all('picture')
            
            # Extract URLs from source tags within picture tags
            for tag in picture_tags:
                source_tags = tag.find_all('source', srcset=True)
                for source in source_tags:
                    # Get the srcset attribute and extract the URL
                    url = source['srcset']
                    # Convert &amp; to &
                    url = url.replace('&amp;', '&')
                    urls.append(url)
                
                # Also check for img tags within picture tags
                img_tags = tag.find_all('img', src=True)
                for img in img_tags:
                    # Get the src attribute
                    url = img['src']
                    # Convert &amp; to &
                    url = url.replace('&amp;', '&')
                    urls.append(url)
    
    # Remove duplicates while preserving order
    unique_urls = list(dict.fromkeys(urls))
    
    # Write URLs to output file
    with open(output_file, 'w', encoding='utf-8') as file:
        for url in unique_urls:
            file.write(url + '\n')
    
    print(f"Extracted {len(unique_urls)} unique URLs to {output_file}")

if __name__ == "__main__":
    extract_image_urls()