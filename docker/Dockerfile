FROM ubuntu
# work dir
WORKDIR /opt/cloudbot
# Expose volume
VOLUME ["/opt/cloudbot/db"]
# install build deps
RUN  apt-get update && \
     apt-get install -y software-properties-common && \
     add-apt-repository ppa:deadsnakes/ppa && \
     apt-get update && \
     apt-get install -y python3.6-dev git libenchant-dev libxml2-dev libxslt-dev zlib1g-dev gcc curl nano && \
     rm -rf /var/lib/apt/lists/*
# install pip
RUN curl -Ls https://bootstrap.pypa.io/get-pip.py | python3.6
# add stuff
ADD . /opt/cloudbot
# install deps
RUN pip install -r requirements.txt
# add config
ADD docker/config.json /opt/cloudbot/config.json
# Start
CMD python3.6 -m cloudbot
