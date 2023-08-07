# FastAPI Hero

Project ini diperuntukan sebagai landasan pembelajaran dalam penggunaan fastapi sebagai app backend

# Technology

- Python3.11
- Uvicorn
- SqlAlchemy
- Mysql

# Run Local Server

1. Create database r_game
2. Create virtual environment python

```bash
python3.11 -m venv .venv
```

3. Install library

```bash
pip install --no-cache-dir --upgrade -r ./requirements.txt
```

4. Run server

```bash
uvicorn main:app --reload
```
