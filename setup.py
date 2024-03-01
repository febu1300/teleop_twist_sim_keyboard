from setuptools import setup

package_name = 'teleop_twist_sim_keyboard'

setup(
    name=package_name,
    version='2.3.2',
    packages=[],
    py_modules=[
        'teleop_twist_sim_keyboard'
    ],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Chris Lalancette',
    maintainer_email='buruktetemke@gmail.com',
    author='Graylin Trevor Jay, Austin Hendrix',
    keywords=['ROS'],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: BSD',
        'Programming Language :: Python',
        'Topic :: Software Development',
    ],
    description='A robot-agnostic teleoperation node to convert keyboard'
                'commands to Twist messages.',
    license='BSD',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'teleop_twist_sim_keyboard = teleop_twist_sim_keyboard:main'
        ],
    },
)
