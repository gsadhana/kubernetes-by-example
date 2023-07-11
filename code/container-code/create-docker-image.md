# Create Docker image

1. Build image: `docker build -t k8s-by-example-lesson1 .`

2. Validate image: `docker run -dp 127.0.0.1:8080:80 k7s-by-example-lesson1` + `http://localhost:8080`

3. Add tag so it can be pushed to Docker Hub: `docker tag k8s-by-example-lesson1 {your username}/k8s-by-example-lesson1`

4. Push to Docker Hub: `docker push {your username}/k8s-by-example-lesson1`