FROM python:2-alpine3.7

WORKDIR /root
RUN pip install falcon requests six
COPY forward.py /root
CMD ["python","/root/forward.py"]