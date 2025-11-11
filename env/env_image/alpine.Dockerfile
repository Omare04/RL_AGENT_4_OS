FROM alpine:3.20

RUN apk add --no-cache python3 py3-pip
RUN python3 -m venv /venv
ENV PATH="/venv/bin:$PATH"

RUN pip install flask

WORKDIR /app
COPY server.py .

EXPOSE 5000
CMD ["python3", "server.py"k
