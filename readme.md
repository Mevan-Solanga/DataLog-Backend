# Arduino Data Logger with Node.js Backend

This project combines an Arduino microcontroller with a DHT sensor to collect temperature and humidity data, and a Node.js backend to store and visualize the data. The Arduino reads sensor data and sends it to the Node.js server over a serial connection, where it is stored in a database and can be accessed through a web interface.

## Features

- Read temperature and humidity data from a DHT sensor connected to an Arduino board.
- Send sensor data from Arduino to a Node.js server via serial communication.
- Store data in a database for future analysis and visualization.
- Provide a web interface to view and interact with collected data.

## Components

### Hardware

- Arduino board (e.g., Arduino Uno, Arduino Nano)
- DHT sensor (e.g., DHT11, DHT22)
- Wires for connections
- Optional: Real-time clock (RTC) module for timestamping data

### Software

- PlatformIO VS Code IDE: for developing and uploading code to the Arduino board
- Node.js: for creating the backend server
- Express.js: for handling HTTP requests
- MongoDB or other database: for storing sensor data
- Chart.js or other visualization library: for displaying data on the web interface

## Setup

1. **Arduino Setup**: Connect the DHT sensor to the Arduino board and upload the provided Arduino sketch (`sensor_readings.ino`) to read sensor data and send it over serial communication.

2. **Node.js Setup**: Set up a Node.js server to receive data from the Arduino over serial communication, store it in a database, and serve it to the web interface.

3. **Database Setup**: Create a MongoDB database to store the sensor data. Configure the Node.js server to connect to the database and store incoming sensor readings.

4. **Web Interface**: Create a web interface using HTML, CSS, and JavaScript (with a framework like React.js or Vue.js if preferred) to display the collected sensor data in real-time or with historical data visualization.

## Usage

1. Connect the Arduino board with the DHT sensor to your computer via USB.

2. Start the Node.js server by running `node server.js` in the terminal.

3. Access the web interface in your browser to view the collected sensor data.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgements

- [PlatformIO VS Code IDE](https://platformio.org/platformio-ide)
- [Node.js](https://nodejs.org/)
- [Express.js](https://expressjs.com/)
- [MongoDB](https://www.mongodb.com/)
- [Chart.js](https://www.chartjs.org/)
