# Short Video Creation with Text, Audio, and Images

This project is a Python-based tool for creating short videos using images, audio, and text. It uses various Python libraries to extract content from URLs, summarize articles, generate voice-over, download images, and compile them into a video.

## Prerequisites

- Python 3.x
- `openai`
- `newspaper3k`
- `beautifulsoup4`
- `requests`
- `moviepy`
- `gtts`
- `dotenv` (optional if you are using `.env` files)

## Functionality

1. **Article Summarization**: Uses OpenAI's API to summarize the main content of an article.
2. **Voice Generation**: Generates a voice-over using Google Text-to-Speech (gTTS).
3. **Image Downloading**: Extracts and downloads main images from the article.
4. **Video Creation**: Combines images and audio into a video with a banner displaying the title.
