import requests
import json

def emotion_detector(text_to_analyse):
    # URL of the sentiment analysis service
    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    # Custom header specifying the model ID for the sentiment analysis service
    Headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

     # Constructing the request payload in the expected format
    payload = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(URL, json=payload, headers=Headers)

    # Parsing the JSON response from the API
    formatted_response = json.loads(response.text)

    #process theresponse
    tmp1 = formatted_response['emotionPredictions']
    tmp2 = tmp1[0]
    
    # Extracting emotions label and score from the response
    anger_score = tmp2['emotion']['anger']
    disgust_score = tmp2['emotion']['disgust']
    fear_score = tmp2['emotion']['fear']
    joy_score = tmp2['emotion']['joy']
    sadness_score = tmp2['emotion']['sadness']

    dominant_score = "dominant_score"
    dominant = -1
    if anger_score > dominant:
        dominant = anger_score
        dominant_emotion = "anger_score"
    if disgust_score > dominant:
        dominant = disgust_score
        dominant_emotion = "disgust_score"
    if fear_score > dominant:
        dominant = fear_score
        dominant_emotion = "fear_score"
    if joy_score > dominant:
        dominant = joy_score
        dominant_emotion = "joy_score"
    if sadness_score > dominant:
        dominant = sadness_score
        dominant_emotion = "sadness_score"
    
    
    return {
            'anger': anger_score, 
            'disgust': disgust_score, 
            'fear': fear_score, 
            'joy': joy_score, 
            'sadness': sadness_score, 
            'dominant_emotion': dominant_emotion 
    }