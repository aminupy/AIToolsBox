FROM tiangolo/uvicorn-gunicorn-fastapi:python3.11

COPY ./IAM_Service/requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY ./IAM_Service/app /app/app
