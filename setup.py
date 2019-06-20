from setuptools import setup, find_packages


def readme():
    with open('README.md') as f:
        return f.read()


classifiers = [
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
]

setup(
    name            = 'visjs_timeline',
    packages        = find_packages(),
    package_data    = {'visjs_timeline': ['resources/*.*']},
    version         = '0.1',
    description     = 'Tool for creating VisJs html timeline.',
    long_description=readme(),
    long_description_content_type='text/markdown',
    author          = 'Jan Seda',
    author_email    = 'xsedaj00@gmail.com',
    url             = 'https://github.com/Honzin/visjs_timeline',
    download_url    = '',
    install_requires=[],
    keywords        = ["timeline", "visjs"],
    classifiers     = classifiers,
)

