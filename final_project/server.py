from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    english_text = request.form.get('english_text')
    translated_text = machinetranslation.english_to_french(english_text)
    return "Translated text to French"

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
     french_text = request.form.get('french_text')
    translated_text = machinetranslation.french_to_english(french_text)
    return "Translated text to English"

@app.route("/")
def renderIndexPage():
    #code to render template
     return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
