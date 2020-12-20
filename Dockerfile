FROM python:3.8-slim-buster
ADD ./requirements.txt /app/requirements.txt

RUN set -ex \
    && apt-get update \
    && apt-get install -y python3-pip python3-dev libpq-dev curl build-essential\
       libtiff5-dev zlib1g-dev libfreetype6-dev liblcms2-dev \
       libwebp-dev tcl8.6-dev tk8.6-dev python-tk \
    && pip3 install virtualenv \
    && virtualenv env \
    && /env/bin/pip install --upgrade pip \
    && /env/bin/pip install --no-cache-dir -r /app/requirements.txt

ADD . /app
WORKDIR /app

ENV VIRTUAL_ENV /env
ENV PATH /env/bin:$PATH

EXPOSE 8000

CMD ["gunicorn", "--bind", ":8000", "--workers", "3", "educate_me.wsgi:application"]