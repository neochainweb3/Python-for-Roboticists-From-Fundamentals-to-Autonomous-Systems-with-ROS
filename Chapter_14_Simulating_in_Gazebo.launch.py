<!-- Chapter 14 - Gazebo launch -->
<launch>
  <include file="$(find gazebo_ros)/launch/empty_world.launch" />
  <node name="spawn_urdf" pkg="gazebo_ros" type="spawn_model" ... />
</launch>
