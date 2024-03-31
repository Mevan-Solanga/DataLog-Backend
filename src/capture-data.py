import serial
import csv

# Define the serial port and baud rate
serial_port = 'COM7'  # Change this to match your Arduino's serial port
baud_rate = 9600

# Open the serial port
ser = serial.Serial(serial_port, baud_rate)

# Create and open the CSV file
with open('sensor_data.csv', 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['Temperature (°C)', 'Humidity (%)'])

    # Read data from the serial port indefinitely and write to the CSV file
    try:
        while True:
            line = ser.readline().decode().strip()
            if line.startswith('T ='):
                temperature = line.split('=')[1].split(' ')[1]
                humidity = line.split(',')[1].split('=')[1].split('%')[0]
                csv_writer.writerow([temperature, humidity])
    except KeyboardInterrupt:
        print('Data capture stopped.')

# Close the serial port
ser.close()
