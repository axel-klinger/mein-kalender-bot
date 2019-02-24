# Mein Kalender Bot

Das Ziel ist ein Chatbot, der mir Auskunft über Ferienzeiten, Müllabfuhrtermine und andere Ereignisse liefert.

Auf Basis dieses [Youtube Videos](https://www.youtube.com/watch?v=xu6D_vLP5vY&t=3848s)
Quellen des Beispiels auf [GitHub](https://github.com/JustinaPetr/Weatherbot_Tutorial)

## Voraussetzung

* Python 3 (3.6.5_1) // 3.7.2 macht Probleme
* pip3 install rasa-nlu
* pip3 install rasa-nlu-trainer
// * pip3 install tensorflow (1.12.0) // 1.13.0rcX nicht kompatibel mit rasa_core
* pip3 install rasa_core
* pip3 install rasa_core_sdk
* pip3 install spacy
* python3 -m spacy download de

## Kurzanleitung
* Intents trainieren und testen
```
python3 kalender-intent-training.py
```
* kalender-actions.py als service starten
```
python3 -m rasa_core_sdk.endpoint --actions kalender-actions
```
* Dialoge / Stories initial trainieren
```
python3 kalender-dialogue-training.py
```
* Dialoge / Stories interaktiv trainieren
```
python3 kalender-interactive-training.py
```
* Bot testen
```
python3 kalender-bot.py
```

## Die einzelnen Schritte im Detail
### Verstehen was der Anwender will - Trainieren des Modells
Anhand von Beispielsätzen lernt der Bot was der Anwender will und wovon er redet. Durch das Training kann der Bot auch bei abweichenden Formulierungen oder Rechtschreibfehlern die richtige Intention erkennen und auch neue Begriffe richtig einordnen ohne dass jede mögliche Abweichung explizit angegeben wird.   

1. [data/data.json](data/data.json) anlegen und mit **rasa-nlu-trainer** befüllen

```
rasa-nlu-trainer
```

Die Trainingdaten
* ordnen Beispielsätze den Intentionen zu
* klassifizieren einzelne Begriffe in den Sätzen


2. [config.json](config.json) erstellen

Die Konfiguration
* beschreibt die Trainings-Pipeline
* definiert die Daten für die Eingabe
* definiert einen Ordner für die Ausgabe des Modells


3. Skript [kalender-intent-training.py](kalender-intent-training.py) erstellen und ausführen -> erzeugt das Modell im Ordner models (die Modelle werden nicht versioniert)

```
python3 kalender-intent-training.py
```

Der Trainer
* nimmt Daten und Konfiguration
* generiert und speichert ein Modell
* lädt das Modell
* parsed die Eingabe und liefert die Intention


### Richtig reagieren - Dialog Management

Je nach Eingabe soll der Bot nach weiteren Details fragen oder antworten.

#### Definition der Domäne

4. [kalender-domain.yml](kalender-domain.yml) erstellen

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

#### Custom actions definieren

5. [kalender-actions.py](kalender-actions.py) erstellen

Custom actions werden als service ausgeführt

6. [endpoints.yml](endpoints.yml) erstellen

Custom action service starten

```
python3 -m rasa_core_sdk.endpoint --actions kalender-actions
```

#### Geschichten erzählen - Definition der Stories

In den Stories werden die Elemente des Dialogs beispielhaft miteinander verbunden. Durch interaktives Training lernt der Bot richtig zu reagieren.

Die Stories beschreiben mögliche Wege in einem FlowChart für den Dialog.

Zunächst werden nur einfache Reaktionen formuliert, ohne Bezug auf Objekte im Kontext.

7. [data/stories.md](data/stories.md) erstellen

#### Ein Basis-Dialogmodell trainieren

Auf der Basis von *stories* und *domain* werden Fake-Sätze erstellt.

Initiales Training des Dialogs

8. [policy-config.yml](policy-config.yml) für neuere Version von rasa_core ausgelagert **<- kann wohl weg? -> TESTEN**

9. [kalender-dialogue-training.py](kalender-dialogue-training.py) erstellen und ausführen

```
python3 kalender-dialogue-training.py
```

Interaktives Training - generiert Stories und hängt sie an die initialen stories an.

10. [kalender-interactive-training.py](kalender-interactive-training.py) erstellen und ausführen

```
python3 kalender-interactive-training.py
```

**Test des Bots**

11. [kalender-bot.py](kalender-bot.py)
