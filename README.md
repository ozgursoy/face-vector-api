# Face Vector API

A simple API service to save your face recognition vectors to database

See [face_recognition](https://github.com/ageitgey/face_recognition)

```sh
$ docker build -t face-vector-api:latest .
$ docker run -d -p 5000:5000 face-vector-api
$ curl localhost:5000/encodes/get?url=[IMAGE_URL]
```

If you wonder how to search on SQL

```sh
SELECT * from vectors 
ORDER BY 
      sqrt(
         power(v1 - will_be_tested_value1, 2) +
         power(v2 - will_be_tested_value2, 2) + 
         ...
         power(v128 - will_be_tested_value128, 2) + 
     )
```
Have Fun
