FROM nginx:1.19.2

RUN rm /etc/nginx/conf.d/default.conf
COPY mead.conf /etc/nginx/conf.d/
COPY nginx.conf /etc/nginx/nginx.conf
