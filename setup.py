from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()

setup(name='test_dependencies',
      version='0.1.0',
      description='just playing around',
      long_description=readme(),
      classifiers = [
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent'
      ],
      python_requires=">=3.8",
      setup_requires=["numpy"],
      install_requires=[
          'pandas',
          'numpy',
          'matchms >= 0.9.0',
          'spec2vec >= 0.4',
          'plotly >= 4.14.3',
          'cimcb-lite >= 1.0.2',
          'scikit-bio >= 0.5.6',
          'scikit-learn >= 0.24.1'
      ],
      zip_safe=False)
