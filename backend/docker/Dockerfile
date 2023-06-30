FROM ubuntu:20.04 as python-base

ENV LC_ALL=C.UTF-8 \
    LANG=C.UTF-8 \
    TZ=Europe/Rome

RUN mkdir /code

WORKDIR /code

RUN \
   apt-get -y upgrade && \
   apt -y clean && \
   apt-get -y update && \
   apt-get install -y gcc tini && \
   apt-get install -y --no-install-recommends --yes python3 && \
   apt-get install -y --no-install-recommends python3-pip && \
   apt-get install -y software-properties-common && \
   apt-get install -y python3-gdal && \
   add-apt-repository ppa:ubuntugis/ppa && \
   apt-get install -y python-numpy gdal-bin libgdal-dev && \
   apt-get install -y --no-install-recommends gdal-bin && \
   apt-get install -y --no-install-recommends gdal-bin && \
   apt-get install -y --no-install-recommends libgdal-dev && \
   apt-get install -y python3-dev libcairo2-dev pkg-config && \
   apt-get install -y libpq-dev && \
   apt-get install --reinstall build-essential -y && \
   apt-get clean && apt-get autoremove -y && \
   rm -rf /var/lib/apt-get/lists/* && \
   pip3 install GDAL

ARG CPLUS_INCLUDE_PATH=/usr/include/gdal
ARG C_INCLUDE_PATH=/usr/include/gdal

COPY . /code

RUN pip3 install -r requirements.txt && \
    pip3 install --upgrade requests && \
    pip3 install numpy -U \
