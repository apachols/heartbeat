'''
   chart.py - chart heartrate data from csv

   setup steps OSX:

   * install pyenv

        brew install pyenv

   * install python 3.5

        PYTHON_CONFIGURE_OPTS="--enable-framework" pyenv install 3.5.4

   * install matplotlib

        pip install matplotlib

   * basic idea stolen from here:

        https://stackoverflow.com/questions/13545388/plot-data-from-csv-file-with-matplotlib

   * links that made this setup work

        https://github.com/pyenv/pyenv
        https://matplotlib.org/faq/osx_framework.html
        https://python-graph-gallery.com/120-line-chart-with-matplotlib/
'''

import matplotlib as mpl
import numpy as np
import matplotlib.pyplot as plt

import os
import sys
path = os.path.dirname(os.path.realpath(__file__))
if len(sys.argv) == 1:
    raise ValueError('Missing filename')

from scipy.signal import medfilt

'''
  THIS IS THE SENSOR WE ARE USING:
    http://embedded-lab.com/blog/easy-pulse-version-1-1-sensor-overview-part-1/

  Apparently the data is 40 samples / second, no matter what the CSV says
'''

# Make a chart for a csv file from the data directory
file_name = path + '/data/' + sys.argv[1]

data = np.genfromtxt(
    file_name,
    dtype=[('myint','i8'),('myfloat','f8')],
    delimiter=',',
    skip_header=1,
    names=['x', 'y']
)

fig = plt.figure()

ax1 = fig.add_subplot(111)

ax1.set_title("Heartbeat Data")
ax1.set_xlabel('time')
ax1.set_ylabel('reading')

x = data['x']
y = data['y']

# This is a moving average (median) filter that smooths out the data.
# The default for the second argument is 3; this argument needs to be ODD not EVEN.
yfilt = medfilt(y, 15)

ax1.plot(x, yfilt, color='r', label='the data')

plt.show()

# import ipdb; ipdb.set_trace()
