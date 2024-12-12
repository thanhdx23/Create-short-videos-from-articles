import openai
from newspaper import Article
import os

from openai import OpenAI
# Set up your API key

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

# create a list of models 
GPT_MODELS = ["gpt-4o", "gpt-4o-mini"]

# Function to extract article title and content from URL
def get_article_from_url(url):
    article = Article(url)
    article.download() # Download article content
    article.parse()  # Text analysis and extraction
    title = article.title  # Get the article title
    content = article.text  # Get article content
    return title, content  # Returns both title and content


# Function to summarize article with title
def summarize_text_with_title(title, content, model_name = "gpt-4o-mini"):
    # Combine title and content
    combined_text = f"Tiêu đề bài báo: {title}\n\nNội dung bài báo: {content}"

    # Use the OpenAI API for combined text summarization
    response = client.chat.completions.create(
        model= model_name,
        messages=[{"role": "system", "content": "You are a helpful assistant."},
                  {"role": "user", "content": f"Tóm tắt bài báo sau ( Đầu ra chỉ bao gồm nội dung chính, không thêm phần mở đầu hoặc tiêu đề): {combined_text}"}],
        temperature=0.5  # Điều chỉnh độ sáng tạo của mô hình
    )
    return response.choices[0].message.content.strip()

# Function to get article from URL and abstract including title
def summarize_article_from_url(url):
    title, content = get_article_from_url(url)
    summary = summarize_text_with_title(title, content)
    return summary
