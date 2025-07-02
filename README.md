# rss-til-bot

이 저장소는 dev.to에서 인기 글을 가져와 간단히 요약하고 한국어로 번역하여 마크다운 형식의 TIL(Today I Learned) 파일로 저장해 주는 파이썬 스크립트와 GitHub Actions 워크플로우를 포함합니다.

## 요구 사항

- Python 3.10 이상
- `requirements.txt`에 명시된 파이썬 패키지들

의존성 설치 예시는 다음과 같습니다.

```bash
pip install -r requirements.txt
```

## 사용 방법

1. 저장소를 클론한 뒤 위의 명령으로 필요한 패키지를 설치합니다.
2. `python rss_til.py` 명령을 실행하면 최신 dev.to 글을 요약하여 `til/` 폴더에 마크다운 파일로 저장합니다.

## GitHub Actions 워크플로우

`.github/workflows/rss.yml` 파일에 정의된 워크플로우가 매일 한 번 실행됩니다. 이 워크플로우는 랜덤한 시간에 `rss_til.py` 스크립트를 실행하고, 새로 생성된 TIL 파일을 커밋하여 저장소에 자동으로 업로드합니다.
