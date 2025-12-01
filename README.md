## go2_urdf
This repository contains the urdf/xacro model of go2.


## Build the library
Create a new workspace:
```
# Create the directories
# Do not forget to change <...> parts
mkdir -p <directory_to_ws>/<ws_name>/src
cd <directory_to_ws>/<ws_name>/
```

Clone this library:
```
# Navigate to the directory of src
# Do not forget to change <...> parts
cd <directory_to_ws>/<ws_name>/src
git clone git@github.com:unitreerobotics/go2_urdf.git
```

Build:
```
# Build it
colcon build --symlink-install

# Source it
source <directory_to_ws>/<ws_name>/devel/setup.bash
```

## Run the library
```
# Show the go2 model in Rviz
roslaunch go2_description go2_rviz.launch

```

## Note - isaac gym (or other similiar engine) usage

Collision parameters in urdf can be amended to better train the robot:

Open "go2_description.urdf" in "./go2_description/urdf" and amend
`box size="0.213 0.0245 0.034"` in the "FL_thigh", "FR_thigh", "RL_thigh", 
"RR_thigh" links.

For example, changing to `box size="0.11 0.0245 0.034"` shortens the length of 
the thigh is shortened from 0.213 to 0.11, which may avoid unnecessary collisions 
between the thigh link and the calf link.
