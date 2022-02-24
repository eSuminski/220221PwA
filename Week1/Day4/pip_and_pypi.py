"""This module contains notes on pip and pypi and the virtual environment"""
from name_generator.name_generator import GenName

print(GenName())

"""
To make use of the GenName() function I had to download the name_generator package from pypi. Pypi is the main
repository for Python packages that is free to use, and has just about anything you can need for your code. For
instance, to get the name generator above, I first used the pip install command to get the package from Pypi

pip install name-generator

Once the package was installed I was able to go into my virtual environment folder, find the package, and look over
the module to see how the function actually works. Once I knew it was just a simple method call, I made sure to import
it from the name_generator module inside the package called name_generator. Once I did that, I had free use of
the GeName() function!
"""

"""
I've mentioned the virtual environment a few times now. This folder contains the pip software for our project, and
any packages will install from Pypi. What is nice about having a virtual environment is that we can localize all
of the code and runtime configurations we want for our project specifically. Without the Virtual Environment, we would
have to be careful, because every time we wanted to start a new project we would have to specify to our Python 
interpreter where it is supposed to be looking. Pycharm does us a favor and handles that, along with creating our
Virtual Environment for us.
"""