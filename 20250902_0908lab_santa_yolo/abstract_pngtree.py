import os
import re
from bs4 import BeautifulSoup

# Create the code in abstract_pngtree.py to abstract all the image urls from the html files in pngtree_pages folder.
# The urls should be found from <figure> / <p> tag with attribute of "src"
# save all the urls to the output file called "pngtree_urls.txt".

def extract_image_urls():
    # Directory containing HTML files
    html_dir = 'pngtree_pages'
    output_file = 'pngtree_urls.txt'
    
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
            
            # Find all figure and p tags
            figure_tags = soup.find_all('figure')
            p_tags = soup.find_all('p')
            
            # Extract URLs from img tags within figure tags
            for tag in figure_tags:
                img_tags = tag.find_all('img', src=True)
                for img in img_tags:
                    urls.append(img['src'])
            
            # Extract URLs from img tags within p tags
            for tag in p_tags:
                img_tags = tag.find_all('img', src=True)
                for img in img_tags:
                    urls.append(img['src'])
    
    # Remove duplicates while preserving order
    unique_urls = list(dict.fromkeys(urls))
    
    # Write URLs to output file
    with open(output_file, 'w', encoding='utf-8') as file:
        for url in unique_urls:
            file.write(url + '\n')
    
    print(f"Extracted {len(unique_urls)} unique URLs to {output_file}")

if __name__ == "__main__":
    extract_image_urls()