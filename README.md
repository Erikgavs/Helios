# ✨Elendil

Elendil is a bot designed to send information about the resources of the user server to him, the script uses te smtp library to send emails.

The script is configured to send you a email at 10 and at 19 o'clock, this allows you to know the status of your server and follow-up the state.

Also the script can easly adapt to new features.


## ⚙️Features
- N8n compatibility
- Execute local commands
- Psutil library 
- Public IP info


## 🤖n8n (opcional)
We can use this script with n8n making petitions to **/helios** endpoint. 
## 🔐.env
To make this script functional we need to have a .env file.

in the .env file we have to put **3 parameters**, one for the person that sends the email, other parameter for the one who recive the email and the last parameter for the password of google app.

## 🏠Flask instalation

## 🛖Enviorenment

Before we start we need to create a environment in python.

```
python3 -m venv nombre-entorno
source nombre-entorno/bin/activate
```
Now we need to install the dependences (in our environment).
```
pip install -r requirements.txt
```

## ⚔️Execution
To start this script que need to execute main.py with the next command.

```
nohup python3 main.py &
```
## 🧙‍♂️Authors

- [@Erikgavs](https://www.github.com/Erikgavs)
