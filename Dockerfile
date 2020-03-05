FROM python:3.7.6
WORKDIR /usr/src
RUN ls
COPY . .
RUN pip install -r requirements.txt
RUN ls models -r
ENTRYPOINT ["python"]
CMD ["server.py"]