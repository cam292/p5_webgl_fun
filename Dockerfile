FROM python:3-alpine

RUN mkdir /flask_template

# Copy over and install requirements to create the base layer for this server
COPY requirements.txt /flask_template

WORKDIR /flask_template

RUN python3 -m pip install -r requirements.txt --no-cache-dir

# Copy over the rest of the service, so config changes don't require re-running installs
COPY . /flask_template

EXPOSE 80

ENTRYPOINT ["/flask_template/entry.sh"]
