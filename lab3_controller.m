%Get simulation time step;
TIME_STEP = wb_robot_get_basic_time_step();
% Create instances of motors sensors, nodes;
motor_R = wb_robot_get_device('motor_R'); 
% Device names have to be char, not string;
motor_L = wb_robot_get_device('motor_L');
compass = wb_robot_get_device('compass');
gyro = wb_robot_get_device('gyro');
lidar_R = wb_robot_get_device('Lidar_R');
lidar_F = wb_robot_get_device('Lidar_F');
robot = wb_supervisor_node_get_from_def('robot'); % For ground truth access;
rotation = wb_supervisor_node_get_field(robot,'rotation');
% Enable sensors (instance, sampling period[ms]);
wb_compass_enable(compass, TIME_STEP);
wb_gyro_enable(gyro, TIME_STEP);
wb_distance_sensor_enable(lidar_R, TIME_STEP);
wb_distance_sensor_enable(lidar_F, TIME_STEP);
% Make the motors non-position control mode;
wb_motor_set_position(motor_R, inf);
wb_motor_set_position(motor_L, inf);
%graphing the lines
%figure(1);
%lidar_F_plot = animatedline('Color', 'r');
%lidar_R_plot = animatedline('Color', 'b');
%legend('Front Sensor', 'Right Sensor')
%xlabel('Time [ms]');ylabel('Distance[m]')
%title('Lidar Sensor Data')
%figure(2);
%gyro_plot = animatedline('Color', 'r');
%legend('Gyro')
%xlabel('Time [ms]');ylabel('Angular Speed[rad/s]')
%title('Gyro Sensor Data')
%figure(3);
%compass_plot_x = animatedline('Color', 'b');
%compass_plot_y = animatedline('Color', 'g');
%legend('Compass x', 'Compass y')
%xlabel('Time [ms]');ylabel('Rotation[rad]')
%title('Compass Sensor Data')
steps =0;
time = 0;
fileID = fopen('values.txt', 'w');
% Need to call wb robot step periodically to communicate to the simulator;
while wb_robot_step(TIME_STEP) ~= -1  && time <20
  time = ((steps)*5)/1000;
  steps = steps + 1;
% Run a motor by velocity rad/sec;
  if time < 5
    wb_motor_set_velocity(motor_R,1);
    wb_motor_set_velocity(motor_L,1);
  elseif time < 10
    wb_motor_set_velocity(motor_R,-2);
    wb_motor_set_velocity(motor_L,2);
   else
     wb_motor_set_velocity(motor_R,-1);
     wb_motor_set_velocity(motor_L,-1);
  end

% Or run a motor by torque N/m;
%wb motor set torque(motor R,1);
% Read sensor data;
compass_data = wb_compass_get_values(compass);
gyro_data = wb_gyro_get_values(gyro);
lidar_F_data = wb_distance_sensor_get_value(lidar_F)/409.6;
lidar_R_data = wb_distance_sensor_get_value(lidar_R)/409.6;

%plot position sensor data

%addpoints(lidar_F_plot,time,lidar_F_data);
%addpoints(lidar_R_plot,time,lidar_R_data);
% Get ground truth data;
position = wb_supervisor_node_get_position(robot);
angle = wb_supervisor_field_get_sf_rotation(rotation);
velocity = wb_supervisor_node_get_velocity(robot);
fprintf(fileID, '%9.6f %9.6f %9.6f %9.6f %9.6f %9.6f %9.6f %9.6f %9.6f \r\n', time, lidar_F_data, lidar_R_data, gyro_data(2), compass_data(1), compass_data(3), position(1)+5, position(3)+5,angle(4)) ;
%plotground truth data;

%addpoints(gyro_plot, time, gyro_data(2));
%addpoints(compass_plot_x, time, compass_data(1));
%addpoints(compass_plot_y, time, compass_data(3));


end
% Close your controller;
wb_robot_cleanup();