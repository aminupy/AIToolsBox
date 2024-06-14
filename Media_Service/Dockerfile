FROM tiangolo/uvicorn-gunicorn-fastapi:python3.11

# Install supervisor
RUN apt-get -o Acquire::Check-Valid-Until=false update && apt-get install -y supervisor

# Copy the supervisor configuration file
COPY ./Media_Service/supervisord.conf /etc/supervisor/conf.d/supervisord.conf

COPY ./Media_Service/requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY ./Media_Service/app /app/app

# Use supervisor to run both processes
CMD ["/usr/bin/supervisord"]