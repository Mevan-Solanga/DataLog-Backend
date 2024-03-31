#include <Arduino.h>
#include <DHT.h>

#define DHTPIN 2      // Define the pin number where your DHT sensor is connected
#define DHTTYPE DHT11 // Define the type of DHT sensor you're using (DHT11, DHT21, DHT22)

DHT dht(DHTPIN, DHTTYPE);

void setup()
{
  Serial.begin(9600);
}

void loop()
{
  int chk = dht.read();
  Serial.print("Temperature = ");
  Serial.println(dht.readTemperature());
  Serial.print("Humidity: ");
  Serial.println(dht.readHumidity());
  delay(1000);
}
