import requests
from bs4 import BeautifulSoup
from datetime import datetime
from googletrans import Translator
from urllib.parse import urljoin
import os
import asyncio

TIL_DIR = "til"
translator = Translator()

# 🔧 dev.to 트렌딩 글 하나 크롤링
def fetch_devto_trending():
    try:
        res = requests.get("https://dev.to/", headers={"User-Agent": "Mozilla/5.0"}, timeout=10)
        res.raise_for_status()
    except Exception as e:
        print(f"❌ dev.to 접속 실패: {e}")
        return None, None, None

    soup = BeautifulSoup(res.text, "html.parser")
    article = soup.select_one(".crayons-story__title > a")
    if not article:
        print("❌ 트렌딩 글을 찾지 못했습니다.")
        return None, None, None

    link = urljoin("https://dev.to", article.get("href"))
    title = article.get_text(strip=True)
    author = article.get("href").split("/")[1]
    return title, link, author

# 🔧 기사 본문 수집
def extract_content(link):
    try:
        res = requests.get(link, headers={"User-Agent": "Mozilla/5.0"}, timeout=10)
        res.raise_for_status()
    except Exception as e:
        print(f"❌ 본문 요청 실패: {e}")
        return "(본문 요청 실패)"

    soup = BeautifulSoup(res.text, "html.parser")
    article = soup.select_one(".crayons-article__main")
    if not article:
        print("❌ 본문을 찾을 수 없습니다.")
        return "(본문 추출 실패)"
    return article.get_text(strip=True)

# 🔧 번역 (비동기)
async def translate_korean(text):
    try:
        translated = await asyncio.to_thread(translator.translate, text, dest='ko')
        return translated.text
    except Exception as e:
        print(f"❌ 번역 실패: {e}")
        return "(번역 실패)"

# 🔧 저장
def save_markdown(title, link, author, en_summary, ko_summary):
    today = datetime.now().strftime("%Y-%m-%d")
    filename = f"{today}-TIL.md"
    filepath = os.path.join(TIL_DIR, filename)

    if os.path.exists(filepath):
        print(f"⚠️ 이미 오늘의 TIL이 존재합니다. 저장을 건너뜁니다: {filename}")
        return None

    os.makedirs(TIL_DIR, exist_ok=True)

    try:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(f"# 📌 TIL: {title}\n\n")
            f.write(f"> 원문: [{link}]({link})\n\n")
            f.write(f"🗓 {today}  \n")
            f.write(f"✍️ 작성자: @{author}\n\n")
            f.write("---\n\n")
            f.write("## 🔹 영어 요약\n\n")
            f.write(f"{en_summary}\n\n")
            f.write("---\n\n")
            f.write("## 🔸 한국어 번역\n\n")
            f.write(f"{ko_summary}\n")
        print(f"✅ 저장 완료: {filepath}")
        return filepath
    except Exception as e:
        print(f"❌ 파일 저장 실패: {e}")
        return None

# 🔁 실행
async def main():
    title, link, author = fetch_devto_trending()
    if not title:
        return

    print(f"🔗 링크: {link}")

    content = extract_content(link)
    short_en = content[:1000] + ("..." if len(content) > 1000 else "")
    short_ko = await translate_korean(short_en)
    save_markdown(title, link, author, short_en, short_ko)

if __name__ == '__main__':
    asyncio.run(main())
