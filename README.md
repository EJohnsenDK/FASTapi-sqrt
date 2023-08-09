## FastAPI Square Root Web Application
This repository contains a FastAPI application that calculates the square root of numbers and maintains a brief history of calculations.

## Cloning the Repository
1. Git: Ensure you have Git installed on your machine. 
   If not, you can download and install it from here https://git-scm.com/downloads
2. Navigate to the Desired Directory: Use your terminal or command-line interface to navigate to the directory 
   where you want to clone the repository: (cd <path_to_directory>)
3. Clone the Repository: Clone the repository using the following command. 
   Replace <repository_url> with the actual URL of the GitHub repository: (git clone <repository_url>)
4. Navigate to the Cloned Directory: (cd <repository_name>)

## Building and Running the Docker Image
1. Ensure Docker is installed on your machine. 
   If not, you can download and install it from here https://www.docker.com/products/docker-desktop/
2. Navigate to the directory containing the Dockerfile.
3. Run the command `docker build -t <desired_image_name> .` to build the Docker image.
4. Once built, you can run the image using the command: `docker run -p 8000:8000 <desired_image_name>`.

## Testing the Web Application through a local browser
1. After the Docker container is running, open a web browser and navigate to `http://localhost:8000/docs`. 
   This will bring up the FastAPI Swagger UI, where you can see the defined endpoints and test them directly.
2. To test the POST endpoint:
   - In the Swagger UI, click on the POST `/api/v1/sqrt` endpoint.
   - Click the "Try it out" button.
   - Provide a JSON payload with a number, e.g., `{"number": "134,87"}`. (NB: Check * below)
   - Click "Execute". The square root of the provided number will be displayed in the response.
3. To test the GET endpoint:
   - In the Swagger UI, click on the GET `/api/v1/sqrt` endpoint.
   - Click the "Try it out" button.
   - Click "Execute". You will see a list of the latest square root calculations, up to a maximum of 4.

## Testing the Web Application through the command-line interface (CLI)
1. If needed run Docker in the background by the 'docker run -d -p 8000:8000 <desired_image_name>' command
2. To test the POST request type:
   - Linux, macOS: (NB: Check * below)
   > `curl -X 'POST' -H 'Content-Type: application/json' -d '{"number": "134,87"}' http://localhost:8000/api/v1/sqrt` 
   - Windows: (NB: Check * below)
   > Invoke-WebRequest -Uri http://localhost:8000/api/v1/sqrt -Method POST -Headers @{"Content-Type"="application/json"} -Body '{"number": "134,87"}' 
   - or for content only:
   > (Invoke-WebRequest -Uri http://localhost:8000/api/v1/sqrt -Method POST -Headers @{"Content-Type"="application/json"} -Body '{"number": 
   > "134,87"}').Content
3. To test the GET request type: 
   - Linux, macOS: 
   > `curl -X 'GET' http://localhost:8000/api/v1/sqrt`
   - Windows:
   > Invoke-WebRequest -Method GET -Uri http://localhost:8000/api/v1/sqrt
   - or for content only:
   > (Invoke-WebRequest -Method GET -Uri http://localhost:8000/api/v1/sqrt).Content

'*' Input number format is string to allow for both ',' and'.' as decimal separator
