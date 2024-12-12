import openai
from newspaper import Article
import os

from openai import OpenAI
# Thiết lập API key của bạn


client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

# create a list of models 
GPT_MODELS = ["gpt-4o", "gpt-4o-mini"]

# Hàm trích xuất tiêu đề và nội dung bài báo từ URL
def get_article_from_url(url):
    article = Article(url)
    article.download()  # Tải nội dung bài báo
    article.parse()  # Phân tích và trích xuất văn bản
    title = article.title  # Lấy tiêu đề bài báo
    content = article.text  # Lấy nội dung bài báo
    return title, content  # Trả về cả tiêu đề và nội dung


# Hàm tóm tắt bài báo với tiêu đề
def summarize_text_with_title(title, content, model_name = "gpt-4o-mini"):
    # Kết hợp tiêu đề và nội dung
    combined_text = f"Tiêu đề bài báo: {title}\n\nNội dung bài báo: {content}"

    # Sử dụng OpenAI API v1.0.0 mới để tóm tắt văn bản kết hợp
    response = client.chat.completions.create(
        model= model_name,
        messages=[{"role": "system", "content": "You are a helpful assistant."},
                  {"role": "user", "content": f"Tóm tắt bài báo sau ( Đầu ra chỉ bao gồm nội dung chính, không thêm phần mở đầu hoặc tiêu đề): {combined_text}"}],
        temperature=0.5  # Điều chỉnh độ sáng tạo của mô hình
    )
    return response.choices[0].message.content.strip()

# Hàm lấy bài báo từ URL và tóm tắt bao gồm cả tiêu đề
def summarize_article_from_url(url):
    title, content = get_article_from_url(url)
    summary = summarize_text_with_title(title, content)
    return summary
