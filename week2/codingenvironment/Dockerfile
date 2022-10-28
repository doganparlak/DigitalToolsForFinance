FROM python:3.7
 
WORKDIR /usr/src/app

# copy all the files to the container
COPY . .
#RUN mkdir -p /root/.config/matplotlib
#RUN echo "backend : Agg" > /root/.config/matplotlib/matplotlibrc

RUN pip install pandas matplotlib==2.2.4

CMD ["python", "./main.py"]