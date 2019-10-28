import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='django_fieldsets_with_inlines',
    version='0.2',
    author='Robert Kovac',
    author_email='robert.kovac@gmail.com',
    description='Mixin inlines and fieldsets in Django admin.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/robertkovac/django-fieldsets-with-inlines",
    packages=['fieldsets_with_inlines'],  # setuptools.find_packages(),
    include_package_data=True,
    license='MIT',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Framework :: Django',
        'Framework :: Django :: 2.0',
        'Intended Audience :: Developers',
    ],
    python_requires='>=3.4'
)
