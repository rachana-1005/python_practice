#3.L3
def show_details(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}:{value}")
show_details(name="Rachana",age=20,city="koppa")       
