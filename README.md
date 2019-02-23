## Trainieren eines ersten einfachen Modells

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
