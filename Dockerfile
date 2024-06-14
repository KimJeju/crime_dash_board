FROM python:3.11


COPY . /src
WORKDIR /src

RUN pip install -r requirements.txt

EXPOSE 8892

CMD  python main.py