FROM debian

### So logging/io works reliably w/Docker
ENV PYTHONUNBUFFERED=1
### UTF Python issue for Click package (pipenv dependency)
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8
### Need to explicitly set this so `pipenv shell` works
ENV SHELL=/bin/bash

### Basic Python dev dependencies
RUN apt-get update && \
  apt-get upgrade -y && \
  apt-get install python3-pip curl nano -y && \
  pip3 install pandas && \
  pip3 install matplotlib && \
  pip3 install seaborn && \
  pip3 install sklearn && \
  pip3 install -i https://test.pypi.org/simple/ lambdata-pkg-nrvanwyck && \
  python3 -c "import lambdata_pkg_nrvanwyck; print('Success!')"