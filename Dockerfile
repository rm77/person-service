FROM python:2.7
ADD Persons_Model.py /code
ADD Service.py /code
ADD requirements.txt /code
WORKDIR /code
RUN pip install -r requirements.txt
CMD python Service.py
