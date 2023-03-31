URL Checker
This is a Dockerized web app that checks a list of URLs and displays the HTTP response, HTTP status code, requester IP, and resolved DNS target for each URL.

Prerequisites
Docker installed on your machine
Getting started
Clone this repository to your local machine.

Navigate to the project directory.

Create a new file called urls.txt in the project directory, and paste a list of URLs (one per line) into it.

Build the Docker image by running the following command:

Copy code
docker build -t url-checker .
This will create a new Docker image called url-checker.

Run a container from the Docker image by running the following command:

arduino
Copy code
docker run -p 5000:5000 url-checker
This will run the container and start the Flask app, which will be available at http://localhost:5000/.

Open a web browser and navigate to http://localhost:5000/. You should see a table with the results of hitting each URL in the urls.txt file.

Notes
The app uses the Flask web framework and the requests and socket Python libraries.
The urls.txt file should contain one URL per line.
The app listens on port 5000, which is exposed in the Dockerfile.
The Flask app is set to run in debug mode by default. This can be changed by modifying the debug parameter in the app.run() method in app.py.
To stop the container, press Ctrl+C in the terminal running the container, or run docker stop <container_id> (where <container_id> is the ID of the container, which can be found by running docker ps).
To remove the container and image, run docker rm <container_id> and docker rmi url-checker.