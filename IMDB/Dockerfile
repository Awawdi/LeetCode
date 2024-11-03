FROM python:3.9-slim

WORKDIR /imdb_app

COPY ./IMDB/requirements.txt /imdb_app/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /imdb_app

EXPOSE 5000

CMD ["python", "movie_search_cache_flask.py"]
