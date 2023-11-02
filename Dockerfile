FROM python:3.10.13
ADD . /emergent_experiments
WORKDIR /emergent_experiments
RUN python3 -m pip install --upgrade pip
RUN pip install -r requirements.txt
