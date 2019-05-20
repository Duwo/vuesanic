FROM python:3.6

RUN pip install sanic
RUN pip install requests-async

ADD backend /backend
EXPOSE 8000

WORKDIR /backend

CMD ["python", "main.py"]
