import sqlite3

# Initialize the database
def init_db():
    conn = sqlite3.connect('farm_management.db')
    c = conn.cursor()
    
    # Create crops table
    c.execute('''CREATE TABLE IF NOT EXISTS crops (
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    quantity INTEGER,
                    last_watered DATE)''')
    
    # Create tasks table
    c.execute('''CREATE TABLE IF NOT EXISTS tasks (
                    id INTEGER PRIMARY KEY,
                    description TEXT NOT NULL,
                    due_date DATE)''')
    
    # Create cows table
    c.execute('''CREATE TABLE IF NOT EXISTS cows (
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    breed TEXT NOT NULL,
                    birth_date DATE,
                    last_milked DATE)''')
    
    # Create milk production table
    c.execute('''CREATE TABLE IF NOT EXISTS milk_production (
                    id INTEGER PRIMARY KEY,
                    cow_id INTEGER,
                    date DATE,
                    quantity REAL,
                    FOREIGN KEY (cow_id) REFERENCES cows(id))''')
    
    # Create feed schedule table
    c.execute('''CREATE TABLE IF NOT EXISTS feed_schedule (
                    id INTEGER PRIMARY KEY,
                    cow_id INTEGER,
                    feed_type TEXT NOT NULL,
                    feed_time DATE,
                    quantity REAL,
                    FOREIGN KEY (cow_id) REFERENCES cows(id))''')
    
    conn.commit()
    conn.close()

# Add a crop
def add_crop(name, quantity, last_watered):
    conn = sqlite3.connect('farm_management.db')
    c = conn.cursor()
    c.execute('INSERT INTO crops (name, quantity, last_watered) VALUES (?, ?, ?)', 
              (name, quantity, last_watered))
    conn.commit()
    conn.close()

# List all crops
def list_crops():
    conn = sqlite3.connect('farm_management.db')
    c = conn.cursor()
    c.execute('SELECT * FROM crops')
    crops = c.fetchall()
    conn.close()
    return crops

# Add a task
def add_task(description, due_date):
    conn = sqlite3.connect('farm_management.db')
    c = conn.cursor()
    c.execute('INSERT INTO tasks (description, due_date) VALUES (?, ?)', 
              (description, due_date))
    conn.commit()
    conn.close()

# List all tasks
def list_tasks():
    conn = sqlite3.connect('farm_management.db')
    c = conn.cursor()
    c.execute('SELECT * FROM tasks')
    tasks = c.fetchall()
    conn.close()
    return tasks

# Add a cow
def add_cow(name, breed, birth_date, last_milked):
    conn = sqlite3.connect('farm_management.db')
    c = conn.cursor()
    c.execute('INSERT INTO cows (name, breed, birth_date, last_milked) VALUES (?, ?, ?, ?)', 
              (name, breed, birth_date, last_milked))
    conn.commit()
    conn.close()

# List all cows
def list_cows():
    conn = sqlite3.connect('farm_management.db')
    c = conn.cursor()
    c.execute('SELECT * FROM cows')
    cows = c.fetchall()
    conn.close()
    return cows

# Add milk production record
def add_milk_production(cow_id, date, quantity):
    conn = sqlite3.connect('farm_management.db')
    c = conn.cursor()
    c.execute('INSERT INTO milk_production (cow_id, date, quantity) VALUES (?, ?, ?)', 
              (cow_id, date, quantity))
    conn.commit()
    conn.close()

# List all milk production records
def list_milk_production():
    conn = sqlite3.connect('farm_management.db')
    c = conn.cursor()
    c.execute('SELECT * FROM milk_production')
    records = c.fetchall()
    conn.close()
    return records

# Add feed schedule
def add_feed_schedule(cow_id, feed_type, feed_time, quantity):
    conn = sqlite3.connect('farm_management.db')
    c = conn.cursor()
    c.execute('INSERT INTO feed_schedule (cow_id, feed_type, feed_time, quantity) VALUES (?, ?, ?, ?)', 
              (cow_id, feed_type, feed_time, quantity))
    conn.commit()
    conn.close()

# List all feed schedules
def list_feed_schedules():
    conn = sqlite3.connect('farm_management.db')
    c = conn.cursor()
    c.execute('SELECT * FROM feed_schedule')
    schedules = c.fetchall()
    conn.close()
    return schedules

