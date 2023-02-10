FROM python:3.8

## Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

RUN apt-get -y update

RUN mkdir /project
ADD . /project
WORKDIR /project

RUN python -m pip install --upgrade pip
RUN pip install -r requirments.txt

# 컨테이너가 수행될 때 entrypoint가 실행
ENTRYPOINT ["sh", "./entrypoint.sh"]