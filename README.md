# DjDockerManager

DjDockerManager is a Django-based web application that allows you to manage Docker containers through a RESTful API. 
With DjDockerManager, you can create and manage "apps," which represent Docker container configurations, and execute and track the execution of these containers.

## Prerequisites
Before getting started, ensure you have the following dependencies installed on your system:
Python 3.x
Django
Django Rest Framework

## Usage
DjDockerManager provides a simple web interface to manage Docker containers. You can perform the following actions:
  1. Create an App: Create a new Docker container configuration by providing a name, Docker image URL, executable command, and environment variables.
  2. List Apps: View a list of all created apps.
  3. Get, Update, Delete an App: Perform operations on individual apps, including getting details, updating configurations, and deleting.
  4. Run App: Execute an app, which starts a Docker container based on the app's configuration.
  5. List Runs: View a list of execution history (runs) for a specific app.
  6. For detailed usage instructions and examples, please refer to the API Endpoints section below.

## API Endpoints
DjDockerManager exposes the following API endpoints for managing apps and runs:

- Create an App: POST /apps/
  Create a new app with the specified configuration.

- List Apps: GET /apps/
  Retrieve a list of all created apps.

- Get, Update, Delete an App: GET /apps/{app_id}/, PUT /apps/{app_id}/, DELETE /apps/{app_id}/
  Perform operations on a specific app by its ID.

- Run App: POST /apps/{app_id}/run/
  Execute an app and start a Docker container based on its configuration.

- List Runs: GET /apps/{app_id}/run/
  View a list of execution history (runs) for a specific app.

## Project Structure
The project is organized as follows:  
  - main/: The main Django app containing models, views, and serializers.
  - main/models.py: Defines the database models for App and Run.
  - main/views.py: Contains API views for managing apps and runs.
  - main/serializers.py: Serializers for the app and run data validation.
  - main/urls.py: Defines the URL patterns for API endpoints.
  - DjDockerManager/: The project's root directory containing settings and configuration files.
  - requirements.txt: Lists project dependencies.
  - manage.py: Django management script.

## Contributing
Contributions to DjDockerManager are welcome! If you have suggestions, or bug reports, or would like to add new features, please open an issue or create a pull request.
