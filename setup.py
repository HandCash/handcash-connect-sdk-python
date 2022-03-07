from setuptools import setup, find_packages

setup(name='handcash_connect_sdk',
      version='0.2.1',
      description='handcash_connect_sdk - library for interacting with Handcash Connect API',
      long_description='This library allows HandCash users to authorize your app '
                       'in order to get the users\' info and trigger payments on their behalf.',
      classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: The Unlicense (Unlicense)',
        'Programming Language :: Python :: 3.8',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Intended Audience :: Developers',
      ],
      keywords='api handcash connect nanopayments duro',
      url='https://github.com/HandCash/handcash-connect-sdk-python',
      download_url='https://github.com/HandCash/handcash-connect-sdk-python',
      author='Krzysztof Fonal, Rafa Jimenez',
      author_email='krzysiekfonal@gmail.com, rafa@handcash.io',
      license='The Unlicense',
      packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
      install_requires=[
          'bitcoinx', 'requests', 'attr'
      ],
      zip_safe=True)
