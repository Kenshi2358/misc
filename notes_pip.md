<h2>General Notes:</h2>
Pip is a package manner for Python and is operating system independent.<br>
Homebrew is a package manner for MacOS only.<br>
Both Pip and Homebrew are command-line package installers and are open source software.<br>
There is sometimes overlap between the two depending on how you installed Python / pip, which can cause conflicts.

<h3>Commands:</h3>

To check what version of python you’re running, type: `python3 --version`  
To see where this version is installed, type: `which python3`

To install a python package, run: `pip install [package_name]`  
To upgrade a python package, run: `pip install [package_name] --upgrade`  

To check for all python packages installed, type: `pip list`  
To check for outdated python packages, type: `pip list --outdated`  
To update pip, type: `pip install --upgrade pip`  

To see where pip installs a package, type: `pip show [package_name]`  
To see where pip is installed, type: `python3 -m pip --version`

<h3>Requirements File:</h3>

To generate a requirements file for installing in another environment, run:  
`python -m pip freeze > requirements.txt`

To install a requirements.txt file, run:  
`python -m pip install -r requirements.txt`

To update a virtual environment with a new requirements.txt file, run:  
`pip install -r requirements.txt --upgrade`  
This compares the current virtualenv with your requirements and updates only the necessary packages.

<h3>Version checks:</h3>

To check your python3 version, type: `python3 --version`  
To check your pip version and installation location, type: `pip --version`

<h4>Virtual Environments:</h4>

venv is the module to create and manage virtual environments (VE’s).  
venv is included in the Python standard library and does not require any additional installation.  
There are many other VE packages out there, but this explanation only deals with venv.

<h4>General recommendation:</h4>
Create one virtual environment for each repo.<br>
Have one virtual environment for your personal testing.<br>
Protect the original python package installation by never using it.

<h4>To create a new virtual environment:</h4>

Navigate to the folder where you want to create them.  
Then run: `python3 -m venv env1`  
where env1 is new name of your environment.

If you want to run a particular version of python, say 3.9, you can install as:<br>
`python3.9 -m venv env1`

Then, to activate your VE, type:
`source “folder_path_to_ve”/bin/activate`

To leave a VE, type: `deactivate`<br>
To confirm which python interpreter you’re in, type: `which python`<br>
To delete a VE, type: `sudo rm -rf “virtual environment name”`

<h3>To run a virtual environment locally within VS Code:</h3>
You’ll need to create a launch.json file if you don’t already have one.<br>
Visual Studio Code has more details on this: https://code.visualstudio.com/docs/editor/debugging

You need this json file under the “.vscode” folder.<br>
From here, you can change how your scripts run locally and in what environment.<br>
To change your environment, go to the configurations array and add a new key called “python”, with value:<br>
”folder_path_to_ve/bin/python”

For example, I have my environment defaulted to:

`"python": "/Users/shahnert/Desktop/Envs/metl3.10/bin/python",`<br>
If you want to change your python version to another installed version, you can update it here as well.<br>
For example, to switch between Python 3.10, I can type:<br>
`"python": "/opt/homebrew/bin/python3.10",`

Additionally, this configuration array is where you add arguments if you’re using the python module: argparse<br>
This requires the key: “args”, with value: “your_arguments”. For example:

`"args": ["-db_host", "venom.des.mdx.med", "-db_name", "mdx_wh_phi_data_operations", "-path", "/Users/shahnert/Downloads/", "-table_type", "eligibility", "-elig_table_name", "basys_elig_20230605"]`

<h3>To run a virtual environment on a server:</h3>

1) In the associated repo, create a branch with a new .txt file under the requirements folder.<br>
The name of that text file will serve as the name of that virtual environment.<br>
2) Enter in all python packages and versions you want install here.<br>
3) Save file. Deploy branch.<br>
4) SSH onto that server. Sudo su des.<br>
5) Check what VE’s are available on that server, with the following commands:<br>
`workon, lsvirtualenv -b`