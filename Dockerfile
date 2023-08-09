FROM python:3.8-slim
WORKDIR /git

RUN apt-get update && \
    apt-get install -y \
    git \
    && rm -rf /var/lib/apt/lists/*

RUN git clone https://github.com/IAM-KIRAN/Testcase1.git /git

CMD python p1.py