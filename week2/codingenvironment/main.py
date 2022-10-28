import os
import matplotlib
if os.environ.get('DISPLAY','') == '':
    print('no display found. Using non-interactive Agg backend')
    matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('data/coding-environment-exercise.csv')
st_name=data['student']
marks=data['mark']
x=list(st_name)
y=list(marks)
print(data)
out_path = '/output/your_filename.png'
plt.plot(x,y)
plt.savefig("test3.png",format="png")


