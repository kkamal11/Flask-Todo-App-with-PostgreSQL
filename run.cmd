::To prevent all commands in the batch file from displaying on screen
@echo off

::clear the screen
cls


ECHO ==========================#############===============================
ECHO Hello and Welcome.
ECHO I am initiating the server.
ECHO You can re-run me without any issues.
ECHO -----------===-------------################-------------===-------------

IF exist env (
ECHO Virtual environment exists. Enabling the virtual env
CALL ".\env\Scripts\activate"
) ELSE ( 
ECHO No Virtual environment.
ECHO creating venv and installing dependencies using pip
:: Create the venv env -> Activate it -> Install dependencies
python -m venv env
CALL .\env\Scripts\activate 
ECHO virtual env activated
python -m pip install --upgrade pip
pip install -r requirements.txt
ECHO =================================ALL PACKAGES INSTALLED======================================
)


SET ENV=development
SET SECRET_KEY=pw123pwshdshbdsuvydkj345@-1
SET SECURITY_PASSWORD_SALT=1247091232kj345@-1

ECHO.
ECHO Required %ENV% environment variables exported
ECHO.

python app.py