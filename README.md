# flask-socketio-guacamole

A flask-socketio based web service to achieve remote desktop work with guacd together.

###Useage

---

- You need to have a guacamole server (guacd), follow the step given by the official: 
https://guacamole.apache.org/doc/gug/installing-guacamole.html or install with docker
 "guacamole/guacd". Highly recommended that to use docker.
 
- Get the code from this repository by 
'git clone https://github.com/MUYUSY/flask-socketio-guacamole.git' or 'download zip'.

- Setting the guacd host and port in config.py

- Run 'python app.py' just like a normal flask app and go to "http://localhost:5000"

- Easy to use with just input the parameters.


###Notes

flask-socketio-guacamole is licensed under the MIT License.
Appreciate to [pygocamole](https://github.com/mohabusama/pyguacamole) and 
[guacamole-client/guacamole-common-js](https://github.com/apache/guacamole-client/tree/master/guacamole-common-js).

   

