from setuptools import setup

setup(
    name='gnss-robot-localization',
    version='0.0.1',
    packages=['gnss-robot-localization'],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/gnss-robot-localization']),
        ('share/gnss-robot-localization/launch', ['gnss_ekf.launch.py']),
        ('share/gnss-robot-localization', ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Li',
    maintainer_email='ziyli@o-robotics.com',
    description='GNSS localization with EKF',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'gnss2pose = gnss_ekf.gnss2pose:main',
        ],
    },
)
