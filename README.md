# ECE183DA-Lab3

## Usage:
* run controller.py with no arguments
* output data will be stored in analytic_outputs
* output plots will be stored in saved_plots
* All the paths for either the Paperbot or the Segway will be simulated at once
  * you can determine which one by changing *PAPERBOT_SIM* to True or False in **main()** of *controller.py*

### robot.py
* Includes definition of the **Agent** class that is the subject of the simulation. 
* Using the parameters loaded from one of two yaml files, an **Agent** can be instantiated as either a Paperbot or a Segway.
* **state_update()**: takes as input the PWN signals and updates the Agent's state
* **get_observation()**: returns the noisy output of the Lidar and IMU sensors
* **get_distance()**: takes the room dimensions, true position and true theta of the **Agent** as input and returns the exact length of a ray projecting out of the **Agent** at an angle of theta.
    * This function is called twice for the two different Lidar sensors with different theta inputs, and noise is applied to the output

### controller.py
* Contains the main() function and runs the simulation
* **main()**: opens the parameter file, initialize the **Agent** as either a Paperbot or Segway, then passes the **Agent** and the name of an input file to loop()
* **loop()**: given an **Agent** and the name of an input file, open the input file and run through the simulation until the inputs are exhausted
    * The input file is a CSV file with two columns, one for the PWM inputs for each wheel
    * Outputs all the sensor readings and state history to a CSV file with 9 columns
* Also contains deprecated code for *pygame* which would display an individual simulation graphically. This was commented out since we started running several simulations at once

### plots.py
* Given the output files of the analytical and webots simulation, plot the data onto several graphs
    * Front_Lidar vs Time
    * Right_Lidar vs Time
    * Compass_X vs Time (cos(theta) with noise)
    * Compass_Y vs Time (sin(theta) with noise)
    * Gyro vs Time (angular velocity)
    * Theta vs Time (exact value, in degrees)
    * X position vs Time (exact value)
    * Trajectory (X pos vs Y pos)
    
### analytic_inputs/generate_paths.py
* The webots simulation got its inputs from a function that returned different values for different time periods, but the analytical simulation inputs came from reading one line at a time from an input file
* **create_input_file_from_func()**: converts a function defining the path into a CSV file that can be used by our simulation
* **path_N()**: a python translation of the Nth path that was used in the webots simulation

### analytic_inputs/
* contains all the input files that will control how the **Agent** acts in the simulation
* Each is a CSV with two columns
    * First column is for the left wheel inputs
    * Second column is for the right wheel inputs
    
### analytic_outputs/ and webots_outputs/
* contains the outputs of all the different simulations
* Each is a CSV with 9 columns
    * Column 1 is the time, with a time step of 5 ms
    * Columns 2-3 are the Front and Right Lidar readings, respectively
    * Column 4 is the gyro reading
    * Column 5-6 are the compass readings
    * Column 7-8 are the true (non-noisy) x and y positions
    * Column 9 is the true (non-noisy) theta position
    
### webots_outputs/*.txt
* These are copy-and-pasted matlab functions that each of the MAE teammates used in their simulation that were translated in the *generate_paths.py* module

### saved_plots
* contains png images of all the plots created by *plots.py*

### lab3_controller.py and my_controller2.py
* two different implementations by different teammates of a python Webots controller
* NOT used to create the files in webots_outputs/
* Only included for use in the future

### lab3_controller.m
* Matlab webots controller
* Used to create the files in webots_outputs/