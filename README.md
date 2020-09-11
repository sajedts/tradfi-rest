# tradfri-rest
Simple REST API server for controlling IKEA Trådfri lights.

### Building and running the server

Build the Docker image with:

```
docker build  -t tradfri-rest:latest .
```

Run the server with:

```
docker run -d --restart=always -p 5000:5000 -e GATEWAY_IP=<your_gateway_ip> -e GATEWAY_KEY=<your_gateway_key> tradfri-rest
```

### Set light brightness

    Sets light brightness.

* **URL**

  /lights/:light_name/:brightness_level

* **Method:**

  `POST`
  
*  **URL Params**

   **Required:**
 
   `light_name` - Light name set in Tradfri app

   `brightness_level` - Light brightness from 0 to 254

* **Success Response:**

  * **Code:** 200 <br />
 
* **Error Response:**

  * **Code:** 404 NOT FOUND <br />


### Set brightness for all lights

    Loop trough all lghts and sets their brightness

* **URL**

  /lights/all/:brightness_level

* **Method:**

  `POST`
  
*  **URL Params**

   **Required:**
 

   `brightness_level` - Light brightness from 0 to 254

* **Success Response:**

  * **Code:** 200 <br />
 
