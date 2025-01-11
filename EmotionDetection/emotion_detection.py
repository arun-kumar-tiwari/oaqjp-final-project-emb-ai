import requests
import json

def emotion_detector(text_to_analyse):

    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyse } }

    response = requests.post(url, json=myobj, headers=header)
    
    if response.status_code == 200:
        formatted_response = json.loads(response.text)
        emotionPredictions = formatted_response['emotionPredictions'][0]['emotion']
        dominant_emotion = None
        score = -1
        for key, val in emotionPredictions.items():
            if float(val) > score:
                dominant_emotion = key
                score = float(val)

        emotion = {
            'anger': emotionPredictions['anger'],
            'disgust': emotionPredictions['disgust'],
            'fear': emotionPredictions['fear'],
            'joy': emotionPredictions['joy'],
            'sadness': emotionPredictions['sadness'],
            'dominant_emotion': dominant_emotion
        }
    else:
        emotion = {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
    
    return emotion




# print(emotion_detector("I love this new technology."))


