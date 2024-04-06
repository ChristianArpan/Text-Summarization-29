import requests
from flask import Flask,render_template,request,url_for
from flask import request as req


app = Flask(__name__)

@app.route("/", methods=["GET", "POST"]) 
def Index():
    return render_template("index.html")
    
@app.route("/Summarize", methods=["GET", "POST"])
def Summarize():
    # Your function implementation
    if req.method == "POST":
        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 = "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"

        API_URL = "https://api-inference.huggingface.co/models/sshleifer/distilbart-cnn-12-6"
        headers = {"Authorization": f"Bearer {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}"}

        data =request.form["data"]

        maxL = int(req.form["maxL"])
        minL = maxL//4
        

        def query(payload):
            response = requests.post(API_URL, headers=headers, json=payload)
            return response.json()

        output = query({
            "inputs": data,
            "parameters": {"min_length": minL, "max_length": maxL},  # Corrected parameter name
        })[0]['summary_text']

        return render_template("index.html",result=output)
    else:
        return render_template("index.html")

if __name__ == '__main__':
    app.debug=True
    app.run()




    