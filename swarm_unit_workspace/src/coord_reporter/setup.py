from setuptools import setup

package_name = 'coord_reporter'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='sim',
    maintainer_email='swarmation@todo.todo',
    description='Swarm unit publishes its position',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'coord_publisher = coord_reporter.swarm_bot_coord_pub:main',
            'coord_subscriber = coord_reporter.swarm_bot_visual_perc:main'
        ],
    },
)
