# Image-to-Base64-and-md5

## How to use it
### 1. By uploading image
  * Go to this [link](https://image-api-invoid.herokuapp.com/).
  * Click on Choose and select an image file from your system.
  * Click on Submit.
  * It will return a json file with md5 hash and base64 data. 
  
  ```json
  {
     "md5" : "value",
     "base64" : "value",
  }
  ```
  
### 2. By URL
  * Replace the value of url to the link of an image in the below link.
  ```
  https://image-api-invoid.herokuapp.com/api/?url=https://example.com/example.png
  ```
  It will return the json with both the data.
  
  

  
