FROM python:3.10-alpine
RUN apk add python3
RUN pip install streamlit
COPY tik-tak-toe.py .

ENTRYPOINT ["streamlit","run","tik-tak-toe.py"]
