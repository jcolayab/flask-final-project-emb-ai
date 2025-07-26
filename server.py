''' Executing this function initiates the application of sentiment
    analysis to be executed over the Flask channel and deployed on
    localhost:5000.
'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_detector():
    """
    Extracts input text from query parameters and analyzes its emotional tone
    using the emotion_detector function. Returns a formatted string of emotion
    scores and the dominant emotion.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    # Pass the text to the sentiment_analyzer function and store the response
    response = emotion_detector(text_to_analyze)

    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']

    if dominant_emotion is None:
        return "Invalid text! Please try again"

    return (
    f"For the given statement, the system response is 'anger': {anger}, "
    f"'disgust': {disgust}, 'fear': {fear}, 'joy': {joy}, 'sadness': {sadness}. "
    f"The dominant emotion is {dominant_emotion}"
)


@app.route("/")
def render_index_page():
    """
    Renders the main HTML index page for the emotion detection web app.
    Acts as the landing route for the application UI.
    """

    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
