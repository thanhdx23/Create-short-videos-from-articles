# -*- coding: utf-8 -*-
import os
from gtts import gTTS

def generate_voice(summary_text, output_file="output.mp3", speed=1.5):
    tts = gTTS(text=summary_text, lang='vi')
    tts.save(output_file)
    print(f"Voice saved to {output_file}")


def generate_faster_voice(input_file, output_file, speed=1.5):

    # Tăng tốc độ bằng FFmpeg
    faster_output = output_file
    os.system(f'ffmpeg -i {input_file} -filter:a "atempo={speed}" -vn {faster_output}')
    print(f"Faster voice saved to {faster_output}")

