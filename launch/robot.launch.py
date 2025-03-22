# Copyright (c) 2024 Intelligent Robotics Lab (URJC)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import Command, FindExecutable, LaunchConfiguration, PathJoinSubstitution
from launch_ros.actions import Node
import launch_ros.descriptions
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():

    declared_arguments = []
    nodes = []

    declared_arguments.append(
        DeclareLaunchArgument(
            'description_package',
            default_value='go2_description',
            description='Description package with robot URDF/xacro files made by manufacturer.',
        )
    )
    declared_arguments.append(
        DeclareLaunchArgument(
            'description_file',
            default_value='go2_description.urdf.xacro',
            description='URDF/XACRO description file with the robot.',
        )
    )
    declared_arguments.append(
        DeclareLaunchArgument(
            'prefix',
            default_value='',
            description='Prefix to be added to the robot description.',
        )
    )

    description_file = LaunchConfiguration('description_file')
    prefix = LaunchConfiguration('prefix')

    robot_description_content = Command(
        [
            PathJoinSubstitution([FindExecutable(name='xacro')]),
            ' ',
            PathJoinSubstitution([FindPackageShare('go2_description'), 
                                  'robots', description_file]),
            ' ',
            'prefix:=', prefix
        ]
    )

    robot_description_param = launch_ros.descriptions.ParameterValue(robot_description_content,
                                                                     value_type=str)

    nodes.append(Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        name='robot_state_publisher',
        output='screen',
        parameters=[{
            'robot_description': robot_description_param,
            'publish_frequency': 100.0,
            'frame_prefix': prefix,
            }],
        )
    )

    return LaunchDescription(declared_arguments + nodes)
