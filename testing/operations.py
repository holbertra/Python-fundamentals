
def traffic_light_choice(car, light):
    car_command = ""

    #- Moving Car
    if car == "moving":
        if light == "red":
            car_command = "stop"
        elif light == "yellow":
            car_command = "stop"
        elif light == "green":
            car_command = "go"
        else:
            print("Light is broken")

    #- Stopped Car
    elif car == "stopped":
        if light == "red":
            car_command = "stop"
        elif light == "yellow":
            car_command = "stop"
        elif light == "green":
            car_command = "go"
        else:
            print("Light is broken")
        
    return car_command

