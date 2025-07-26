import requests
import json

def emotion_detector(text_to_analyse):
    """
        emotion detector
    """
    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    Headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    payload = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(URL, json=payload, headers=Headers)

    formatted_response = json.loads(response.text)
    tmp1 = formatted_response['emotionPredictions']
    tmp2 = tmp1[0]
    
    anger_score = tmp2['emotion']['anger']
    disgust_score = tmp2['emotion']['disgust']
    fear_score = tmp2['emotion']['fear']
    joy_score = tmp2['emotion']['joy']
    sadness_score = tmp2['emotion']['sadness']
    dominant_score = "dominant_score"

    dominant = -1
    dominant_emotion = None
    if anger_score > dominant:
        dominant = anger_score
        dominant_emotion = "anger"
    if disgust_score > dominant:
        dominant = disgust_score
        dominant_emotion = "disgust"
    if fear_score > dominant:
        dominant = fear_score
        dominant_emotion = "fear"
    if joy_score > dominant:
        dominant = joy_score
        dominant_emotion = "joy"
    if sadness_score > dominant:
        dominant = sadness_score
        dominant_emotion = "sadness"
    
    if response.status_code == 400:
        return { 'anger': None, 'disgust': None, 'fear': None, 'joy': None, 'sadness': None, 'dominant_emotion': None}     
    
    return { 'anger': anger_score, 'disgust': disgust_score, 'fear': fear_score, 'joy': joy_score, 'sadness': sadness_score, 'dominant_emotion': dominant_emotion }