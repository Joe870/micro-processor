from machine import Pin
import utime

led_1 = Pin(10, Pin.OUT)
led_2 = Pin(11, Pin.OUT)
led_3 = Pin(12, Pin.OUT)

segments = [
    machine.Pin(18, machine.Pin.OUT),
    machine.Pin(16, machine.Pin.OUT),
    machine.Pin(22, machine.Pin.OUT),
    machine.Pin(26, machine.Pin.OUT),
    machine.Pin(27, machine.Pin.OUT),
    machine.Pin(19, machine.Pin.OUT),
    machine.Pin(20, machine.Pin.OUT)
]
matrix_keys = [['1', '2', '3', 'A'],['4', '5', '6', 'B'],['7', '8', '9', 'C'],['*', '0', '#', 'D']]

keypad_rows = [9,8,7,6]
keypad_columns = [5,4,3,2]


currentFloor = 0

digit_segments = [
    [1, 1, 1, 1, 1, 1, 0, 0],  # 0
    [0, 1, 1, 0, 0, 0, 0, 0],  # 1
    [1, 1, 0, 1, 1, 0, 1, 0],  # 2
    [1, 1, 1, 1, 0, 0, 1, 0],  # 3
    [0, 1, 1, 0, 0, 1, 1, 0],  # 4
    [1, 0, 1, 1, 0, 1, 1, 0],  # 5
    [1, 0, 1, 1, 1, 1, 1, 0],  # 6
    [1, 1, 1, 0, 0, 0, 0, 0],  # 7
    [1, 1, 1, 1, 1, 1, 1, 0],  # 8
    [1, 1, 1, 1, 0, 1, 1, 0],  # 9
]

row_pins = [Pin(pin, Pin.OUT) for pin in keypad_rows]
col_pins = [Pin(pin, Pin.IN, Pin.PULL_DOWN) for pin in keypad_columns]

def display_number(number):
    segments_values = digit_segments[number]
    for i in range(len(segments)):
        segments[i].value(segments_values[i])

def scankeys():
    global currentFloor
    for row in range(4):
        for col in range(4):
            row_pins[row].high()
            utime.sleep(0.01)
            
        for col in range(4):
            if col_pins[col].value() == 1:  # Check if the column pin is high
                targetfloor = matrix_keys[row][col]
                
                print("You have pressed:", targetfloor)
            
                if targetfloor.isdigit():
                    led_1.off()
                    targetfloor = int(targetfloor)
                    if targetfloor < currentFloor:
                        #floor is lower
                        for floor in range(currentFloor, targetfloor-1, -1):
                            currentFloor = floor
                            display_number(currentFloor)
                            utime.sleep(1)  # Debounce delay
                        led_1.on()           
                    else:                    
                        #floor is higher
                        for floor in range(currentFloor, targetfloor + 1):
                            currentFloor = floor
                            display_number(currentFloor)
                            utime.sleep(1)  # Debounce delay
                        led_1.on()    
        # Set the row back low
        row_pins[row].low()
    
while True:
    scankeys()
    #for number in range(10):
    #    display_number(number)
    #    utime.sleep_ms(1000)
    