FROM nginxinc/nginx-unprivileged:1.29-alpine

COPY src/index.html /usr/share/nginx/html/index.html
COPY src/default.conf /etc/nginx/conf.d/default.conf

EXPOSE 8080
