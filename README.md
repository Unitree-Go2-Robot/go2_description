## go2_description
This repository contains the urdf model of go2.


## Build the package
Create a new workspace:
```
# Create the directories
# Do not forget to change <...> parts
mkdir -p <directory_to_ws>/<ws_name>/src
cd <directory_to_ws>/<ws_name>/

# Initialize the catkin workspace
colcon build
```

Clone this library:
```
# Navigate to the directory of src
# Do not forget to change <...> parts
cd <directory_to_ws>/<ws_name>/src
git clone git@github.com:Unitree-Go2-Robot/go2_description.git
git clone git@github.com:Unitree-Go2-Robot/go2_rviz.git
```

Build:
```
# Build it
colcon build

# Source it (Also available for zsh)
source <directory_to_ws>/<ws_name>/install/setup.bash
```

## Run the library
```
# Show urdf model of go2 in Rviz
ros2 launch go2_description robot.launch.py

#In another terminal
ros2 launch go2_rviz rviz.launch.py

```
If you want to visualize it using a GUI to move each joint, you can use the following command:
```
# Show urdf model of go2 in Rviz
ros2 launch go2_description robot_gui.launch.py
```

<!-- ## When used for isaac gym or other similiar engine 

Collision parameters in urdf can be amended to better train the robot:

Open "go2_description.urdf" in "./go2_description/urdf",
and amend the ` box size="0.213 0.0245 0.034" ` in links of "FL_thigh", "FR_thigh", "RL_thigh", "RR_thigh".

For example, change previous values to ` box size="0.11 0.0245 0.034" ` means the length of the thigh is shortened from 0.213 to 0.11, which can avoid unnecessary collision between the thigh link and the calf link. 

The collision model before and after the above amendment are shown as "Normal_collision_model.png" and "Amended_collision_model.png" respectively. -->


