FROM python:3.13-bookworm

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        ca-certificates make \
    && rm -rf /var/lib/apt/lists/*

RUN install -d -m 0755 /etc/apt/keyrings \
    && wget -q https://packages.mozilla.org/apt/repo-signing-key.gpg -O- | \
        tee /etc/apt/keyrings/packages.mozilla.org.asc > /dev/null \
    && gpg -n -q --import --import-options import-show /etc/apt/keyrings/packages.mozilla.org.asc | awk '/pub/{getline; gsub(/^ +| +$/,""); print "\n"$0"\n"}' \
    && echo "deb [signed-by=/etc/apt/keyrings/packages.mozilla.org.asc] https://packages.mozilla.org/apt mozilla main" | tee -a /etc/apt/sources.list.d/mozilla.list > /dev/null \
    && apt-get update \
    && apt-get install -y --no-install-recommends firefox

COPY . /app

WORKDIR /app

RUN make init

CMD ["python3", "main.py"]
