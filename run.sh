#! /usr/bin/bash
echo "==========================#############==============================="
echo "Hello and Welcome."
echo "I am initiating the server."
echo "You can re-run me without any issues."
echo "-----------===-------------################-------------===-------------"
if [ -d "venv" ];
then
    echo "Virtual environment exists. Enabling the virtual env"
    # Activate virtual env
    source venv/bin/activate
else
    echo "No Virtual environment."
    echo "creating .venv and installing dependencies using pip"
    # Create the venv -> Activate it -> Install dependencies
    python3 -m virtualenv venv
    source venv/bin/activate
    pip3 install --upgrade pip
    pip3 install -r requirements.txt
fi

export ENV=production
if [ $ENV == "production" ]
then
    export DB_USER=postgres
    export DB_PASSWORD=enter_your_password_here
    export DB_HOST=localhost
    export DB_PORT=5432
    export DB_NAME=flask_db
    export SECRET_KEY=pw123pwshdshhjcvjh6567bdsuvydkj345@-1
    export SECURITY_PASSWORD_SALT=124709gchgcjvjvhtrer51232kj345@-1
else
    export SECRET_KEY=pw123pwshdshhjcvjh6567bdsuvydkj345@-1@-1
    export SECURITY_PASSWORD_SALT=124709gchgcjvjvhtrer51232kj345@-1
fi
echo "Required ${ENV} environment variables exported"

python3 app.py
deactivate
