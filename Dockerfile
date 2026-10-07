FROM nginxinc/nginx-unprivileged:1.29-alpine

USER root
RUN apk upgrade --no-cache
USER 101

COPY src/index.html /usr/share/nginx/html/index.html
COPY src/default.conf /etc/nginx/conf.d/default.conf

EXPOSE 8080
