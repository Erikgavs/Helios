from flask import Flask
from reporter import enviar_mensaje # Import the reporter function from the reporter file

app = Flask(__name__)

@app.route("/helios", methods=["GET"]) # /helios endpoint
def mensaje():
    resultado = enviar_mensaje()
    return {"status": "ok", "resultado": resultado}, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
