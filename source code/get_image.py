from bs4 import BeautifulSoup
import requests
import os

def get_main_images_from_article(url):
    # Gửi yêu cầu đến bài báo
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Dựa vào các thẻ chứa hình ảnh chính (phổ biến trên các trang báo)
    main_images = []

    # Tìm trong các thẻ <figure>, <div> hoặc các class liên quan
    for figure in soup.find_all('figure'):
        img_tag = figure.find('img')
        if img_tag and 'src' in img_tag.attrs:
            img_url = img_tag['src']
            if img_url not in main_images:  # Tránh trùng lặp
                main_images.append(img_url)

    # Tìm thêm trong các thẻ <img> có class liên quan
    for img_tag in soup.find_all('img', class_=['main-image', 'featured-image']):
        img_url = img_tag['src']
        if img_url not in main_images:
            main_images.append(img_url)

    # Hoàn thiện URL nếu thiếu phần đầu
    main_images = [
        img if img.startswith('http') else f"{url.rsplit('/', 1)[0]}/{img}" for img in main_images
    ]

    return main_images

def download_images(image_urls, download_folder):
    # Tạo thư mục nếu chưa tồn tại
    os.makedirs(download_folder, exist_ok=True)

    # Tải từng hình ảnh
    for idx, img_url in enumerate(image_urls):
        try:
            response = requests.get(img_url, stream=True)
            if response.status_code == 200:
                file_extension = img_url.split('.')[-1]  # Lấy phần đuôi file
                file_name = f"image_{idx + 1}.{file_extension}"
                file_path = os.path.join(download_folder, file_name)

                # Lưu hình ảnh vào thư mục
                with open(file_path, 'wb') as img_file:
                    for chunk in response.iter_content(1024):
                        img_file.write(chunk)
                print(f"Đã tải: {file_path}")
            else:
                print(f"Lỗi khi tải hình ảnh: {img_url}")
        except Exception as e:
            print(f"Lỗi: {e} với hình ảnh: {img_url}")


            