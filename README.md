                                                  Hello World Greetings Service


This project implements a simple greetings service using Python and Flask. The service responds with different salutations based on the customer's preference. The solution includes a Dockerfile for containerization and Kubernetes deployment scripts.


              Build and Run Locally

1. Clone the Repository:
    git clone https://github.com/sanath05/parcelLab-SRE-entrytest.git
    cd parcelLab-SRE-entrytest


2. Build and Run Locally:
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
. For customer A:
  curl http://localhost/greet?customer_name=A


. For customer B:
  curl http://localhost/greet?customer_name=B


. For customer C:
  curl http://localhost/greet?customer_name=C
