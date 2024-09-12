import pandas as pd
import random
import time
import sqlite3

excel_file = "Task.xlsx"
data = pd.read_excel(excel_file)

def generate_value(auto_generated_range):
    if isinstance(auto_generated_range, str):
        min_val, max_val = map(float, auto_generated_range.split(" to "))
        return random.uniform(min_val, max_val)
    return auto_generated_range

machines = [{"machine_id": 81258856, "machine_name": "EMXP1", "tool_capacity": 24} for _ in range(20)]
axes = ['X', 'Y', 'Z', 'A', 'C']

def generate_machine_data():
    generated_data = []
    for machine in machines:
        for axis in axes:
            tool_offset = generate_value("5 to 40")
            feedrate = generate_value("0 to 20000")
            tool_in_use = random.randint(1, machine["tool_capacity"])
            
            generated_data.append({
                "machine_id": machine["machine_id"],
                "machine_name": machine["machine_name"],
                "axis": axis,
                "tool_offset": tool_offset,
                "feedrate": feedrate,
                "tool_in_use": tool_in_use,
                "timestamp": time.strftime('%Y-%m-%d %H:%M:%S')
            })
    
    return generated_data

data = generate_machine_data()

conn = sqlite3.connect('machine_data.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS machine_data (
    machine_id INTEGER,
    machine_name TEXT,
    axis TEXT,
    tool_offset REAL,
    feedrate REAL,
    tool_in_use INTEGER,
    timestamp DATETIME
)
''')
conn.commit()

def insert_data(data):
    for record in data:
        cursor.execute("""
            INSERT INTO machine_data (machine_id, machine_name, axis, tool_offset, feedrate, tool_in_use, timestamp)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (record['machine_id'], record['machine_name'], record['axis'], record['tool_offset'], 
              record['feedrate'], record['tool_in_use'], record['timestamp']))
    conn.commit()

insert_data(data)
conn.close()
