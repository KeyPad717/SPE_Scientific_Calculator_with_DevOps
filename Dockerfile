FROM python:3.10-slim   
#lightweight python image
WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

CMD ["sh", "-c", "python -m calculator.main || tail -f /dev/null"]
#command