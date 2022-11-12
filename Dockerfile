FROM python:3.9-alpine
WORKDIR /usr/src/app
COPY . .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install -r requirements.txt
CMD ["python","-u","app.py"]