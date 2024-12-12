from moviepy.editor import *
import os

def create_video(image_folder, audio_file, output_file, title_text, fps=24):
    """
    Create a video from a folder of images, audio, and other types of title banners that are displayed throughout.
    
    Arguments:
    image_folder (str): Path to the folder containing the images.
    audio_file (str): Path to the audio file.
    out_file (str): The output file name of the video.
    title_text (str): Title of the video (displayed as a banner).
    fps (int): Number of frames per second.
    
    Returns:
    None
    """
    # Create a list of images
    image_files = sorted([
        os.path.join(image_folder, img) for img in os.listdir(image_folder) if img.endswith((".png", ".jpg", ".jpeg"))
    ])

    if not image_files:
        raise ValueError("Thư mục ảnh không chứa hình ảnh hợp lệ.")

    # Load audio file and get duration
    audio = AudioFileClip(audio_file)
    audio_duration = audio.duration  # Thời lượng tệp âm thanh

    # Calculate display duration of each image
    image_duration = audio_duration / len(image_files)

    if image_duration <= 0:
        raise ValueError("Thời gian hiển thị mỗi ảnh không đủ. Hãy tăng số lượng ảnh.")

    # Create video from photos
    clips = []
    for image_file in image_files:
        img_clip = ImageClip(image_file).set_duration(image_duration)  # Thời lượng hiển thị mỗi ảnh
        clips.append(img_clip)

    # Merge photo clips into one video
    video = concatenate_videoclips(clips, method="compose")

    # Add title as banner
    title_clip = TextClip(
        title_text,
        fontsize=40,
        color='white',
        bg_color='black',
        size=(video.size[0], 100),
        method='caption'
    ).set_position(("center", "bottom")).set_duration(audio_duration)

    # Combine banner title with video
    final_video = CompositeVideoClip([video, title_clip])

    # Add audio to video
    final_video = final_video.set_audio(audio)

    # Export video
    final_video.write_videofile(output_file, fps=fps, codec="libx264")


