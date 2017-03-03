from datetime import datetime
import serial, io

outfile = 'serial-temperature.tsv'

ser = serial.Serial(
    port = '/dev/ttyUSB0',
    baudrate = 9600,
    bytesize = serial.EIGHTBITS,
    parity = serial.PARITY_NONE,
    stopbits = serial.STOPBITS_ONE
)

sio = io.TextIOWrapper(
    io.BufferedRWPair (ser, ser, 1),
    encoding = 'ascii', newline='\r'
)

with open (outfile, 'a') as f: #appends to exsisting file
    while ser.isOpen():
        datastring = sio.readline()
        f.write (datetime.utcnow().isoformat() + '\t' + datastring + '\n')
        f.flush() # included to force the system to write to disk.

ser.close()

import numpy as py

INFILE = 'serial-temperature.tsv'
outfile = 'sensor-data.nc'
from tsv import reader

times = []
temps = []

#function to convert from text file format to numbers
def convert_time(tm):
    tm = datetime.strptime(tm, "Y-%m-%dT%H::%M:%S.%f")
    return tm

def convert_temp(temp):
    value = temp.strip("+").strip("C").lstrip("0")
    return float(value) + 273.15


with open(infile, 'rb') as tsvfile:
    tsvreader = reader(tsvfile, delimiter = '\t')
    for row in tsvreader:
        time.append(convert_time(row[0]))
        temps.append(convert_temp(row[1]))

