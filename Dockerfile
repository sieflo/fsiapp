FROM python:latest

RUN useradd mycalendar

WORKDIR /home/mycalendar

COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN python -m venv venv
RUN venv/bin/pip install -r requirements.txt
RUN venv/bin/pip install gunicorn pymysql cryptography

COPY app app
COPY migrations migrations
COPY calendar.py config.py boot.sh ./
COPY wsgi.py wsgi.py
RUN chmod a+x boot.sh

ENV FLASK_APP calendar.py

RUN chown -R mycalendar:mycalendar ./
USER mycalendar

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]
