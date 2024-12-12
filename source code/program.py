from summarize_text import summarize_article_from_url, get_article_from_url
from generate_voice import generate_voice, generate_faster_voice
from get_image import get_main_images_from_article, download_images
from create_video import create_video
from moviepy.config import change_settings




if __name__ == "__main__":
    change_settings({"IMAGEMAGICK_BINARY": "C:/Program Files/ImageMagick-7.1.1-Q16-HDRI/magick.exe"})
    #Đường dẫn tới thư mục chứa ảnh và tệp âm thanh
    url = "https://thanhnien.vn/chu-tich-tphcm-neu-huong-xu-ly-hon-1000-nha-dat-cong-bo-trong-185241210091326944.htm"

    summary = summarize_article_from_url(url)

    generate_voice(summary, "output.mp3")
    generate_faster_voice("output.mp3", "faster_output.mp3")
    main_images_url = get_main_images_from_article(url)
    download_images(main_images_url, "Image")

    image_folder = "Image"  # Thay bằng đường dẫn tới thư mục chứa ảnh
    audio_file = "faster_output.mp3"  # Thay bằng đường dẫn tới tệp âm thanh
    output_file = "output_video.mp4"  # Tên tệp video đầu ra
    title_text, _ = get_article_from_url(url)  # Tiêu đề của video

    create_video(image_folder, audio_file, output_file, title_text)
