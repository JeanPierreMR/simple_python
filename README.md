# Simple flask app using a dockerfile

### How to use

Be sure to have the port 5000 available and connection to the internet to pull the image

```
docker pull jeanmr/simple_app

docker run -p5000:5000 jeanmr/simple_app
```

The final result should be in localhost, port 5000

localhost:5000 or http://127.0.0.1:5000/


It can be built again running this inside the folder:

```
docker build -t jeanmr/simple_app .
```
