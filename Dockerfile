FROM python:3.13-bookworm

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        ca-certificates make \
    && rm -rf /var/lib/apt/lists/*

COPY . /app

WORKDIR /app

RUN make init

CMD ["python3", "main.py"]
