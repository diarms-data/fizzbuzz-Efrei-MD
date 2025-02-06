FROM python:3.10-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt || echo "No requirements file"

#CMD ["python", "-m", "unittest", "discover", "-s", ".", "-p", "test_*.py"]
CMD ["python", "main.py"]
