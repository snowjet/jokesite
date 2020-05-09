FROM registry.access.redhat.com/ubi8/python-36 
LABEL description="Jokesite"
MAINTAINER chris

USER root
RUN mkdir -p /opt/app-root/src && chown -R 1001:0 /opt/app-root/src
USER 1001 
WORKDIR /opt/app-root/src
COPY requirements.txt ./
RUN pip install --upgrade pip --no-cache-dir -r requirements.txt
RUN mkdir /opt/app-root/src
WORKDIR /opt/app-root/src
ADD . ./

ENV PORT 8080
EXPOSE 8080

CMD [ "/opt/app-root/src/start-application.sh"]
