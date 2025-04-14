from flask import Flask, render_template, request
app = Flask(__name__)
def chat_responce(que):
    if (que.lower() == "hi") or (que.lower() == "hello"):
        return "Hello Friend , MAT-E here ! . How can I help You ?"

    elif (que.lower() == "category"):
        return "Food , Electronics , Fashion , Jewellry , etc."

    elif (que.lower() == "bye"):
        return "Thank you , Bye !"
    
    else:
        return "Sorry Can't Understand , Please Retry!!"

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(chat_responce(userText))
    


if __name__ == "__main__":
    app.run(debug=True)