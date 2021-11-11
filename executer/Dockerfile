FROM python:3.7-alpine
LABEL Description="HexQBot-executer" VERSION='1.0'

WORKDIR /opt/hexqbot_executer
RUN mkdir -p /opt/hexqbot_executer

COPY main.py .

RUN python -m pip install fastapi

EXPOSE 20000
CMD ["python", "main.py"]
