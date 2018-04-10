from setuptools import setup

setup(name='zxcvbn',
      version='1.0',
      description='Password strength estimator',
      author='Ryan Pearl',
      author_email='rpearl@dropbox.com',
      url='https://www.github.com/rpearl/python-zxcvbn',
      packages=['zxcvbn'],
      package_data={
        'zxcvbn': ['generated/frequency_lists.json',
                   'generated/adjacency_graphs.json',
                   ],
        },
      classifiers=[
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        ],
     )
