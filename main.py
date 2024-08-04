from database import *

def main():
    init_db()
    
    # Example usage for crops
    add_crop('Tomato', 100, '2024-08-04')
    add_task('Water the crops', '2024-08-05')
    
    # Example usage for dairy farming
    add_cow('Bella', 'Holstein', '2020-05-10', '2024-08-03')
    add_milk_production(1, '2024-08-04', 20.5)
    add_feed_schedule(1, 'Hay', '2024-08-04 08:00:00', 5.0)
    
    print("Crops:")
    for crop in list_crops():
        print(crop)
    
    print("\nTasks:")
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
