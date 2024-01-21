
Hello World Greetings Service


This project implements a simple greetings service using Python and Flask. The service responds with different salutations based on the customer's preference. The solution includes a Dockerfile for containerization and Kubernetes deployment scripts.


Build and Run Locally


1. Clone the Repository:
    git clone https://github.com/sanath05/parcelLab-SRE-entrytest.git

    cd parcelLab-SRE-entrytest


3. Build and Run Locally:

          # Build the Docker image 
          ./build.sh 
  

           # Run the Docker container 
           docker run -p 5000:5000 greetings-service

  The service will be accessible at http://localhost:5000/greet.


Build Docker Image and Register
              
1. Build and Register Docker Image:
   
       # Build and register the Docker image
       ./build.sh
This script builds the Docker image and tags it for a local registry.


Deploy to Kubernetes
                    
1. Deploy to Kubernetes:

          # Deploy the solution to a local Kubernetes cluster 
          ./deploy.sh
This script deploys the greetings service to Kubernetes using the deployment.yaml and service.yaml files.

Testing Endpoints
                    
After deployment, you can test the endpoints using tools like curl:
  
    For customer A:
      curl http://localhost/greet?customer_namea


    For customer B:
      curl http://localhost/greet?customer_nameb


    For customer C:
      curl http://localhost/greet?customer_namec


Cleanup: 

To clean up the deployed resources:

        kubectl delete deployment greetings-deployment
        kubectl delete service greetings-service


 
For Quality Considerations

1. Unit Testing: Write unit tests for the service to ensure that each customer gets the expected greeting.
2. Code Review: Conduct code reviews to maintain code quality.
3. Error Handling: Implement proper error handling to handle unexpected scenarios.
4. Logging: Include appropriate logging statements for debugging and monitoring.
5. Use linting tools (e.g., pylint) to enforce coding standards.
6. Consider using a code formatter (e.g., black) for consistent code style.
7. Document your code and include comments where necessary.






NOTE:
. This setup assumes you have a local Docker registry running on localhost:5000. Adjust the registry location accordingly if needed.

. Remember to make the scripts executable using chmod +x script.sh before running them.




ERRORS:


Error: ErrImagePull
Error: ImagePullBackOff


While checking pod level logs I noticed above error that ErrImagePull and after describing the pod got to know below error:

Failed to pull image "localhost:5000/greetings-service": Error response from daemon: Get "http://localhost:5000/v2/": dial tcp 127.0.0.1:5000: connect: connection refused


Troubleshooting steps:

While I am using minikube and want to pull down the image from 127.0.0.1:5000 then getting above error.
So I have setup the registry inside the minikube instead of host side.
i.e.

host: registry (127.0.0.1:5000)

minikube: no registry (the K8s could not find your image)


How to check ?
Check minikube container.

    docker ps -a
Then login into minikube

    minikube ssh
enter: curl 127.0.0.1:5000
you will get Failed to connect to 127.0.0.1 port 5000: Connection refused.

Now to setup the registry type below command in minikube:

    docker run --restart=always -d -p 5000:5000 --name registry registry:2

Now you can test the registry with following commands:

    curl 127.0.0.1:5000
    curl 127.0.0.1:5000/v2
    curl 127.0.0.1:5000/v2/_catalog
    
    {"repositories":[]}
    # it's successful


Now again start running from ./build.sh. You will able to pull the image without any errors. 
