from distutils.core import setup

setup(
    name='x_cloud_py',
    packages=['x_cloud_py'],  # this must be the same as the name above
    version='0.1.0',
    description='A random test lib',
    author='Arturo Martinez',
    author_email='wankes2000@gmail.com',
    url='https://github.com/peterldowns/mypackage',  # use the URL to the github repo
    download_url='https://github.com/peterldowns/mypackage/archive/0.1.tar.gz',  # I'll explain this in a second
    install_requires=['boto3==1.5.22','google-cloud-datastore==1.4.0'],
    keywords=['aws', 'cloud', 'google','gcp'],  # arbitrary keywords
    classifiers=[],
)