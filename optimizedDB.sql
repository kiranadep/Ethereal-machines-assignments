USE MACHINE_DATA;
CREATE TABLE Machines (
    machine_id INTEGER PRIMARY KEY,
    machine_name TEXT,
    tool_capacity INTEGER
);

CREATE TABLE Axes (
    axis_id INTEGER PRIMARY KEY,
    axis_name TEXT
);

CREATE TABLE Field_Values (
    value_id INTEGER PRIMARY KEY,
    machine_id INTEGER,
    axis_id INTEGER,
    field_name TEXT,
    value REAL,
    timestamp DATETIME,
    FOREIGN KEY (machine_id) REFERENCES Machines (machine_id),
    FOREIGN KEY (axis_id) REFERENCES Axes (axis_id)
);

INSERT INTO Machines (machine_id, machine_name, tool_capacity) VALUES (81258856, 'EMXP1', 24);

INSERT INTO Axes (axis_name) VALUES ('X'), ('Y'), ('Z'), ('A'), ('C');

INSERT INTO Field_Values (machine_id, axis_id, field_name, value, timestamp)
VALUES (81258856, 1, 'tool_offset', 20.5, '2024-09-09 10:00:00'),
       (81258856, 1, 'feedrate', 15000, '2024-09-09 10:00:00'),
       (81258856, 1, 'tool_in_use', 5, '2024-09-09 10:00:00');

