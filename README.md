# Mein Kalender Bot

## Voraussetzung

* Python 3
* pip3 install rasa-nlu
* pip3 install rasa-nlu-trainer
* pip3 install tensorflow

## Verstehen was der Anwender will - Trainieren des Modells
Anhand von Beispielsätzen lernt der Bot was der Anwender will und wovon er redet. Durch das Training kann der Bot auch bei abweichenden Formulierungen oder Rechtschreibfehlern die richtige Intention erkennen und auch neue Begriffe richtig einordnen ohne dass jede mögliche Abweichung explizit angegeben wird.   

1. data/data.json anlegen und mit rasa-nlu-trainer befüllen

```
Die Trainingdaten
* ordnen Beispielsätze den Intentionen zu
* klassifizieren einzelne Begriffe in den Sätzen
```

2. config.json erstellen

```
Die Konfiguration
* beschreibt die Trainings-Pipeline
* definiert die Daten für die Eingabe
* definiert einen Ordner für die Ausgabe des Modells
```

3. Skript kalender-training.py erstellen und ausführen -> erzeugt das Modell im Ordner models (die Modelle werden nicht versioniert)

```
Der Trainer
* nimmt Daten und Konfiguration
* generiert und speichert ein Modell
```

4. Skript kalender-training-test.py anlegen und ausführen -> hier wird die Intention der Aussage (intent) anhand eines statischen Beispiels getestet.

```
Der Interpreter
* lädt das Modell
* parsed die Eingabe und liefert die Intention
```
## Richtig reagieren - Dialog Management

Je nach Eingabe soll der Bot nach weiteren Details fragen oder antworten. Die Gesprächsführung kann in einem Flowchart skizziert werden.
