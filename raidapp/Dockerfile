FROM python:3.12-alpine



ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /raidapp

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt



COPY . .

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]