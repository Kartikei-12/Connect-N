# Language Support
FROM python:latest

# The first parameter 'main.py' is the name of the file on the host.
# The second parameter '/' is the path where to put the file on the image.
# Here we put the file at the image root folder.

WORKDIR /project
ADD ./requirements.txt /project/requirements.txt
RUN pip install -r requirements.txt
ADD . /project
CMD ["python", "/project/main.py"]
