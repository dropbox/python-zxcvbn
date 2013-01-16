from distutils.core import setup

setup(name='zxcvbn',
      version='1.0',
      description='Password strength estimator',
      author='Ryan Pearl',
      author_email='rpearl@dropbox.com',
      url='https://www.github.com/rpearl/python-zxcvbn',
      packages=['zxcvbn'],
      package_data={'zxcvbn': ['generated/frequency_lists.json', 'generated/adjacency_graphs.json']}
     )
