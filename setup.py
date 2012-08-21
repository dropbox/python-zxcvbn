from distutils.core import setup

setup(Name='zxcvbn',
      version=1.0,
      description='Password strength estimator',
      author='Ryan Pearl',
      author_email='rpearl@dropbox.com',
      url='https://www.github.com/rpearl/python-zxcvbn',
      packages=['zxcvbn'],
      data_files=[('generated', ['frequency_lists.json', 'adjacency_graphs.json'])]
     )
