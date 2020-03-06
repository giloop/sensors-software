# Version pour capteurs PPD42NS, SDS011, DHT22, BMP180 et NEO-6M

Features:

* Fonctionnement simultané de plusieurs capteurs
* Configuration via WLAN (capteur comme point d'accès) possible
* Prise en charge des écrans OLED avec SSD1306
* Sélection de la ou des API auxquelles les données sont envoyées, y compris l'option de sortie des données au format CSV via USB
* utilisable avec ESP8266 (NodeMCU et cartes compatibles)

ToDo's:

* Optimisations (en fait toujours)
* nouveaux capteurs

Fichiers dans ce répertoire:

* airrohr-firmware.ino - code source du firmware actuel
* ext_dev.h - configuration de base des paramètres (WLAN, capteurs, API)
* html-content.h - sources et images HTML générales pour la sortie HTML et texte
* intl_xx.h - fichiers avec textes traduits pour l'internationalisation, 'xx' est le code ISO à 2 lettres de la 'langue'
* intl_template.h - modèle pour les traductions
* astyle.rc - modèle de formatage pour Astyle
* ppd42ns-wificonfig-ppd-sds-dht.spiffs.bin - Binaire avec un système de fichiers vide, pour supprimer la configuration, voir les instructions dans le wiki.

## WLAN Configuration

voir aussi la page wiki sur Github [configuration des capteurs](https://github.com/opendata-stuttgart/meta/wiki/Konfiguration-der-Sensoren)

Si le WLAN spécifié ne peut pas être atteint après 20 secondes, un point d'accès est mis en place qui peut être atteint via "Capteur de matière particulaire - \ [Sensor-ID \]". Une fois connecté à ce point d'accès, toutes les demandes doivent être redirigées vers la page de configuration. L'adresse directe de la page est [http://192.168.4.1/](http://192.168.4.1/).

Les éléments suivants peuvent être configurés:

* Nom et mot de passe WiFi
* Capteurs à lire
* Destinations d'envoi des données

Le point d'accès devrait être désactivé à nouveau après 10 minutes (actuellement ne fonctionne pas encore de manière stable).

## Enregistrer au format CSV

Les données peuvent être sorties au format CSV via USB. Pour cela, le débogage doit être défini sur 0 dans ext_def.h et dans la configuration WLAN afin que les données de sortie ne soient que les données du capteur. Lorsque l'ESP8266 est redémarré, seuls quelques caractères apparaissent qui représentent l'état de démarrage.

## Câblage

* Câblage SDS et DHT: [nodemcu v3 Schéma sds011.jpg](https://raw.githubusercontent.com/opendata-stuttgart/meta/master/files/nodemcu-v3-schaltplan-sds011.jpg)

## Logiciel requis (version testée entre parenthèses et type de licence)

* [Arduino IDE](https://www.arduino.cc/en/Main/Software) (Version 1.8.5) (GNU Lesser General Public License v2.1)
* [ESP8266 pour Arduino](http://arduino.esp8266.com/stable/package_esp8266com_index.json) (IMPORTANT: version 2.3.0)

### Paramètres IDE Arduino

* Carte: NodeMCU 1.0 (modules ESP-12E)
* Fréquence du processeur: 80 MHz
* Taille du flash: 4M (3M SPIFFS)

De "ESP pour Arduino 2.4":

* Port de débogage: désactivé
* Niveau de débogage: NoAssert-NDEBUG
* Variante lwIP: v1.4 Bande passante supérieure (pré-construction)
* Effacer Flash: uniquement croquis

### Bibliothèques utilisées (pour ESP8266)

Inclus dans Arduino:

* Câble (GNU Lesser General Public License v2.1)

Inclus dans ESP8266 pour Arduino IDE:

* FS (GNU Lesser Public License> = 2.1)
* ESP8266WiFi (GNU Lesser Public License> = 2.1)
* ESP8266WebServer (GNU Lesser Public License> = 2.1)
* ESP8266httpUpdate (1.1.0) (GNU Lesser Public License> = 2.1)
* Serveur DNS (GNU Lesser Public License> = 2.1)

Installable via Arduino IDE (menu Sketch -> Inclure la bibliothèque -> Gérer les bibliothèques, la version testée et le type de licence entre parenthèses):

* [ArduinoJson](https://github.com/bblanchon/ArduinoJson) (5.13.1) (MIT)
* [Adafruit Unified Sensor](https://github.com/adafruit/Adafruit_Sensor) (1.0.2) (Apache)
* [Adafruit BMP085 library](https://github.com/adafruit/Adafruit-BMP085-Library) (1.0.0) (BSD)
* [Adafruit BMP280 library](https://github.com/adafruit/Adafruit_BMP280_Library) (1.0.2) (BSD)
* [Adafruit BME280 library](https://github.com/adafruit/Adafruit_BME280_Library) (1.0.7) (BSD)
* [DallasTemperature](https://github.com/milesburton/Arduino-Temperature-Control-Library) (3.8.0)
* [DHT sensor library](https://github.com/adafruit/DHT-sensor-library) (1.1.1) (MIT)
* [ESP8266 and ESP32 Oled driver for SSD1306 display](https://github.com/squix78/esp8266-oled-ssd1306) (4.0.0) (MIT)
* [OneWire](www.pjrc.com/teensy/td_libs_OneWire.html) (2.3.4)
* [LiquidCrystal I2C](https://github.com/marcoschwartz/LiquidCrystal_I2C) (1.1.2)
* [Adafruit HTU21DF Library](https://github.com/adafruit/Adafruit_HTU21DF_Library) (1.0.1)
* [SoftwareSerial](https://github.com/plerup/espsoftwareserial) (1.0.0) (GNU Lesser Public License >=2.1)

Installation manuelle:

* [TinyGPS++](http://arduiniana.org/libraries/tinygpsplus/) (0.95) (GNU Lesser Public License >=2.1)

Jusqu'à la version NRZ-2016-15:

* [DHT](https://github.com/adafruit/DHT-sensor-library)
  (`DHT.cpp` und `DHT.h` downloaden und in das Softwareverzeichnis kopieren)

J'espère avoir attrapé toutes les bibliothèques. Si une bibliothèque est manquante lors de la compilation, veuillez le signaler comme [Problème](https://github.com/opendata-stuttgart/sensors-software/issues/). J'ajoute ensuite les informations.

ATTENTION: à partir de la version 1.2, la bibliothèque de capteurs DHT a un problème sur l'ESP8266. Par conséquent, max. Utilisez la version 1.1.1

## Connexion des capteurs

Lors de la connexion de capteurs avec 5V, veuillez noter la version de la carte. NodeMCU v3 fournit 5 V à «VU», la version 2 n'a pas cette connexion et «VIN» peut être utilisé pour cela.

### SDS011

* Pin 1 (TX)   -> Pin D1 (GPIO5)
* Pin 2 (RX)   -> Pin D2 (GPIO4)
* Pin 3 (GND)  -> GND
* Pin 4 (2.5m) -> unused
* Pin 5 (5V)   -> VU
* Pin 6 (1m)   -> unused

### PPD42NS

* Pin 1 => GND
* Pin 2 => Pin D5 (GPIO14)
* Pin 3 => VU
* Pin 4 => Pin D6 (GPIO12)
* Pin 5 => unused

### DHT22

* Pin 1 => 3V3
* Pin 2 => Pin D7 (GPIO13)
* Pin 3 => unused
* Pin 4 => GND

### DS18B20 (OneWire interface)

Please check your version (pinout) at [datasheets DS18B20](https://datasheets.maximintegrated.com/en/ds/DS18B20.pdf)
Uses the same PIN D7 as DHT22, so DHT22 OR DS18B20 can be used.

* GND  -> Pin GND
* DQ   -> Pin D7 (GPIO 13)
* VCC  -> Pin 3V3 or Pin VU

### PMS1003 to PMS6003

Pinout:
   8 7 6 5 4 3 2 1

* Pin 1 (VCC)   -> VU
* Pin 2 (GND)   -> GND
* Pin 3 (SET)   -> unused
* Pin 4 (RX)    -> Pin D2 (GPIO4)
* Pin 5 (TX)    -> Pin D1 (GPIO5)
* Pin 6 (RESET) -> unused
* Pin 7 (NC)    -> unused
* Pin 8 (NC)    -> unused

### PMS7003

Pinout PMS7003:
   9  7  5  3  1
  10  8  6  4  2

* Pin  1/2 (VCC) -> VU
* Pin  3/4 (GND) -> GND
* Pin  5 (RESET) -> GND
* Pin  6 (NC)    -> unused
* Pin  7 (RX)    -> Pin D2 (GPIO4)
* Pin  8 (NC)    -> unused
* Pin  9 (TX)    -> Pin D1 (GPIO5)
* Pin 10 (SET)   -> unused

### Honeywell PM sensor

Pinout: 8 7 6 5 4 3 2 1

* Pin 1 (3.3V)   -> unused
* Pin 2 (5V)     -> VU
* Pin 3 (NC)     -> unused
* Pin 4 (NC)     -> unused
* Pin 5 TEST)    -> unused
* Pin 6 (TX)     -> Pin D1 (GPIO5)
* Pin 7 (RX)     -> Pin D2 (GPIO4)
* Pin 8 (GND)    -> GND

### BMP180 / BMP280 / BME280 (I2C)

* VCC  ->  Pin 3V3
* GND  ->  Pin GND
* SCL  ->  Pin D4 (GPIO2)
* SDA  ->  Pin D3 (GPIO0)

### HTU21D (I2C)

* VCC  ->  Pin 3V3
* GND  ->  Pin GND
* SCL  ->  Pin D4 (GPIO2)
* SDA  ->  Pin D3 (GPIO0)

### LCD1602 (I2C, 5V - check your version)

* VCC  ->  Pin VU
* GND  ->  Pin GND
* SCL  ->  Pin D4 (GPIO2)
* SDA  ->  Pin D3 (GPIO0)

### OLED displays with SSD1306 (I2C, 128x64 pixels)

* VCC -> Pin VU
* GND -> Pin GND
* SCL  ->  Pin D4 (GPIO2)
* SDA  ->  Pin D3 (GPIO0)

### GPS NEO 6M (série) ATTENTION: Fonctionne de manière très instable

Courant et masse de la carte. (GND et généralement 3.3v, vérifiez au préalable / instructions, description GPS!)
TX (envoyer) et RX (recevoir) sont câblés en croix !

* TX de Neo -> Pin D5 (RX)
* RX de Neo -> Pin D6 (TX)

### Luftdaten.info API "Pins"

Lors de l'activation de plusieurs capteurs, par ex. "Simultanément" DHT22 et PPD42NS, l'API nécessite l'affectation d'un capteur auquel une broche à laquelle le capteur est (virtuellement) connecté.
Ce firmware définit les broches des différents capteurs comme suit:

* PPD42NS => Pin 5
* DHT22 => Pin 7
* SDS011 => Pin 1
* BMP180 => Pin 3
* BMP280 => Pin 3
* BME280 => Pin 11
* GPS(Neo-6M) => Pin 9
