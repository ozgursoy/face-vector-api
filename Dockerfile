FROM python:3.5
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
RUN pip install --no-dependencies face_recognition face_recognition_models
ENTRYPOINT ["python"]
CMD ["app.py"]