FROM node:6.4.0
RUN apt-get update || : && apt-get install python -y
RUN apt-get install python3-pip -y

WORKDIR app/src

COPY ./requirements.txt ./
RUN pip3 install -r requirements.txt
COPY ./ ./
CMD ["uvicorn","main:app","--port","3002","--host","0.0.0.0"]