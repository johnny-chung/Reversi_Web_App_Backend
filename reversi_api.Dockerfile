#reversi api dockerfile

FROM ubuntu

COPY ./app /app

WORKDIR /app

RUN apt update && apt -y install curl

RUN apt update && apt -y install python3 python3-pip && apt install -y nginx

RUN python3 -m pip install Flask

RUN python3 -m pip install Flask-Cors


RUN pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu

RUN python3 -m pip install gunicorn


# Set up Nginx
COPY ./nginx.conf /etc/nginx/sites-available/default

# Expose the port that Gunicorn will run on
EXPOSE 8000

# Start Gunicorn to run the Flask app
CMD ["gunicorn", "-w", "2", "-b", "0.0.0.0:8000", "app:app"]