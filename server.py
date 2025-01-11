''' Executing this function initiates the application of emotion
    detector to be executed over the Flask channel and deployed on
    localhost:5000.
'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def set_emotion_detector():
    ''' This code receives the text from the HTML interface and 
        runs emotion detection over it using emotion_detector() function. 
        The output returned shows the emotions along with their scores 
        and dominant emotion, which is the emotion with the highest score for the provided text.
    '''
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    if response['dominant_emotion'] is None:
        msg = "<b>Invalid text! Please try again!</b>"
    else:
        msg = ''
        for key,val in response.items():
            if key == 'joy':
                msg = msg + "'" + key + "': " + str(val) + ", and "
            elif key == 'dominant_emotion':
                continue
            else:
                msg = msg + "'" + key + "': " + str(val) + ", "
        message_1 = "For the given statement, the system response is "
        message_2 = "The dominant emotion is " +  "<b>" + response['dominant_emotion'] + "</b>."
        msg = message_1 + msg + message_2
    return msg

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application page over the Flask channel'''
    return render_template('index.html')

if __name__ == "__main__" :
    app.run(debug=True)
