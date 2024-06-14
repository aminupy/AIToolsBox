FROM tiangolo/uvicorn-gunicorn-fastapi:python3.11

# Install tesseract OCR
RUN apt-get -o Acquire::Check-Valid-Until=false update && apt-get install -y tesseract-ocr libtesseract-dev

# Copy application requirements
COPY ./OCR_Service/requirements.txt /app/requirements.txt

# Install Python dependencies
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

# Copy application code
COPY ./OCR_Service/app /app/app


