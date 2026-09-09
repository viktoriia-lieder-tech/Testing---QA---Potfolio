__Was habe ich gelernt:__

# Was ist Test-Treiber und test-Halter in QA Testing:


Test Halter und Test Treiber in qa testing

Testtreiber (Test Driver) und Testplatzhalter (Test Stub / Stubs) sind Hilfskomponenten, die beim Softwaretesten (insbesondere bei Komponenten- und Integrationstests) verwendet werden, um fehlende Teile eines Systems zu simulieren

-------------
# Testtreiber (Test Driver):

Ein Testtreiber ist ein kleines Programm oder Skript, das ein zu testendes Modul aufruft und steuert.

- Funktion: Er ersetzt das übergeordnete Modul (das Hauptprogramm oder den Aufrufer), das in der echten Anwendung die zu testende Komponente ansprechen würde.

- Aufgabe: Er übergibt Testdaten an das Testobjekt, startet den Aufruf und nimmt das Ergebnis (den Rückgabewert) entgegen, um es zu prüfen.

- Einsatz: Notwendig, wenn eine untergeordnete Komponente von unten nach oben (Bottom-Up) getestet werden soll, aber das Hauptprogramm noch nicht existiert.


# Testplatzhalter (Test Stub / Stub)

Ein Testplatzhalter (auch Stub oder manchmal ungenau als „Halter“ bezeichnet) simuliert das Verhalten einer Komponente, die von dem zu testenden Modul aufgerufen wird.

- Funktion: Er ersetzt ein untergeordnetes Modul, das die zu testende Einheit benötigt (z. B. eine Datenbank, eine Schnittstelle oder einen anderen Dienst).

- Aufgabe: Er gibt auf eine Anfrage vordefinierte oder feste Werte zurück, ohne die echte, komplexe Logik auszuführen.

- Einsatz: Notwendig beim Testen von oben nach unten (Top-Down), wenn die benötigten Nachbarmodule oder externen Services noch nicht fertig oder verfügbar sind.


# Vergleich der Rollen:
- Richtung: Der Treiber sitzt über dem Testobjekt und ruft es aktiv auf. Der Platzhalter (Stub) sitzt unter oder neben dem Testobjekt und wird von diesem aufgerufen.

- Zweck: Treiber ermöglichen den Test von Modulen ohne fertiges Ober- oder Hauptsystem. Platzhalter isolieren das Testobjekt von fehlenden oder langsamen Abhängigkeiten (wie echten Servern)

# Ziel eines jeden Softwaretesters ist die Effektivität und Effizienz des Testdesigns kontinuierlich zu steigern. 
Ein Weg dies zu erreichen ist eine Testautomatisierung. 
Dabei sind folgende Begriffe wichtig:

**Testrahmen:** enthält das Testobjekt
**Testtreiber:** Skript, das die Schnittstellenaufrufe absetzt, das Testobjekt aufruft und dessen Reaktion entgegennimmt

**Platzhalter:**
**Stub:** simulieren das Ein-/ Ausgabeverhalten eines aufrufenden Programmteiles
**Dummy:** besitzt Funktionalitäten und ist ein nahezu vollwertiger Ersatz für eine echte Implementierung eines weiteren Komponente
**Mock:** wie Dummy aber noch zusätzliche Funktionalität für Testzwecke
**Monitor:** stellt Informationen für Testzwecke zur Verfügung, z.B. Schnittstelleninformationen, Resourcenauslastung


#Code für Test Treiber und für Test Halter:
# Beschreibung:
_Beispiel für einen Testplatzhalter (Stub)_
Das Testobjekt benötigt aktuelle Steuersätze von einem externen Server (TaxService). Da dieser Server im Test nicht verfügbar ist, liefert der Stub stattdessen einen festen Wert (z. B. immer 19% Steuern).

```
# Das Testobjekt (Die Komponente, die wir testen wollen)
class PriceCalculator:
    def __init__(self, tax_service):
        self.tax_service = tax_service  # Abhängigkeit wird übergeben

    def calculate_total(self, net_price):
        # Ruft die Steuer-Komponente auf
        tax_rate = self.tax_service.get_current_tax_rate()
        return net_price * (1 + tax_rate)

# DER TESTPLATZHALTER (STUB)
# Er simuliert den echten, komplexen Steuer-Service im Internet
class TaxServiceStub:
    def get_current_tax_rate(self):
        return 0.19  # Liefert einfach immer fest 19% zurück, ohne das Internet zu nutzen

```


#Code für Test Treiber und für Test Driver:
#Beispiel für einen Testtreiber (Driver)
# Beschreibung:
_Beispiel für einen Testhalter (Driver)_
Das Hauptprogramm der Software existiert noch nicht. 
Wir bauen einen Testtreiber, der die Rolle des Hauptprogramms übernimmt, Testdaten einspeist und das Ergebnis prüft.

```

# DER TESTTREIBER (DRIVER)
# Er steuert den Testablauf, übergibt Daten und prüft das Ergebnis
def run_price_calculator_test():
    print("--- Starte Testtreiber ---")
    
    # Vorbereitung: Wir nutzen den Stub von oben
    stub_service = TaxServiceStub()
    test_object = PriceCalculator(stub_service)
    
    # 1. Testfall: Nettopreis = 100 Euro
    input_value = 100.0
    expected_output = 119.0
    
    # Der Treiber ruft das Testobjekt aktiv auf
    actual_output = test_object.calculate_total(input_value)
    
    # Der Treiber prüft das Ergebnis
    if actual_output == expected_output:
        print(f"Test BESTANDEN: 100€ Netto ergaben {actual_output}€ Brutto.")
    else:
        print(f"Test FEHLGESCHLAGEN: Erwartet {expected_output}, aber erhalten {actual_output}")

# Ausführen des Treibers
run_price_calculator_test()

```

# Zusammenfssung:
1. TaxServiceStub ist der Halter. 
- Er verhält sich passiv und wartet darauf, dass das Testobjekt ihn nach Daten fragt.
2. run_price_calculator_test ist der Treiber. 
- Er agiert aktiv, startet den Test, füttert das Testobjekt mit Daten und kontrolliert das Ergebnis.

# Das Framework als Testtreiber und Testplatzhalter
Beispiel mit dem unittest-Framework:

```
import unittest
from unittest.mock import MagicMock

# Das Testobjekt (Die Komponente, die wir testen wollen)
class PriceCalculator:
    def __init__(self, tax_service):
        self.tax_service = tax_service

    def calculate_total(self, net_price):
        tax_rate = self.tax_service.get_current_tax_rate()
        return net_price * (1 + tax_rate)


# DAS FRAMEWORK AGIERT ALS TESTTREIBER
class TestPriceCalculator(unittest.TestCase):

    def test_calculate_total_with_standard_tax(self):
        # 1. SETUP DER PLATZHALTER (STUB)
        # MagicMock() ersetzt die echte Steuer-Klasse vollständig
        tax_service_stub = MagicMock()
        
        # Wir definieren fest, was der Stub zurückgeben soll (wie ein Halter)
        tax_service_stub.get_current_tax_rate.return_return = 0.19
        
        # Testobjekt mit dem Stub initialisieren
        calculator = PriceCalculator(tax_service_stub)

        # 2. AUSFÜHRUNG (Der Treiber ruft das Testobjekt auf)
        result = calculator.calculate_total(100.0)

        # 3. PRÜFUNG (Der Treiber validiert das Ergebnis)
        self.assertEqual(result, 119.0)

if __name__ == '__main__':
    # Startet den Testtreiber des Frameworks
    unittest.main()

```

# Zusammenfassung:
## Was übernimmt welche Rolle?

# Der Testtreiber (unittest):
1. Die Klasse TestPriceCalculator und die Methode unittest.main() sind der Treiber.
2. Das Framework sucht automatisch nach Methoden, die mit test_ beginnen.
3. Es führt den Code aus und füttert das Testobjekt (calculator) mit Daten.
4. Die Methode self.assertEqual() prüft das Ergebnis und meldet Erfolg oder Fehler an die Konsole.

# Der Testplatzhalter (MagicMock):
1. Anstatt eine eigene Klasse TaxServiceStub zu schreiben, erstellen wir ein MagicMock()-Objekt.
2. Mit tax_service_stub.get_current_tax_rate.return_value = 0.19 zwingen wir diesen Platzhalter, immer 0.19 zu antworten, wenn er aufgerufen wird.
3. Das Testobjekt merkt nicht, dass es mit einer Fälschung arbeitet.


# Zweigüberdeckungstest ist als ein Unit Test in python dargestellt:
# Beschreibung:

- Ein Zweigüberdeckungstest (Branch Coverage Test) stellt sicher, dass jeder mögliche Weg (Zweig) einer Kontrollstruktur (wie if-else-Anweisungen) im Code mindestens einmal ausgeführt wird.

- Wir erweitern unser Beispiel um eine if-else-Bedingung: Produkte über 100 Euro erhalten einen Rabatt von 5%, Produkte darunter nicht. 
- Um eine 100%ige Zweigüberdeckung zu erreichen, benötigen wir zwei Testfälle (einen für den if-Zweig und einen für den else-Zweig).

Hier ist die Umsetzung als unittest in Python, bei dem das Framework als Treiber agiert und Mocks als Platzhalter genutzt werden.

```
import unittest
from unittest.mock import MagicMock

# Das Testobjekt mit zwei Zweigen (if / else)
class PriceCalculator:
    def __init__(self, tax_service):
        self.tax_service = tax_service

    def calculate_total(self, net_price):
        tax_rate = self.tax_service.get_current_tax_rate()
        
        # HIER SIND DIE ZWEI ZWEIGE:
        if net_price > 100.0:
            # Zweig 1: Rabatt gewähren
            net_price = net_price * 0.95  
        else:
            # Zweig 2: Kein Rabatt
            pass  

        return net_price * (1 + tax_rate)

```

# Der Unit Test für 100% Zweigüberdeckung
# Beschreibung:
Der Testtreiber (unittest) führt nun gezielt zwei Testmethoden aus, um beide Pfade komplett abzudecken.

```

class TestPriceCalculatorBranchCoverage(unittest.TestCase):

    def setUp(self):
        # Gemeinsamer Testplatzhalter (Stub) für alle Testfälle
        self.tax_service_stub = MagicMock()
        self.tax_service_stub.get_current_tax_rate.return_value = 0.19
        self.calculator = PriceCalculator(self.tax_service_stub)

    # TESTFALL 1: Aktiviert den ELSE-Zweig (Preis <= 100)
    def test_calculate_total_without_discount(self):
        # Netto 100€ -> Kein Rabatt -> 100 * 1.19 = 119€
        result = self.calculator.calculate_total(100.0)
        self.assertEqual(result, 119.0)

    # TESTFALL 2: Aktiviert den IF-Zweig (Preis > 100)
    def test_calculate_total_with_discount(self):
        # Netto 200€ -> 5% Rabatt = 190€ -> 190 * 1.19 = 226.10€
        result = self.calculator.calculate_total(200.0)
        self.assertAlmostEqual(result, 226.10, places=2)

if __name__ == '__main__':
    unittest.main()

```

# Zusammenfassung:

### test_calculate_total_without_discount: ###
Der Wert 100.0 sorgt dafür, dass die Bedingung net_price > 100.0 falsch ist. Der else-Zweig wird durchlaufen.

### test_calculate_total_with_discount: ###
Der Wert 200.0 sorgt dafür, dass die Bedingung wahr ist. Der if-Zweig wird durchlaufen und der Rabatt abgezogen.

### Da beide Testfälle erfolgreich durchlaufen, haben wir eine Zweigüberdeckung von 100% für diese Funktion erreicht. Das Framework steuert beide Tests als Treiber nacheinander an. ###