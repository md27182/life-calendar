import serial
import time

# Open grbl serial port
s = serial.Serial('COM3', 115200) # or is it 9600?

# Wake up grbl
s.write('\r\n\r\n'.encode())
time.sleep(2)   # Wait for grbl to initialize 
s.flushInput()  # Flush startup text in serial input

while True:
    inp = input("Enter g-code: \n")
    if inp == 'exit':
        break
    else:
        print('Sending: ' + inp)
        s.write((inp + '\n').encode()) # Send g-code block to grbl
        grbl_out = s.readline().decode().strip() # Wait for grbl response with carriage return
        print(' : ' + grbl_out)

# # Stream g-code to grbl
# l = 'G91 G0 X1\n' # Put g-code here


# # Wait here until grbl is finished to close serial port and file.
# input("  Press <Enter> to exit and disable grbl.") 

# Close file and serial port
s.close()