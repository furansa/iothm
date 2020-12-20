DROP TABLE IF EXISTS sensor_types;
CREATE TABLE sensor_types (
    id SERIAL PRIMARY KEY,
    description VARCHAR(256) UNIQUE NOT NULL
);
COMMENT ON TABLE sensor_types IS 'Domain table for types of sensors';

DROP TABLE IF EXISTS sensors;
CREATE TABLE sensors (
    id SERIAL PRIMARY KEY,
    type INTEGER NOT NULL,
    description VARCHAR(256) NOT NULL,
    FOREIGN KEY (type) REFERENCES sensor_types(id) ON DELETE CASCADE
);
COMMENT ON TABLE sensors IS 'Registry table for sensors';

DROP TABLE IF EXISTS devices;
CREATE TABLE devices (
    id SERIAL PRIMARY KEY,
    description VARCHAR(256) UNIQUE NOT NULL
);
COMMENT ON TABLE devices IS 'Registry table for devices';

DROP TABLE IF EXISTS devices_sensors;
CREATE TABLE devices_sensors (
    id SERIAL PRIMARY KEY,
    device INTEGER NOT NULL,
    sensor INTEGER NOT NULL,
    FOREIGN KEY (device) REFERENCES devices(id) ON DELETE CASCADE,
    FOREIGN KEY (sensor) REFERENCES sensors(id) ON DELETE CASCADE,
    UNIQUE (device, sensor)
);
COMMENT ON TABLE devices_sensors IS 'Relationship table for devices and sensors';

DROP TABLE IF EXISTS event_types;
CREATE TABLE event_types (
    id SERIAL PRIMARY KEY,
    description VARCHAR(256) UNIQUE NOT NULL
);
COMMENT ON TABLE event_types IS 'Domain table for types of events';

DROP TABLE IF EXISTS events;
CREATE TABLE events (
    id SERIAL PRIMARY KEY,
    type INTEGER NOT NULL,
    timestamp TIMESTAMP NOT NULL DEFAULT NOW(),
    device_sensor INTEGER NOT NULL,
    value VARCHAR(128),
    FOREIGN KEY (type) REFERENCES event_types(id) ON DELETE CASCADE,
    FOREIGN KEY (device_sensor) REFERENCES devices_sensors(id) ON DELETE CASCADE
);
COMMENT ON TABLE events IS 'Registry table for events';

INSERT INTO sensor_types (description) VALUES ('Temperature');
INSERT INTO sensor_types (description) VALUES ('Temperature and humidity');
INSERT INTO sensors (type, description) VALUES (1, 'LM35DZ');
INSERT INTO sensors (type, description) VALUES (2, 'DHT11');
INSERT INTO devices (description) VALUES ('ESP32');
INSERT INTO devices_sensors (device, sensor) VALUES (1, 1);
INSERT INTO event_types (description) VALUES ('New measurement value');
INSERT INTO event_types (description) VALUES ('Measurement value above threshold');
INSERT INTO event_types (description) VALUES ('Measurement value below threshold');
INSERT INTO events (type, device_sensor, value) VALUES (1, 1, '20.1');
INSERT INTO events (type, device_sensor, value) VALUES (1, 1, '20.2');
INSERT INTO events (type, device_sensor, value) VALUES (1, 1, '20.3');
INSERT INTO events (type, device_sensor, value) VALUES (1, 1, '20.0');
