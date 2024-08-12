import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyse } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    anger_score = disgust_score = fear_score = joy_score = sadness_score = None
    dominant_emotion = None

    try:
        response = requests.post(url, json=myobj, headers=header)
        response.raise_for_status()
        
        formatted_response = response.json()

        if 'emotionPredictions' in formatted_response and formatted_response['emotionPredictions']:
            emotion_scores = formatted_response['emotionPredictions'][0].get('emotion', {})
            
            anger_score = emotion_scores.get('anger', None)
            disgust_score = emotion_scores.get('disgust', None)
            fear_score = emotion_scores.get('fear', None)
            joy_score = emotion_scores.get('joy', None)
            sadness_score = emotion_scores.get('sadness', None)
            
            dominant_emotion = max(emotion_scores, key=emotion_scores.get, default=None)
    except Exception as err:
        print(f"An unexpected error occurred: {err}")

    return {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }
