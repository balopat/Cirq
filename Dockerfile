FROM ubuntu:16.04

ADD ./dev_tools/conf/apt-list-dev-tools.txt ./

# Install dependencies.
RUN DEBIAN_FRONTEND=noninteractive apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y \
     python3-pip python3-tk texlive-latex-base latexmk git emacs vim locales

RUN cat apt-list-dev-tools.txt | xargs apt-get install -y

# Configure UTF-8 encoding.
RUN sed -i -e 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen && locale-gen
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8 

RUN apt-get install -y software-properties-common
RUN add-apt-repository ppa:deadsnakes/ppa
RUN apt update
RUN apt-get install -y python3.7
RUN apt-get install -y python3.7-dev

# Make python3 default
RUN rm -f /usr/bin/python && ln -s /usr/bin/python3.7 /usr/bin/python

ADD ./requirements.txt ./
ADD ./dev_tools/conf/pip-list-dev-tools.txt ./

RUN python -m pip install pip wheel --upgrade
RUN python -m pip install -r requirements.txt -r pip-list-dev-tools.txt

