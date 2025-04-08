import requests
from bs4 import BeautifulSoup
import google.generativeai as genai
import time

# Gemini API anahtarını ayarla
GEMINI_API_KEY = "key"
genai.configure(api_key=GEMINI_API_KEY)

def fetch_single_article(article):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    
    title = article.text.strip()
    link_tag = article.find_parent("a", href=True)
    article_url = link_tag["href"] if link_tag else None
    
    if article_url:
        # Haberin detay sayfasını çek
        article_response = requests.get(article_url, headers=headers)
        article_soup = BeautifulSoup(article_response.content, "html.parser")
        
        # Haber içeriğini bul
        content_div = article_soup.find("div", class_="articlebody")
        content = content_div.get_text(strip=True) if content_div else "İçerik bulunamadı."
    else:
        content = "URL yok, içerik çekilemedi."
    
    return {"title": title, "url": article_url, "content": content}

def summarize_with_gemini(content):
    # Gemini modelini başlat
    model = genai.GenerativeModel("gemini-1.5-pro")
    
    # Özetleme promptu
    prompt = f"Bu metni Türkçe olarak kısa ve öz bir şekilde özetle:\n\n{content}"
    response = model.generate_content(prompt)
    
    return response.text

def fetch_and_summarize_articles(limit=5, delay=10):
    url = "https://thehackernews.com/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    
    # Anasayfayı çek
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")
    articles = soup.find_all("h2", class_="home-title")[:limit]
    
    print("The Hacker News'ten Haberler ve Özetler:")
    print("=" * 70)
    
    for i, article in enumerate(articles, 1):
        # Tek tek haber çek ve özetle
        news = fetch_single_article(article)
        try:
            summary = summarize_with_gemini(news["content"])
        except Exception as e:
            summary = f"Özetleme başarısız: {str(e)}"
        
        # Haber ve özeti yazdır
        print(f"{i}. Başlık: {news['title']}")
        print(f"   URL: {news['url']}")
        print(f"   Özet: {summary}")
        print("=" * 70)
        
        # Bir sonraki isteğe geçmeden önce bekle (son haber hariç)
        if i < limit:
            print(f"{delay} saniye bekleniyor...")
            time.sleep(delay)

if __name__ == "__main__":
    # 5 haber için tek tek istek at ve 10 saniye bekle
    fetch_and_summarize_articles(limit=5, delay=60)