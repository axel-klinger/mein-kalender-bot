# Mein Kalender Bot

Auf Basis von Python und Rasa NLU.

## Trainieren eines ersten einfachen Modells

1. data/data.json anlegen und mit rasa-nlu-trainer befüllen
2. config.json erstellen
3. Skript kalender-training.py erstellen und ausführen -> erzeugt das Modell im Ordner models (die Modelle werden nicht versioniert)
4. Skript kalender-training-test.py anlegen und ausführen -> hier wird die Intention der Aussage (intent) anhand eines statischen Beispiels getestet.
