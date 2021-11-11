FROM python:3.7-alpine
LABEL Description="executer" VERSION='1.0'

RUN apk update && apk add gcc g++ make openssl-dev python3-dev libffi-dev autoconf

WORKDIR /opt/hexqbot_executer
RUN mkdir -p /opt/hexqbot_executer

COPY executer.py .

RUN python -m pip install fastapi && python -m pip install uvicorn

EXPOSE 20000
CMD ["python", "-u", "executer.py"]
