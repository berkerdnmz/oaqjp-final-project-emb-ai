'''Server with Exception Handling'''
from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emotion_analyzer():
    ''' Function Emotion Analyzer '''
    text_to_analyze = request.args.get('textToAnalyze')

    response = emotion_detector(text_to_analyze)

    anger_score = response['anger']
    disgust_score = response['disgust']
    fear_score = response['fear']
    joy_score = response['joy']
    sadness_score = response['sadness']
    dominant_emotion = response['dominant_emotion']

    if dominant_emotion is None:
        return "<b>Invalid text! Please try again!</b>"

    response = (
    f"For the given statement, the system response is "
    f"'anger': {anger_score}, 'disgust': {disgust_score}, "
    f"'fear': {fear_score}, 'joy': {joy_score}, "
    f"and 'sadness': {sadness_score}. "
    f"Dominant Emotion is <b>{dominant_emotion}</b>."
    )
    return response

@app.route("/")
def render_index_page():
    '''Routing to Index'''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
