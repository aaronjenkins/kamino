FROM lgatica/python-alpine
WORKDIR /kamino
COPY ./ /kamino
RUN python kamino.py