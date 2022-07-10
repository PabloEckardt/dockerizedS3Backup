FROM python:3.8-alpine3.10

ADD main.py .

RUN apk add --no-cache gnupg

RUN pip install requests
RUN pip install python-gnupg

CMD ["python","./main.py"]


