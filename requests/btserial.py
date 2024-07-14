
# Standard Library
import serial

# ID
XACCL = 0
YACCL = 1
ZACCL = 2
XGYRO = 3
YGYRO = 4
ZGYRO = 5
XMAG = 6
YMAG = 7
ZMAG = 8
ROLL = 9
PITCH = 10
YAW = 11

# Bluetooth Serial Init
UART_TIMEOUT = 5 #[s]
COMPORT = 'COM8'
BAUDRATE = 115200

# Serial Instantiate
btser = serial.Serial(port=COMPORT, baudrate=BAUDRATE, bytesize=8, stopbits=serial.STOPBITS_ONE, parity=serial.PARITY_NONE, timeout=UART_TIMEOUT)

def btserial():
    get_data = []
    for i in range(12):
        rdata = btser.readline()
        get_str = rdata[0:len(rdata)-2].decode()
        get_data.append(float(get_str.replace('"','')))
        
    return get_data

# while True:
#     data = btserial()
#     print(data)