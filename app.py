# libraries used in this project
from google import genai
from flask import Flask, render_template, request
import dotenv as dotenv
import os
import markdown
app = Flask(__name__)
dotenv.load_dotenv()
# API key 
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
# route for the page where users can input the topic they want to study
@app.route("/Topic")
def Topic():
    return render_template("index.html")
#route for the page where the response from the Gemini API will be displayed
@app.route("/study", methods=["POST"])
def study():
    topic = request.form.get("topic")
    response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=f"Explain the topic of {topic} in simple way and in bullet points and give 3 questions to test understanding of the topic."
)
    return render_template("study.html", response=markdown.markdown(response.text))
if __name__ == "__main__":
    app.run(debug=True)