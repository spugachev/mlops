FROM python:3.8

RUN mkdir -p /root/.streamlit
COPY requirements.txt ./requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 8501
CMD streamlit run app.py