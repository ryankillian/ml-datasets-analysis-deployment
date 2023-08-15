# Docker Deployment of PyTorch Model

This folder contains the files necessary for deploying the trained PyTorch model using Docker. The steps below outline how to set up and run the Docker container for model inference.

## Steps

1. **Look in the Notebook:**

   - Refer to the notebook for training the model, saving the model, and running inference.
   - Make sure to place the `model_weights.pth` file (saved from the notebook) in the `docker` folder.
     ```python
     torch.save(model.state_dict(), "model_weights.pth")
     ```

2. **Create a Python Script for Inference:**

   - This folder already includes a Python script named `inference_script.py` that loads the saved model, sets up a Flask server, and defines an API endpoint for running inference.

3. **Create Test Data:**

   - The notebook contains a command to generate test data.
   - Cut and paste the input text into the `curl` command. See `curl-1.txt` in the `test_data` folder for an example.

4. **Test Locally:**

   - Create a virtual environment:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     pip install Flask numpy torch
     python inference_script.py
     ```

5. **Test the Local API Endpoint:**

   - Once the Flask server is running, test the API endpoint with a `curl` command:
     ```bash
     curl -X POST -H "Content-Type: application/json" -d '{"input": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]}' http://localhost:80/predict
     ```

6. **Create a `requirements.txt` File:**

   - This folder already includes a `requirements.txt` file that lists all the Python packages needed to run the `inference_script.py` script.

7. **Create a Dockerfile:**

   - This folder already includes a Dockerfile that specifies the base image (Python 3.8), sets the working directory, copies the `requirements.txt` file and application code into the container, installs the required Python packages, and defines the command to run when the container starts.

8. **Build the Docker Image:**

   - Open a terminal and navigate to the `docker` folder.
   - Build the Docker image with the following command:
     ```bash
     docker build -t mnist-pytorch .
     ```

9. **Run the Docker Container:**

   - Start the Docker container with the following command:
     ```bash
     docker run -p 80:80 mnist-pytorch
     ```

10. **Test the API Endpoint:**

- Once the container is running, test the API endpoint with a `curl` command:
  ```bash
  curl -X POST -H "Content-Type: application/json" -d '{"input": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]}' http://localhost:80/predict
  ```

---

11. **Further Reading**

Deploying a machine learning model involves making it available for use in a production environment, where it can take input data, process it, and return the output. There are several options for deploying a model, each with its own advantages and limitations. Here are some common approaches:

1. **Local deployment:** In this approach, the model is deployed on the same machine where it was developed. This is suitable for testing and small-scale use. However, it is not practical for large-scale applications or for making the model available to external users.

2. **Web API:** The model can be deployed as a web service using frameworks like Flask or FastAPI. This allows users to send data to the model over the internet and receive predictions in real-time. This approach is suitable for making the model available to a wide audience.

3. **Cloud deployment:** Major cloud providers like AWS, Azure, and GCP offer services for deploying machine learning models. These services handle the infrastructure, scaling, and management of the models, making it easier to deploy and maintain them.

4. **Containerization:** Docker and Kubernetes can be used to deploy models in containers. This approach ensures that the model runs in the same environment regardless of where it is deployed, making it more portable and easier to manage.

5. **On-device deployment:** For applications where latency is crucial, the model can be deployed directly on the device where it will be used, such as a smartphone or IoT device. This approach reduces the time needed to send data to a server and receive predictions.

6. **Edge deployment:** In some cases, models can be deployed on edge devices, such as routers or gateways, which are closer to the data source. This approach reduces the time and bandwidth required to send data to a central server.

7. **Embedded deployment:** For certain applications, such as robotics or autonomous vehicles, the model may be deployed on an embedded system, where it runs as part of the system's firmware.

8. **Batch deployment:** In some cases, real-time predictions are not necessary. The model can be deployed to process data in batches, making predictions on large datasets at once.

9. **Serverless deployment:** Some cloud providers offer serverless deployment options, where the model is deployed as a function that is triggered by an event, such as data being added to a database.

Each of these deployment options has its own advantages and limitations, and the best approach depends on the specific use case, the scale of the deployment, the available infrastructure, and the desired performance characteristics.
