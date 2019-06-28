FROM python:3-alpine

WORKDIR /root
RUN pip install falcon\<2.0.0 requests
COPY forward.py /root
CMD ["python","/root/forward.py"]
