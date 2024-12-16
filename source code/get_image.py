from bs4 import BeautifulSoup
import requests
import os

def get_main_images_from_article(url):
    # Submit request to article
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Based on tags containing main images (common on newspaper pages)
    main_images = []

    # Search in <figure>, <div> tags or related classes
    for figure in soup.find_all('figure'):
        img_tag = figure.find('img')
        if img_tag and 'src' in img_tag.attrs:
            img_url = img_tag['src']
            if img_url not in main_images: # Avoid duplication
                main_images.append(img_url)

    # Find more <img> tags with related classes
    for img_tag in soup.find_all('img', class_=['main-image', 'featured-image']):
        img_url = img_tag['src']
        if img_url not in main_images:
            main_images.append(img_url)

    # Complete URL if header is missing
    main_images = [
        img if img.startswith('http') else f"{url.rsplit('/', 1)[0]}/{img}" for img in main_images
    ]

    return main_images

def download_images(image_urls, download_folder):
    # Create directory if it does not exist
    os.makedirs(download_folder, exist_ok=True)

    # Load individual images
    for idx, img_url in enumerate(image_urls):
        try:
            response = requests.get(img_url, stream=True)
            if response.status_code == 200:
                file_extension = img_url.split('.')[-1] # Get file extension
                file_name = f"image_{idx + 1}.{file_extension}"
                file_path = os.path.join(download_folder, file_name)

                # Save image to folder
                with open(file_path, 'wb') as img_file:
                    for chunk in response.iter_content(1024):
                        img_file.write(chunk)
                print(f"Đã tải: {file_path}")
            else:
                print(f"Error loading image: {img_url}")
        except Exception as e:
            print(f"Error: {e} with image: {img_url}")


            
