# Mein Kalender Bot

Das Ziel ist ein Chatbot, der mir Auskunft über Ferienzeiten, Müllabfuhrtermine und andere Ereignisse liefert.

Auf Basis dieses [Youtube Videos](https://www.youtube.com/watch?v=xu6D_vLP5vY&t=3848s)
Quellen des Beispiels auf [GitHub](https://github.com/JustinaPetr/Weatherbot_Tutorial)

## Voraussetzung

* Python 3 (3.6.5_1) // 3.7.2 macht Probleme
* pip3 install rasa-nlu
* pip3 install rasa-nlu-trainer
* pip3 install tensorflow (1.12.0) // 1.13.0rcX nicht kompatibel mit rasa_core
* pip3 install rasa_core

## Kurzanleitung
* Intents trainieren
```
python3 kalender-training.py
```
* Intent-Erkennung testen
```
python3 kalender-training-test.py
```
* Dialoge / Stories initial trainieren
```
python3 -m rasa_core.train -d kalender-domain.yml -s data/stories.md -o models/dialogue -c policy-config.yml
```
* Dialoge / Stories interaktiv trainieren
```
python3 -m rasa_core.train interactive -d kalender-domain.yml -s data/stories.md -o models/dialogue -c policy-config.yml
```
* ... ggf. final trainieren ??? ...

* Bot testen
```
python3 kalender-bot.py
```

## Die einzelnen Schritte im Detail
### Verstehen was der Anwender will - Trainieren des Modells
Anhand von Beispielsätzen lernt der Bot was der Anwender will und wovon er redet. Durch das Training kann der Bot auch bei abweichenden Formulierungen oder Rechtschreibfehlern die richtige Intention erkennen und auch neue Begriffe richtig einordnen ohne dass jede mögliche Abweichung explizit angegeben wird.   

1. [data/data.json](data/data.json) anlegen und mit rasa-nlu-trainer befüllen

```
Die Trainingdaten
* ordnen Beispielsätze den Intentionen zu
* klassifizieren einzelne Begriffe in den Sätzen
```

2. [config.json](config.json) erstellen

```
Die Konfiguration
* beschreibt die Trainings-Pipeline
* definiert die Daten für die Eingabe
* definiert einen Ordner für die Ausgabe des Modells
```

3. Skript [kalender-training.py](kalender-training.py) erstellen und ausführen -> erzeugt das Modell im Ordner models (die Modelle werden nicht versioniert)

```
Der Trainer
* nimmt Daten und Konfiguration
* generiert und speichert ein Modell
```

4. Skript [kalender-training-test.py](kalender-training-test.py) anlegen und ausführen -> hier wird die Intention der Aussage (intent) anhand eines statischen Beispiels getestet. Das Beispiel verwendet sowohl einen anderen Satzbau, als auch einen unbekannten Ferienbegriff und Intention und Objekt werden dennoch richtig erkannt.

```
Der Interpreter
* lädt das Modell
* parsed die Eingabe und liefert die Intention
```
### Richtig reagieren - Dialog Management

Je nach Eingabe soll der Bot nach weiteren Details fragen oder antworten.

5. [kalender-domain.yml](kalender-domain.yml) erstellen

#### Definition der Domäne

**slots - Platzhalter im Kontext für Objekte und ihre Datentypen**

Slots halten Objekte (entities) im Kontext fest. Wenn ich beispielsweise sage, "Ich habe einen Hund" und "er ist schwarz", dann steht im Kontext, dass wir von (m)einem Hund reden, und im zweiten Satz beziehen wir uns auf den Hund mit "er".

**intents - Intentionen oder was der Anwender will**

Die Intention sagt, was ich von dem Bot will, ohne das *wie ich es formuliert habe*.

Die Intents entsprechen denen aus data/data.json.

**entities - Objekte über die wir reden**

Die Entitäten sind die Objekte oder Begriffe über die wir reden.

**templates - Vorlagen für die Ausgabe**

Mögliche Formen der Antworten auf bestimmte Eingaben (Intentionen). *Antworten und Nachfragen zu Details.* Alternative Antworten, damit es natürlicher wirkt.

**actions - Triggern von Templates und Logik**

Jedes Template wird durch eine Aktion aktiviert.

Jede eigentliche Beantwortung eines Anliegens, durch Logik oder Abfrage aus dem Web, wird in einer *custom action* als separates Python Skript formuliert.

7. [kalender-actions.py](kalender-actions.py) erstellen

#### Geschichten erzählen - Definition der Stories

In den Stories werden die Elemente des Dialogs beispielhaft miteinander verbunden. Durch interaktives Training lernt der Bot richtig zu reagieren.

Die Stories beschreiben mögliche Wege in einem FlowChart für den Dialog.

Zunächst werden nur einfache Reaktionen formuliert, ohne Bezug auf Objekte im Kontext.

7. [data/stories.md](data/stories.md) erstellen

#### Ein Basis-Dialogmodell trainieren

Auf der Basis von *stories* und *domain* werden Fake-Sätze erstellt.

Initiales Training des Dialogs

8. [policy-config.yml](policy-config.yml) für neuere Version von rasa_core ausgelagert

```
python3 -m rasa_core.train \
        -d kalender-domain.yml \
        -s data/stories.md \
        -o models/dialogue \
        -c policy-config.yml
```

Interaktives Training - generiert Stories und hängt sie an die initialen stories an.

```
python3 -m rasa_core.train interactive \
        -d kalender-domain.yml \
        -s data/stories.md \
        -o models/dialogue \
        -c policy-config.yml
```

Finales Training ...

10. [kalender-dialog-final-training.py](kalender-dialog-final-training.py)

... und **Test des Bots**

11. [kalender-bot.py](kalender-bot.py)

### Die Anwendungen

... mit Bot als (Flask?) Server ...

* vom Smartphone via Sprachein/ausgabe
* in Facebook im Messanger
* im Web als iframe
