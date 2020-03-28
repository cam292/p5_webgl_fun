#!/bin/sh

# You can set the following environment variables with the following effects:
#export HOST=0.0.0.0                # Specify the host name of the web server (needs to be 0.0.0.0 to work in a docker container)
#export PORT=80                     # Use a different port inside the container
#export ENVIRONMENT=production      # Specify the environment to bring the server up in, either development or production
#export DEBUG=false                 # What log level to run the server at
#export SECRET_KEY=a_super_secret   # If you want to specify a specific secret key, otherwise a random one is generated

if [ "$1" = 'shell' ]; then
    # Access the shell of this container
    exec /bin/ash
elif [ "$1" = 'dev' ]; then
    # Run this container in development mode
    export ENVIRONMENT=development
    export DEBUG=true
    export HOST=0.0.0.0
    export PORT=80
    python flask_template.py
else
    python flask_template.py
fi
