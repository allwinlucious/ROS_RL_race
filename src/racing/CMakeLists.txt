cmake_minimum_required(VERSION 3.10.0 FATAL_ERROR) # required for modern CMake features

include_guard(GLOBAL) # this CMakeLists can only be read once in this project

project(racing VERSION 0.1 LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 11) # compiler that supports C++11 is necessary
set(CMAKE_CXX_STANDARD_REQUIRED 11) # C++11 must be used by the compiler

# Find catkin and all required components.
# - roscpp: client library of ROS in Cpp
# - sensor_msgs: package containing lidar scan message definition
# - geometry_msgs: package containing "twist" message for target values for actuators
find_package(catkin REQUIRED REQUIRED COMPONENTS
    roscpp
    rospy
    sensor_msgs
    geometry_msgs
    flatland_msgs)

# Create the catkin package that depends on all requirements mentions above
catkin_package(INCLUDE_DIRS include
    LIBRARIES ${PROJECT_NAME}
    CATKIN_DEPENDS
    roscpp
    rospy
    sensor_msgs
    geometry_msgs
    flatland_msgs)

# add a building output: a library independent of ROS

# add a building output: a ROS-node that wraps the ROS-independent library
add_executable(vehicle_timer_node src/vehicle_timer_node.cpp)

# Link the node to the ROS packages used to encode send and receive signals.
add_dependencies(vehicle_timer_node ${catkin_EXPORTED_TARGETS})
target_include_directories(vehicle_timer_node PRIVATE ${catkin_INCLUDE_DIRS})
target_link_libraries(vehicle_timer_node ${catkin_LIBRARIES})

catkin_install_python(PROGRAMS scripts/RLcontroller_train.py scripts/RL_learn.py scripts/RL_controller.py
    DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)