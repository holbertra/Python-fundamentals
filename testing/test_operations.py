from operations import traffic_light_choice

# car = go or stop
# light = yellow, red, green

#- Moving Car
def test_light_choice():
    assert traffic_light_choice("moving", "red") == "stop"
    assert traffic_light_choice("moving", "yellow") == "go"
    assert traffic_light_choice("moving", "yellow") == "stop"

def test_light_choice_moving_yellow():
    assert traffic_light_choice("moving", "yellow") == "stop"

def test_light_choice_moving_green():
    assert traffic_light_choice("moving", "green") == "go"

#- Stopped Car
def test_light_choice_stop_red():
    assert traffic_light_choice("stopped", "red") == "stop"

def test_light_choice_stop_yellow():
    assert traffic_light_choice("stopped", "yellow") == "stop"

def test_light_choice_stop_green():
    assert traffic_light_choice("stopped", "green") == "go"


