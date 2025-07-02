

# rss-til-bot

dev.to에서 인기 게시글을 가져와 간단하게 요약하고, 한국어로 번역한 후 `til/` 폴더에 마크다운으로 저장하는 자동화 봇입니다.  
GitHub Actions를 통해 매일 새 TIL을 생성합니다.

---

## 🛠 사용 기술

- Python 3.10+
- GitHub Actions
- OpenAI API (또는 다른 번역 API 사용 가능)

---

## 📦 설치 및 실행 방법

### 1. 의존성 설치

```bash
pip install -r requirements.txt
````

### 2. 로컬에서 실행하기

```bash
python rss_til.py
```

> 🔧 `.env` 파일에 필요한 환경변수를 설정해야 합니다. (예: `OPENAI_API_KEY`)

---

## 🧾 기능 설명

* `rss_til.py`:

  * dev.to 인기 글을 하나 가져옴
  * 내용을 요약하고 한국어 번역
  * `til/` 디렉토리에 날짜 기반 마크다운 파일 저장

* `.github/workflows/rss.yml`:

  * 매일 1회 GitHub Actions로 자동 실행
  * 레포에 커밋으로 저장됨

---

## ⚙️ 환경변수 (.env)

```env
OPENAI_API_KEY=your_openai_key_here
```

또는 사용하는 번역 API에 맞게 조정하세요.

---

## 📁 디렉토리 구조

```
rss-til-bot/
├── rss_til.py
├── til/
│   └── 2025-07-02.md
├── requirements.txt
├── .github/
│   └── workflows/
│       └── rss.yml
└── README.md
```

---

## 📅 자동화 스케줄

GitHub Actions가 매일 오전 9시(KST 기준) `rss_til.py`를 실행하고, 결과를 `til/` 폴더에 저장 후 커밋합니다.

---

## 📄 라이선스

MIT License (원하면 `LICENSE` 파일 추가 가능)

---

## 💡 향후 개선사항

* 요약 정확도 향상
* 번역 품질 튜닝
* 멀티 RSS 지원
* TIL 포맷 커스터마이징

---

## 🙋 문의

개선 제안, 버그 제보는 [Issues](https://github.com/your-id/rss-til-bot/issues)로 주세요!

