import setuptools

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setuptools.setup(
    name='linkedinputs',
    version='0.0.1',
    license='LICENSE',
    author='naderidev',
    author_email='mohammadrezanaderi84@gmail.com',
    description='linked inputs for flet framework',
    keywords=['flet', 'pin input', 'pininput', 'TextField',
              'python', 'field', 'naderidev', 'text field'],
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/naderidev/linkedinputs',
    package_dir={'': 'src'},
    packages=setuptools.find_packages(where='src'),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python :: 3.10',
        'License :: OSI Approved :: MIT License',
    ],
    python_requires='>=3.9',
    include_package_data=True,
    install_requires=[
        'flet'
    ]
)
