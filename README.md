BigPanda DevOps Exercise Solution

Services:
services are using tornado library for http request handling.
services are running as unprivileged 'panda' user
supervisord is used to manage service state and allows auto restart in case of failure
big-service is running on port 8081
panda-service is running on port 8080

Provisioning:
Applied by the 'common' ansible role
ensures python, pip, and supervisor are present
ensures unprivileged user 'panda' exists

Deployment process:
deployment of both services is done via a generic 'service' role
the service is copied from roles/service/files/service-name to ~panda/service-name
supervisord configuration is updated
service is restarted

Deployment script:
deploy.sh allows to deploy each service separately or both at once


Adding new service:
Add the service code to roles/service/files/service-name
Add an instance of 'service' role to base.yml with service_name variable
