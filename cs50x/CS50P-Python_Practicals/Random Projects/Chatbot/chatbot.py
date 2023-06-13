import random
import json
import pickle
import numpy as np

import nltk
from nltk.stem import WordNetLemmatizer

from tensorflow.keras.models import load_model

# Initialize WordNet lemmatizer for word normalization
lemmatizer = WordNetLemmatizer()

# Load intents JSON file
with open("intents.json", "r") as file:
    intents = json.load(file)

# Load preprocessed data from pickle files
words = pickle.load(open("words.pkl", "rb"))
classes = pickle.load(open("classes.pkl", "rb"))
model = load_model("chatbot_model.h5")


try:
    # Function to clean up user input sentence
    def clean_up_sentence(sentence):
        sentence_words = nltk.word_tokenize(sentence)
        sentence_words = [lemmatizer.lemmatize(word) for word in sentence_words]
        return sentence_words


    # Function to convert user input sentence to bag of words representation
    def bag_of_words(sentence):
        sentence_words = clean_up_sentence(sentence)
        bag = [0] * len(words)
        for w in sentence_words:
            for i, word in enumerate(words):
                if word == w:
                    bag[i] = 1
        return np.array(bag)


    # Function to predict the class of user input sentence
    def predict_class(sentence):
        bow = bag_of_words(sentence)
        res = model.predict(np.array([bow]))[0]
        ERROR_THRESHOLD = 0.25
        results = [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]

        results.sort(key=lambda x: x[1], reverse=True)
        return_list = []
        for r in results:
            return_list.append({"intent": classes[r[0]], "probability": str(r[1])})
        return return_list


    # Function to get a random response for a given intent
    def get_response(intents_list, intents_json):
        tag = intents_list[0]["intent"]
        list_of_intents = intents_json["intents"]
        result = "No response found."
        for i in list_of_intents:
            if i["tag"] == tag:
                result = random.choice(i["responses"])
                break
        return result


    # Start of the chatbot
    print("GO! Bot is running!")

    while True:
        # Get user input
        message = input("")

        # Predict the intent of user input
        ints = predict_class(message)

        # Get a response based on the predicted intent
        res = get_response(ints, intents)

        # Print the response
        print(res)

except KeyboardInterrupt:
    # Handle KEyboard Interrupt exception
    print("Keyboard interrupt detected. Exiting...")
