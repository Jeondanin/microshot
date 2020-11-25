FROM python:3.7.3-slim-stretch
ENV PYTHONBUFFERED=1
ENV PYTHONHASHSEED=random

RUN mkdir /opt/app
WORKDIR /opt/app
COPY requirements.txt .
RUN pip install -r requirements.txt
RUN apt-get update && apt-get -y install libglib2.0-0; apt-get clean
RUN pip install opencv-contrib-python-headless
COPY . .

COPY /usr/local/lib/python3.6/dist-packages/torch .
COPY /usr/local/lib/python3.6/dist-packages/torch-1.5.0.dist-info .
COPY /usr/local/lib/python3.6/dist-packages/torchvision .
COPY /usr/local/lib/python3.6/dist-packages/torchvision-0.6.0.dist-info .

# RUN yes |cp -arpf /opt/app/site-packages/. /usr/local/lib/python3.7/site-packages
# RUN rm -rf /opt/app/site-packages
EXPOSE 8000
ENTRYPOINT ["gunicorn", "-b", ":8000","-t", "180", "-w" ,"4",  "segmentationSetting.wsgi:application"]
# ENTRYPOINT ["python","manage.py", "runserver", "0.0.0.0:8000"]
