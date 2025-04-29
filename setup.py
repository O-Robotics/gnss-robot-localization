from setuptools import setup

setup(
    name='gnss_ekf',
    version='0.0.0',
    packages=['gnss_ekf'],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + 'gnss_ekf']),
        ('share/gnss_ekf/launch', ['launch/gnss_ekf.launch.py']),
        ('share/gnss_ekf', ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='your_name',
    maintainer_email='your_email@example.com',
    description='GNSS localization with EKF',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'gnss2pose = gnss_ekf.gnss2pose:main',
        ],
    },
)
