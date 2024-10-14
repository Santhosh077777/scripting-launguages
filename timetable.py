timetable = [
    ["open elective", "open elective","business intelligence", "operating system",  "networking lab", "networking lab","networking lab"], 
    ["training", "training", "training", "training", "training", "training","training"], 
    ["training", "training", "training", "training","training", "training","training"], 
    ["design thinking lab", "design thinking lab", "operating system", "design thinking", "startup and entrepreneurship", "data communication and networks","operating system"], 
    ["data communication and networks","startup and entrepreneurship","mechine learning lab","mechine learning lab","operating system","business intelligence","design thinking"], 
    ["mechine learning lab","mechine learning lab","data communication and networks","data communication and networks","business intelligence","startup and entrepreneurship", "mentor/NPTEL"], 
    ["No classes", "No classes", "No classes", "No classes", "Lunch", "No classes", "No classes"] 
]
if __name__ == "__main__":
    day = int(input("Enter the day (0 for Monday, 6 for Sunday): "))
    hour = int(input("Enter the hour (0 to 6 for periods 1 to 7): "))
    subject = timetable[day][hour]
    print(f"Period {hour + 1}: {subject}")