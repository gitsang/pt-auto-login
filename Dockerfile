FROM debian:bullseye-slim

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        ca-certificates python3 python3-pip python3-setuptools make \
    && rm -rf /var/lib/apt/lists/*

COPY . /app

WORKDIR /app

RUN make init

CMD ["python3", "main.py"]
