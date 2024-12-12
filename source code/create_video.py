from moviepy.editor import *
import os

def create_video(image_folder, audio_file, output_file, title_text, fps=24):
    """
    Tạo video từ thư mục ảnh, âm thanh và thêm tiêu đề dạng banner hiển thị xuyên suốt.

    Args:
        image_folder (str): Đường dẫn tới thư mục chứa ảnh.
        audio_file (str): Đường dẫn tới tệp âm thanh.
        output_file (str): Tên tệp video đầu ra.
        title_text (str): Tiêu đề của video (hiển thị như banner).
        fps (int): Số khung hình mỗi giây.

    Returns:
        None
    """
    # Tạo danh sách các bức ảnh
    image_files = sorted([
        os.path.join(image_folder, img) for img in os.listdir(image_folder) if img.endswith((".png", ".jpg", ".jpeg"))
    ])

    if not image_files:
        raise ValueError("Thư mục ảnh không chứa hình ảnh hợp lệ.")

    # Tải tệp âm thanh và lấy thời lượng
    audio = AudioFileClip(audio_file)
    audio_duration = audio.duration  # Thời lượng tệp âm thanh

    # Tính toán thời lượng hiển thị mỗi ảnh
    image_duration = audio_duration / len(image_files)

    if image_duration <= 0:
        raise ValueError("Thời gian hiển thị mỗi ảnh không đủ. Hãy tăng số lượng ảnh.")

    # Tạo video từ các bức ảnh
    clips = []
    for image_file in image_files:
        img_clip = ImageClip(image_file).set_duration(image_duration)  # Thời lượng hiển thị mỗi ảnh
        clips.append(img_clip)

    # Ghép các clip ảnh thành một video
    video = concatenate_videoclips(clips, method="compose")

    # Thêm tiêu đề dưới dạng banner
    title_clip = TextClip(
        title_text,
        fontsize=40,
        color='white',
        bg_color='black',
        size=(video.size[0], 100),
        method='caption'
    ).set_position(("center", "bottom")).set_duration(audio_duration)

    # Kết hợp tiêu đề banner với video
    final_video = CompositeVideoClip([video, title_clip])

    # Thêm âm thanh vào video
    final_video = final_video.set_audio(audio)

    # Xuất video
    final_video.write_videofile(output_file, fps=fps, codec="libx264")


