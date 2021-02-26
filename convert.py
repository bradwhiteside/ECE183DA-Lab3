"""
if time<5
    wb_motor_set_velocity(motor_R,-1);
    wb_motor_set_velocity(motor_L,-6);
  elseif time>=5 && time<10
    wb_motor_set_velocity(motor_R,4);
    wb_motor_set_velocity(motor_L,-8);
  elseif time>=10 && time<15
    wb_motor_set_velocity(motor_R,-2);
    wb_motor_set_velocity(motor_L,-6);
  elseif time>=15
    wb_motor_set_velocity(motor_R,-8);
    wb_motor_set_velocity(motor_L,-2);
  end
"""

def input_func_1(time):
    if (time < 5):
        return -6, -1
    elif (time < 10):
        return -8, 4
    elif (time < 15):
        return -6, -2
    else:
        return -2, -8

def create_input_file_from_func(f, time_step, max_time):
