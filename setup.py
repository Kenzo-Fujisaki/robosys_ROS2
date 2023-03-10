from setuptools import setup
import os 
from glob import glob

package_name = 'robosys_ROS2'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name), glob('launch/*.launch.py'))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='kenzo-fujisaki',
    maintainer_email='s21c1103bk@s.chibakoudai.jp',
    description='a package for practice',
    license='BSD-3-Clause',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'fortune = robosys_ROS2.fortune:main',
            'result = robosys_ROS2.result:main',
        ],
    },
)
