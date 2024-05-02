# Data Logger with Node.js Server Backend

This project combines an Arduino microcontroller with a DHT sensor to collect temperature and humidity data, and a Node.js backend to store and visualize the data. The Arduino reads sensor data and sends it to the Node.js server over a serial connection, where it is stored and can be accessed through a web interface.

## Quick Note

- Please note the server setup is in a different [repository]([https://github.com/Mevan-Solanga/DataLog-Backend](https://github.com/Mevan-Solanga/TemperatureLogger-Frontend)

## Features

- Read temperature and humidity data from a DHT sensor connected to an Arduino board.
- Send sensor data from Arduino to a Node.js server via serial communication.
- Store data in a database for future analysis and visualization.
- Provides a web interface to view and interact with collected data.
- Provided a web interface with current data, a data graph, and max temperature reading all developed using vanilla js, css and html

### Hardware Used

- Arduino board (e.g., Arduino Uno, Arduino Nano)
- DHT sensor (e.g., DHT11, DHT22)
- Wires for connections

### Software

- PlatformIO VS Code IDE: for developing and uploading code to the Arduino board
- Node.js: for creating the backend server
- Express.js: for handling HTTP requests

## Setup

1. **Arduino Setup**: Connect the DHT sensor to the Arduino board and upload the provided Arduino sketch (`sensor_readings.ino`) to read sensor data and send it over serial communication.

2. **Node.js Setup**: Set up a Node.js server to receive data from the Arduino over serial communication, and serve it to the web interface.

3. **Web Interface**: Create a web interface using HTML, CSS, and JavaScript (with a framework like React.js or Vue.js if preferred) to display the collected sensor data in real-time or with historical data visualization.

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
