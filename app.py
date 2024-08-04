from flask import Flask, render_template, request, jsonify, redirect, url_for
from database import *

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/crops', methods=['GET', 'POST'])
def crops():
    if request.method == 'POST':
        name = request.form['name']
        quantity = request.form['quantity']
        last_watered = request.form['last_watered']
        add_crop(name, quantity, last_watered)
        return redirect(url_for('crops'))
    crops_list = list_crops()
    return render_template('crops.html', crops=crops_list)

@app.route('/tasks', methods=['GET', 'POST'])
def tasks():
    if request.method == 'POST':
        description = request.form['description']
        due_date = request.form['due_date']
        add_task(description, due_date)
        return redirect(url_for('tasks'))
    tasks_list = list_tasks()
    return render_template('tasks.html', tasks=tasks_list)

@app.route('/cows', methods=['GET', 'POST'])
def cows():
    if request.method == 'POST':
        name = request.form['name']
        breed = request.form['breed']
        birth_date = request.form['birth_date']
        last_milked = request.form['last_milked']
        add_cow(name, breed, birth_date, last_milked)
        return redirect(url_for('cows'))
    cows_list = list_cows()
    return render_template('cows.html', cows=cows_list)

@app.route('/milk_production', methods=['GET', 'POST'])
def milk_production():
    if request.method == 'POST':
        cow_id = request.form['cow_id']
        date = request.form['date']
        quantity = request.form['quantity']
        add_milk_production(cow_id, date, quantity)
        return redirect(url_for('milk_production'))
    production_list = list_milk_production()
    return render_template('milk_production.html', productions=production_list)

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
    for task in list_tasks():
        print(task)
    
    print("\nCows:")
    for cow in list_cows():
        print(cow)
    
    print("\nMilk Production:")
    for record in list_milk_production():
        print(record)
    
    print("\nFeed Schedules:")
    for schedule in list_feed_schedules():
        print(schedule)

if __name__ == "__main__":
    main()
