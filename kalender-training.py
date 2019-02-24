from rasa_nlu.training_data import load_data
from rasa_nlu.model import Trainer
from rasa_nlu import config
from rasa_nlu.model import Metadata, Interpreter

def train_kalender(data, configs, model_dir):
	training_data = load_data(data)
	trainer = Trainer(config.load(configs))
	trainer.train(training_data)
	model_directory = trainer.persist(model_dir, fixed_model_name = 'kalenderbot')

def run_nlu():
	interpreter = Interpreter.load('./models/nlu/default/kalenderbot')
	print(interpreter.parse(u"Kannst du mir sagen wann die Weihnachtsferien sind."))

if __name__ == '__main__':
	train_nlu('./data/data.json', 'config.json', './models/nlu')
	run_nlu()
