**requirements_dev.txt**  
We use it for testing.  
It makes it easier to install and manage dependencies for development and testing, separate from the dependencies required for production.  

**difference between requirements_dev.txt and requirements.txt**  
**requirements.txt** is used to specify the dependencies required to run the production code of a Python project, while **requirements_dev.txt** is used to specify the dependencies required for development and testing purposes.  

**tox.ini**  
We use it for testing in the Python package, testing against different versions of Python.  

**how tox works (tox environment creation)**  
- Install dependencies and packages  
- Run commands  
- It's a combination of **virtualenvwrapper** and **makefile**  
- It creates a **.tox** folder  

**pyproject.toml**  
It is used for configuring the Python project. It is an alternative to the **setup.cfg** file. It contains configuration related to the build system, such as the build tool used, package name, version, author, license, and dependencies.  

**setup.cfg**  
In summary, **setup.cfg** is used by **setuptools** to configure the packaging and installation of a Python project.  

**Testing Python application**  

**types of testing**  
- **Automated testing**  
- **Manual testing**  

**Mode of testing**  
- **Unit testing**  
- **Integration tests**  

**Testing frameworks**  
- **pytest**  
- **unittest**  
- **robotframework**  
- **selenium**  
- **behave**  
- **doctest**  

**Check with the code style formatting and syntax (coding standards)**  
- **pylint**  
- **flake8** (It is best because it contains 3 libraries: pylint, pycodestyle, and mccabe)  
- **pycodestyle**









test using python <copy relative path >

for mlflow needed the run-->   mlflow ui
