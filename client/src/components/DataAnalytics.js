import React, { useEffect, useState } from 'react';

export default function DataAnalytics() {
  const [sensorData, setSensorData] = useState([]);

  useEffect(() => {
    // Fetch sensor data on component mount
    const fetchSensorData = async () => {
      try {
        const response = await fetch('http://127.0.0.1:8000/sensors/readings/');
        if (response.ok) {
          const data = await response.json();
          setSensorData(data);
        } else {
          console.error('Error fetching sensor data');
        }
      } catch (error) {
        console.error('Error fetching sensor data:', error);
      }
    };

    fetchSensorData();
  }, []);

  return (
    <div className="data-analytics">
      <h2>Sensor Data Analytics</h2>
      <div className="data-list">
        {sensorData.map((item, index) => (
          <div key={index} className="data-item">
            <p><strong>Timestamp:</strong> {item.timestamp}</p>
            <p><strong>DHT Humidity:</strong> {item.dht_humidity}</p>
            <p><strong>DHT Temperature:</strong> {item.dht_temperature}</p>
            <p><strong>Soil Moisture:</strong> {item.soil_moisture}</p>
            <p><strong>Rain:</strong> {item.rain}</p>
            <p><strong>Light:</strong> {item.light}</p>
            <p><strong>Analog Temperature:</strong> {item.analog_temperature}</p>
            <p><strong>Digital Temperature:</strong> {item.digital_temperature}</p>
          </div>
        ))}
      </div>
    </div>
  );
}
