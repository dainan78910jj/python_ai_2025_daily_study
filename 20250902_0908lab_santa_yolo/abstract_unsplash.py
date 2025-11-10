import re
from bs4 import BeautifulSoup
from urllib.parse import urlparse, parse_qs, urlencode

# Create the code in abstract_unsplash.py to abstract all the image urls from the html files in unsplash.html.
# The urls should be found from <figure> / <img> tag with attribute of "src"
# Remove the url query parameters and only keep the "fm" one
# save all the urls to the output file called "unsplash_urls.txt".

def extract_image_urls():
    # Input and output files
    input_file = 'unsplash.html'
    output_file = 'unsplash_urls.txt'
    
    # List to store all URLs
    urls = []
    
    # Read the HTML file
    with open(input_file, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Parse HTML content
    soup = BeautifulSoup(content, 'html.parser')
    
    # Find all figure tags
    figure_tags = soup.find_all('figure')
    
    # Extract URLs from img tags within figure tags
    for tag in figure_tags:
        img_tags = tag.find_all('img', src=True)
        for img in img_tags:
            urls.append(img['src'])
    
    # Find all img tags directly
    img_tags = soup.find_all('img', src=True)
    for img in img_tags:
        urls.append(img['src'])
    
    # Remove duplicates while preserving order
    unique_urls = list(dict.fromkeys(urls))
    
    # Process URLs to keep only the "fm" query parameter
    processed_urls = []
    for url in unique_urls:
        parsed_url = urlparse(url)
        query_params = parse_qs(parsed_url.query)
        
        # Keep only the "fm" parameter if it exists
        if 'fm' in query_params:
            new_query = urlencode({'fm': query_params['fm'][0]})
            new_url = parsed_url._replace(query=new_query).geturl()
            processed_urls.append(new_url)
        else:
            # If no "fm" parameter, remove all query parameters
            new_url = parsed_url._replace(query='').geturl()
            processed_urls.append(new_url)
    
    # Write URLs to output file
    with open(output_file, 'w', encoding='utf-8') as file:
        for url in processed_urls:
            file.write(url + '\n')
    
    print(f"Extracted {len(processed_urls)} unique URLs to {output_file}")

if __name__ == "__main__":
    extract_image_urls()