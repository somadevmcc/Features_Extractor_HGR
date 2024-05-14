# Use the latest Python Version as the base image
FROM python:3.11
RUN apt-get update \
    && apt-get -y install libpq-dev gcc 
    

# Library components
RUN apt-get install -y --fix-missing\
    libavformat-dev libavcodec-dev libavdevice-dev --fix-missing\
    libavutil-dev libswscale-dev libswresample-dev libavfilter-dev --fix-missing

RUN apt-get install -y --fix-missing \
    cmake \
    git \
    wget \
    ffmpeg \
    ninja-build
# Setup the working directory for the container
WORKDIR /code

# Copy the requirements file to the container
COPY requirements.txt requirements.txt

# Install the Python dependencies using Python 
RUN pip install --no-cache-dir -r requirements.txt
RUN pip3 install "git+https://github.com/philferriere/cocoapi.git#egg=pycocotools&subdirectory=PythonAPI"
# Copy the rest of the application code to the container
COPY . .
ENV FLASK_APP=app.py
# Setup the command to run when the container starts
#CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
CMD [ "python3", "-m" , "main"]