docker build -t greetings-service .
docker tag greetings-service localhost:5000/greetings-service
docker push localhost:5000/greetings-service
