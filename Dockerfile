FROM python:3.7.6
COPY . /

RUN pip install -r requirements.txt
RUN ls -la /
ENTRYPOINT ["python"]
CMD ["server.py"]