import os  
import can
import time

os.system('sudo ip link set can0 type can bitrate 500000')
os.system('sudo ifconfig can0 up')
can0 = can.interface.Bus(channel = 'can0', bustype = 'socketcan_ctypes')# socketcan_native

msg = can.Message(arbitration_id=0x2A01, data=[0, 0, 0, 0xFE, 0, 0, 0, 0], extended_id=True)
can0.send(msg)
time.sleep(1)

msg = can.Message(arbitration_id=0x2A01, data=[0, 0, 0, 0, 0, 0, 0, 0], extended_id=True)
can0.send(msg)
time.sleep(0.1)

#os.system('sudo ifconfig can0 down')
