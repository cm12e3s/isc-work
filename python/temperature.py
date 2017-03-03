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


    
