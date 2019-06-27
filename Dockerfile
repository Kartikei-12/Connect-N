# Docker Image currently does not support API
# Follow below commands before launching docker
# git clone https://github.com/Kartikei-12/Connect-N
# cd Connect-N-master
# docker build -t connect-n .
# docker run -i connect-n

FROM python:3.7

WORKDIR /project
COPY ./requirements.txt /project/requirements.txt
RUN pip install -r requirements.txt
COPY . /project
CMD ["python", "/project/main.py"]
