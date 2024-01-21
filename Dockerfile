# syntax=docker/dockerfile:1
FROM python:3.11

# Creating the user
RUN addgroup --system dockeruser && adduser --system --group dockeruser

# Diasbles generation of pyc files
ENV PYTHONDONTWRITEBYTECODE 1
# stdout and stderr streams are not buffered and sent straight to your terminal
ENV PYTHONUNBUFFERED 1
ENV ENV=pro

ENV APP_HOME=/txatxilife
ENV LOG_HOME=/log
# ENV APP_USER=appuser

RUN mkdir $APP_HOME
RUN mkdir $LOG_HOME

WORKDIR $APP_HOME

COPY requirements.txt $APP_HOME/
RUN pip install --upgrade pip

RUN pip install -r requirements.txt
COPY . /txatxilife/


# Changing ownership of all files and folders in work dir to user
RUN chown -R dockeruser:dockeruser $APP_HOME

# Changing to user
USER dockeruser

#CMD ["gunicorn", "--config", "gunicorn-cfg.py", "core.wsgi"]
CMD ["python", "core/manage.py", "runserver", "0.0.0.0:8000"]


