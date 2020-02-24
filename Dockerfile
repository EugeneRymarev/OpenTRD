FROM python:3.8-slim

WORKDIR /opt/opentrd

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "./opentrd.py"]