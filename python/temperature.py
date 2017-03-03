from serial import Serial

ser = serial.Serial(
    port = '/dev/ttyUSB0',
    baudrate = 9600,
    bytesize = serial.EIGHTBITS,
    parity = serial.PARITY_NONE,
    stopbits = serail.STOPBITS_one
)

print ser.read(size=8)
ser.close

