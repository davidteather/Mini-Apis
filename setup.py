from distutils.core import setup
import os.path
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
  name = 'TikTokApi',         
  packages = ['TikTokApi'],   
  version = '2.1.5',      
  license='MIT',        
  description = 'The Unoffical TikTok API Wrapper in Python 3.',   
  author = 'David Teather',                   
  author_email = 'contact.davidteather@gmail.com',     
  url = 'https://github.com/davidteather/Mini-Apis',
  long_description=long_description,
  long_description_content_type="text/markdown",  
  download_url = 'https://github.com/davidteather/Mini-Apis/tarball/master', 
  keywords = ['apis', 'collection', 'mini', 'mini-apis'], 
  install_requires=[
          'requests'
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers', 
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',  
    'Programming Language :: Python :: 3.7'
  ],
)