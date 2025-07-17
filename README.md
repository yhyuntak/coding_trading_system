# coin-trading-system

## 프로젝트 실행 방법

1. **가상환경 생성 및 활성화**

```bash
uv venv
source .venv/bin/activate
```

- `uv venv` : 가상환경 생성(이미 있으면 스킵)
- `source .venv/bin/activate` : 가상환경 진입

2. **프로젝트 실행**

```bash
python main.py
```

또는

```bash
uv run python main.py
```

- `uv run` 명령어는 가상환경 진입 없이도 자동으로 해당 프로젝트의 가상환경에서 실행합니다.

---

## 참고

- 패키지 설치, 의존성 관리는 반드시 uv 명령어(`uv pip install ...`)를 사용하세요.
- Streamlit, FastAPI 등 별도의 실행 명령이 필요한 경우 각 도구의 공식 실행 명령을 사용하면 됩니다.
- 실행 중 에러가 발생하면 에러 메시지를 복사해서 질문해 주세요.
