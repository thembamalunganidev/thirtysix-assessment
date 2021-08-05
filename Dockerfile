FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY . /app
RUN pip3 install -r requirements.txt
RUN chmod +x /app/wait-for-it.sh
