FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app
COPY . .

RUN uv python install
RUN uv sync frozen

RUN adduser --disabled-password --gecos "" myuser
USER myuser

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
