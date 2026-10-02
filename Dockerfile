FROM python:3.12-slim

WORKDIR /gradeCalculator

COPY app.py .

CMD ["python" , "-u" , "app.py"]