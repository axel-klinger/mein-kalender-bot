from rasa_nlu.model import Interpreter

def predict_intent (text):
    interpreter = Interpreter.load('./models/nlu/default/kalenderbot')
    print (interpreter.parse(text))

predict_intent("Wann sind die Herbstferien")
