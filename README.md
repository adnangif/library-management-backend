# Getting Started

`prerequisites:`
<br>
**Python recent version**
<br>
**Git Bash**

When running the project for the first time in Windows using powershell,


    git clone https://github.com/adnangif/library-management-backend.git
    cd library-management-backend

 **Create a virtual environment**

    python -m venv env 
    
 **Activating the virtual environment in windows**
    
    .\env\Scripts\Activate.ps1


`
Installing inside virtualenv is recommended, however you can start your project without virtualenv too.
`
<br>
<br>
<br>
Install project dependencies:

    pip install -r requirements.txt
    
    
**Edit 'mysql_credentials.py' to add mysql username,password,database**

You can now run the development server:

    python manage.py runserver