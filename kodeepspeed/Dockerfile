FROM python:3
ARG PROJECT_DIR="/kodeepspeed"
ENV PYTHONUNBUFFERED 1
COPY . ${PROJECT_DIR}
WORKDIR ${PROJECT_DIR}
COPY requirements.txt /work/
RUN pip install -r requirements.txt
COPY . /work/