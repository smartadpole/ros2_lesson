from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
from launch.actions import TimerAction

def generate_launch_description():
    return LaunchDescription([
        # 启动海龟仿真器
        Node(
            package='turtlesim',
            executable='turtlesim_node',
            name='sim'
        ),

        # 启动海龟1的坐标系广播器
        Node(
            package='learning_tf',
            executable='turtle_tf_broadcaster',
            name='broadcaster1',
            parameters=[
                {'turtlename': 'turtle1'}
            ]
        ),

        # 声明目标坐标系参数（默认值为turtle1）
        DeclareLaunchArgument(
            'target_frame', default_value='turtle1',
            description='Target frame name.'
        ),

        # 启动海龟2的坐标系广播器
        Node(
            package='learning_tf',
            executable='turtle_tf_broadcaster',
            name='broadcaster2',
            parameters=[
                {'turtlename': 'turtle2'}
            ]
        ),

        # 启动跟随控制器
        Node(
            package='learning_tf',
            executable='turtle_following',
            name='listener',
            parameters=[
                {'target_frame': LaunchConfiguration('target_frame')}
            ]
        ),
    ])
