# -*- coding: utf-8 -*-

import pytest
import src.ppSplitter as ppSplitter

###############################################################################


text1 = """
24.02.2016 – 15:48

Polizeipräsidium Aalen

Aalen (ots)
 Korb: Vorfahrt missachtet 
Ein 20 Jahre alter VW-Fahrer wollte am Mittwochvormittag gegen 10.15 Uhr vom Ligusterweg in die Bühlstraße abbiegen und übersah dabei eine vorfahrtsberechtige 67-Jährige, die mit einem Smart unterwegs war. Durch den folgenden Zusammenstoß entstand Sachschaden von rund 5000 Euro. 
Remshalden: Sachbeschädigung an Kfz 
Ein Unbekannter beschmierte mit Sprühfarbe die rechte Fahrzeugseite, die Motorhaube sowie das hintere Kennzeichen eines Golfs, der zwischen Dienstag, 17 Uhr, und Mittwoch, 6.40 Uhr, im Oberen Wasen abgestellt war. Die Höhe des Sachschadens kann noch nicht beziffert werden. Hinweise auf den Verursacher nimmt der Polizeiposten Remshalden unter Telefon 07151/72463 entgegen. 
Waiblingen: Versuchter Einbruch in Gaststätte 
Ein Einbrecher versuchte im Zeitraum zwischen Dienstag, 0.30 Uhr, und Mittwoch, 8.30 Uhr, vergeblich in eine Gaststätte in der Karl-Ziegler-Straße einzubrechen. Nachdem der Dieb zunächst versucht hatte, ein Fenster aufzuhebeln, schlug er selbiges ein, konnte dieses aber letztlich nicht öffnen. Der Unbekannte verursachte Sachschaden von rund 300 Euro. Hinweise auf diesen nimmt der Polizeiposten Hohenacker unter Telefon 07151/82149 entgegen. 
Oppenweiler: Trunkenheit im Verkehr 
Bei einer routinemäßigen Verkehrskontrolle in der Hauptstraße musste am Mittwochmorgen gegen 7:45 Uhr bei einer 48-jährigen Daimler-Fahrerin Alkoholgeruch in der Atemluft festgestellt werden. Ein Vortest ergab einen Wert von über einem Promille. Die 48-Jährige musste eine Blutprobe sowie ihren Führerschein abgeben. 
Schondorf: Vorfahrt missachtet - Unfall im Kreisverkehr 
Am Mittwochmorgen kam es gegen acht Uhr an der Kreuzung Benzstraße und Vorstadtstraße zu einem Unfall. Eine 63-jährige Opel-Fahrerin  befuhr die Vorstadtstraße in Richtung Kreisverkehr Benzstraße/Schlachthausstraße. Beim Einfahren in den Kreisverkehr missachtete sie die Vorfahrt eines sich bereits im Kreisverkehr befindlichen 17-jährigen Zweiradfahrer. Der 17-Jährige konnte nicht mehr bremsen und rutschte in den Opel. Beim Unfall wurde niemand verletzt. Am Opel entstand ein Schaden in Höhe von 500 Euro. Am Zweirad entstand ein Schaden in Höhe von 400 Euro. 
Backnang: Feuerwehreinsatz - Plastikbehälter auf eingeschalteter Herdplatte 
Am Mittwochmorgen schlug ein Rauchmelder gegen 8.45 Uhr aus einer Wohnung im Marie-Juchacz-Weg alarm. Auch im Treppenhaus wurde ein verbrannter Geruch wahrgenommen, sodass die Feuerwehr sowei Polizei auf den Plan gerufen wurde. Als die Polizeistreife eintraf, befanden sich die Feuerwehr mit vier Fahrzeugen  und 15 Mann sowie das DRK bereits vor Ort. Die Wohnungstüre musste durch die Wehrmänner  gewaltsam geöffnet werden. Der 69-jährige Bewohner konnte wohlauf angetroffen werden.  Als Ursache für die Rauchentwicklung konnte ein auf der eingeschalteten Herdplatte befindlicher Plastikbehälter festgestellt werden. Zu einem offenen Brand kam es nicht. 
Schwaikheim: Verkehrsunfall 
Eine 46-jährige VW-Fahrerin bemerkte am Mittwochmorgen gegen 8 Uhr zu spät, dass sie an der Kreuzung Friedenstraße in die Silcherstraße abbiegen wollte. Als die 46-Jährige in der Friedenstraße zurücksetzte, um rückwärts in die Kreuzung einzufahren und anschließend abbiegen zu können, übersah sie einen mittlerweile hinter ihr stehenden 54-jährigen Smart-Fahrer. Durch den folgenden Zusammenstoß An diesem entstand am Smart ein Schaden in Höhe von 500 Euro. Der VW kam ohne Sachschaden davon. 
Weinstadt-Beutelsbach: Diebstahl von  Dachrinnen 
Im Verlauf der letzten Woche entwendete ein bisher unbekannter Dieb an zwei Weinberggartenhütten im Gewann Gundelsbacher Berg einmal zehn und einmal elf Meter Dachrinne. Es entstand ein Sachschaden von jeweils ca. 200 Euro. Hinweise auf den Dieb bzw. von ihm benutztes Fahrzeug nimmt der Polizeiposten Weinstadt unter der Telefonnummer 07151/ 65061 entgegen. 
 
Rückfragen bitte an:

Polizeipräsidium Aalen
Öffentlichkeitsarbeit
Telefon: 07361 580-106
E-Mail: aalen.pp.stab.oe@polizei.bwl.de
http://www.polizei-bw.de/
Original-Content von: Polizeipräsidium Aalen, übermittelt durch news aktuell
"""


split1 = [
    '2016 – 15:48 Polizeipräsidium Aalen Aalen (ots)  Korb: Vorfahrt missachtet Ein 20 Jahre alter VW-Fahrer wollte am Mittwochvormittag gegen 10.15 Uhr vom Ligusterweg in die Bühlstraße abbiegen und übersah dabei eine vorfahrtsberechtige 67-Jährige, die mit einem Smart unterwegs war. Durch den folgenden Zusammenstoß entstand Sachschaden von rund 5000 Euro.',
    'Remshalden: Sachbeschädigung an Kfz Ein Unbekannter beschmierte mit Sprühfarbe die rechte Fahrzeugseite, die Motorhaube sowie das hintere Kennzeichen eines Golfs, der zwischen Dienstag, 17 Uhr, und Mittwoch, 6.40 Uhr, im Oberen Wasen abgestellt war. Die Höhe des Sachschadens kann noch nicht beziffert werden. Hinweise auf den Verursacher nimmt der Polizeiposten Remshalden unter Telefon 07151/72463 entgegen.',
    'Waiblingen: Versuchter Einbruch in Gaststätte Ein Einbrecher versuchte im Zeitraum zwischen Dienstag, 0.30 Uhr, und Mittwoch, 8.30 Uhr, vergeblich in eine Gaststätte in der Karl-Ziegler-Straße einzubrechen. Nachdem der Dieb zunächst versucht hatte, ein Fenster aufzuhebeln, schlug er selbiges ein, konnte dieses aber letztlich nicht öffnen. Der Unbekannte verursachte Sachschaden von rund 300 Euro. Hinweise auf diesen nimmt der Polizeiposten Hohenacker unter Telefon 07151/82149 entgegen.',
    'Oppenweiler: Trunkenheit im Verkehr Bei einer routinemäßigen Verkehrskontrolle in der Hauptstraße musste am Mittwochmorgen gegen 7:45 Uhr bei einer 48-jährigen Daimler-Fahrerin Alkoholgeruch in der Atemluft festgestellt werden. Ein Vortest ergab einen Wert von über einem Promille. Die 48-Jährige musste eine Blutprobe sowie ihren Führerschein abgeben.',
    'Schondorf: Vorfahrt missachtet - Unfall im Kreisverkehr Am Mittwochmorgen kam es gegen acht Uhr an der Kreuzung Benzstraße und Vorstadtstraße zu einem Unfall. Eine 63-jährige Opel-Fahrerin befuhr die Vorstadtstraße in Richtung Kreisverkehr Benzstraße/Schlachthausstraße. Beim Einfahren in den Kreisverkehr missachtete sie die Vorfahrt eines sich bereits im Kreisverkehr befindlichen 17-jährigen Zweiradfahrer. Der 17-Jährige konnte nicht mehr bremsen und rutschte in den Opel. Beim Unfall wurde niemand verletzt. Am Opel entstand ein Schaden in Höhe von 500 Euro. Am Zweirad entstand ein Schaden in Höhe von 400 Euro.',
    'Backnang: Feuerwehreinsatz - Plastikbehälter auf eingeschalteter Herdplatte Am Mittwochmorgen schlug ein Rauchmelder gegen 8.45 Uhr aus einer Wohnung im Marie-Juchacz-Weg alarm. Auch im Treppenhaus wurde ein verbrannter Geruch wahrgenommen, sodass die Feuerwehr sowei Polizei auf den Plan gerufen wurde. Als die Polizeistreife eintraf, befanden sich die Feuerwehr mit vier Fahrzeugen und 15 Mann sowie das DRK bereits vor Ort. Die Wohnungstüre musste durch die Wehrmänner gewaltsam geöffnet werden. Der 69-jährige Bewohner konnte wohlauf angetroffen werden. Als Ursache für die Rauchentwicklung konnte ein auf der eingeschalteten Herdplatte befindlicher Plastikbehälter festgestellt werden. Zu einem offenen Brand kam es nicht.',
    'Schwaikheim: Verkehrsunfall Eine 46-jährige VW-Fahrerin bemerkte am Mittwochmorgen gegen 8 Uhr zu spät, dass sie an der Kreuzung Friedenstraße in die Silcherstraße abbiegen wollte. Als die 46-Jährige in der Friedenstraße zurücksetzte, um rückwärts in die Kreuzung einzufahren und anschließend abbiegen zu können, übersah sie einen mittlerweile hinter ihr stehenden 54-jährigen Smart-Fahrer. Durch den folgenden Zusammenstoß An diesem entstand am Smart ein Schaden in Höhe von 500 Euro. Der VW kam ohne Sachschaden davon.',
    'Weinstadt-Beutelsbach: Diebstahl von Dachrinnen Im Verlauf der letzten Woche entwendete ein bisher unbekannter Dieb an zwei Weinberggartenhütten im Gewann Gundelsbacher Berg einmal zehn und einmal elf Meter Dachrinne. Es entstand ein Sachschaden von jeweils ca. 200 Euro. Hinweise auf den Dieb bzw. von ihm benutztes Fahrzeug nimmt der Polizeiposten Weinstadt unter der Telefonnummer 07151/ 65061 entgegen.',
    ]


split1_2 = [
 '2016 – 15:48 Polizeipräsidium Aalen Aalen (ots) Korb: Vorfahrt missachtet Ein 20 Jahre alter VW-Fahrer wollte am Mittwochvormittag gegen 10.15 Uhr vom Ligusterweg in die Bühlstraße abbiegen und übersah dabei eine vorfahrtsberechtige 67-Jährige, die mit einem Smart unterwegs war. Durch den folgenden Zusammenstoß entstand Sachschaden von rund 5000 Euro.',
 'Remshalden: Sachbeschädigung an Kfz Ein Unbekannter beschmierte mit Sprühfarbe die rechte Fahrzeugseite, die Motorhaube sowie das hintere Kennzeichen eines Golfs, der zwischen Dienstag, 17 Uhr, und Mittwoch, 6.40 Uhr, im Oberen Wasen abgestellt war. Die Höhe des Sachschadens kann noch nicht beziffert werden. Hinweise auf den Verursacher nimmt der Polizeiposten Remshalden unter Telefon 07151/72463 entgegen.',
 'Waiblingen: Versuchter Einbruch in Gaststätte Ein Einbrecher versuchte im Zeitraum zwischen Dienstag, 0.30 Uhr, und Mittwoch, 8.30 Uhr, vergeblich in eine Gaststätte in der Karl-Ziegler-Straße einzubrechen. Nachdem der Dieb zunächst versucht hatte, ein Fenster aufzuhebeln, schlug er selbiges ein, konnte dieses aber letztlich nicht öffnen. Der Unbekannte verursachte Sachschaden von rund 300 Euro. Hinweise auf diesen nimmt der Polizeiposten Hohenacker unter Telefon 07151/82149 entgegen.',
 'Oppenweiler: Trunkenheit im Verkehr Bei einer routinemäßigen Verkehrskontrolle in der Hauptstraße musste am Mittwochmorgen gegen 7:45 Uhr bei einer 48-jährigen Daimler-Fahrerin Alkoholgeruch in der Atemluft festgestellt werden. Ein Vortest ergab einen Wert von über einem Promille. Die 48-Jährige musste eine Blutprobe sowie ihren Führerschein abgeben.',
 'Schondorf: Vorfahrt missachtet - Unfall im Kreisverkehr Am Mittwochmorgen kam es gegen acht Uhr an der Kreuzung Benzstraße und Vorstadtstraße zu einem Unfall. Eine 63-jährige Opel-Fahrerin befuhr die Vorstadtstraße in Richtung Kreisverkehr Benzstraße/Schlachthausstraße. Beim Einfahren in den Kreisverkehr missachtete sie die Vorfahrt eines sich bereits im Kreisverkehr befindlichen 17-jährigen Zweiradfahrer. Der 17-Jährige konnte nicht mehr bremsen und rutschte in den Opel. Beim Unfall wurde niemand verletzt. Am Opel entstand ein Schaden in Höhe von 500 Euro. Am Zweirad entstand ein Schaden in Höhe von 400 Euro.',
 'Backnang: Feuerwehreinsatz - Plastikbehälter auf eingeschalteter Herdplatte Am Mittwochmorgen schlug ein Rauchmelder gegen 8.45 Uhr aus einer Wohnung im Marie-Juchacz-Weg alarm. Auch im Treppenhaus wurde ein verbrannter Geruch wahrgenommen, sodass die Feuerwehr sowei Polizei auf den Plan gerufen wurde. Als die Polizeistreife eintraf, befanden sich die Feuerwehr mit vier Fahrzeugen und 15 Mann sowie das DRK bereits vor Ort. Die Wohnungstüre musste durch die Wehrmänner gewaltsam geöffnet werden. Der 69-jährige Bewohner konnte wohlauf angetroffen werden. Als Ursache für die Rauchentwicklung konnte ein auf der eingeschalteten Herdplatte befindlicher Plastikbehälter festgestellt werden. Zu einem offenen Brand kam es nicht.',
 'Schwaikheim: Verkehrsunfall Eine 46-jährige VW-Fahrerin bemerkte am Mittwochmorgen gegen 8 Uhr zu spät, dass sie an der Kreuzung Friedenstraße in die Silcherstraße abbiegen wollte. Als die 46-Jährige in der Friedenstraße zurücksetzte, um rückwärts in die Kreuzung einzufahren und anschließend abbiegen zu können, übersah sie einen mittlerweile hinter ihr stehenden 54-jährigen Smart-Fahrer. Durch den folgenden Zusammenstoß An diesem entstand am Smart ein Schaden in Höhe von 500 Euro. Der VW kam ohne Sachschaden davon.',
 'Weinstadt-Beutelsbach: Diebstahl von Dachrinnen Im Verlauf der letzten Woche entwendete ein bisher unbekannter Dieb an zwei Weinberggartenhütten im Gewann Gundelsbacher Berg einmal zehn und einmal elf Meter Dachrinne. Es entstand ein Sachschaden von jeweils ca. 200 Euro. Hinweise auf den Dieb bzw. von ihm benutztes Fahrzeug nimmt der Polizeiposten Weinstadt unter der Telefonnummer 07151/ 65061 entgegen.',
 ]

###############################################################################

text2 = """
18.05.2016 – 12:41

Polizeipräsidium Mannheim

Angelbachtal (ots)
 Zwischen Samstag, 16 Uhr und Dienstag, 14 Uhr kam es zu einem Einbruch in ein Einfamilienhaus in der Sportplatzstraße. Ein bislang unbekannter Täter hebelte eine Terrassentür auf um in das Anwesen zu gelangen. Im Inneren durchwühlte er in mehreren Räumen sämtliche Schränke und Schubladen. Informationen über mögliches Diebesgut liegen bislang keine vor, da sich die Bewohner im Urlaub befinden. 
Der Sachschaden lässt sich bislang nicht näher beziffern. 
Zeugen, die im genannten Tatzeitraum, verdächtige Beobachtungen gemacht haben, werden gebeten, sich mit dem Polizeirevier Sinsheim unter Tel.: 07261/690-0 in Verbindung zu setzen. 
 
Rückfragen bitte an:

Polizeipräsidium Mannheim
Stabsstelle Öffentlichkeitsarbeit
Nadine Maier
Telefon: 0621 174-1107
E-Mail: mannheim.pp.stab.oe@polizei.bwl.de
http://www.polizei-bw.de/
Original-Content von: Polizeipräsidium Mannheim, übermittelt durch news aktuell
"""

split2 = ['2016 – 12:41 Polizeipräsidium Mannheim Angelbachtal (ots) Zwischen Samstag, 16 Uhr und Dienstag, 14 Uhr kam es zu einem Einbruch in ein Einfamilienhaus in der Sportplatzstraße. Ein bislang unbekannter Täter hebelte eine Terrassentür auf um in das Anwesen zu gelangen. Im Inneren durchwühlte er in mehreren Räumen sämtliche Schränke und Schubladen. Informationen über mögliches Diebesgut liegen bislang keine vor, da sich die Bewohner im Urlaub befinden. Der Sachschaden lässt sich bislang nicht näher beziffern. Zeugen, die im genannten Tatzeitraum, verdächtige Beobachtungen gemacht haben, werden gebeten, sich mit dem Polizeirevier Sinsheim unter Tel.: 07261/690-0 in Verbindung zu setzen.']


###############################################################################


text3 = """
08.07.2016 – 17:37

Polizeipräsidium Mannheim

Mannheim (ots)
 Am Freitagnachmittag kam es im Stadtteil Rheinau zu einem Verkehrsunfall, bei dem fünf Personen verletzt wurden, darunter zwei Kleinkinder und ein Säugling. 
Kurz nach 15 Uhr war der Fahrer eines Ford Focus auf der Hockenheimer Straße in Richtung Relaisstraße unterwegs. An der Kreuzung Durlacher Straße missachtete er die Vorfahrt einer von rechts kommenden 29-jährigen Ford Ka-Fahrerin, worauf beide Fahrzeuge inmitten der Kreuzung kollidierten. Die 29-Jährige und zwei 3 und 5 Jahre alten Kleinkinder sowie ein 2-monatiger Säugling und deren Mutter, die im Ford Focus saßen wurden verletzt. Der Säugling wurde mit einem Rettungswagen zur Untersuchung in eine Klinik gebracht. 
An der Unfallstelle gab sich der 28-jährige Halter des Ford Focus als verantwortlicher Fahrer aus, was nach derzeitigem Stand der Ermittlungen fraglich erscheint. Laut Aussagen der 29-Jährigen soll ein anderer, bislang unbekannter Mann der Fahrer zum Unfallzeitpunkt gewesen sein, der sich im allgemeinen Trubel Schaulustiger entfernte. Er wird wie folgt beschrieben: ca. Mitte 40; ca. 180 cm; kurze, gaumelierte Haare, möglicherwiese Italiener. 
Hinweise nimmt das Polizeirevier Mannheim-Neckarau, Tel.: 0621/83397-0 entgegen. 
 
Rückfragen bitte an:

Polizeipräsidium Mannheim
Stabsstelle Öffentlichkeitsarbeit
Norbert Schätzle
Telefon: 0621 174-1102
E-Mail: mannheim.pp.stab.oe@polizei.bwl.de
http://www.polizei-bw.de/
Original-Content von: Polizeipräsidium Mannheim, übermittelt durch news aktuell
"""

split3 = ['2016 – 17:37 Polizeipräsidium Mannheim Mannheim (ots) Am Freitagnachmittag kam es im Stadtteil Rheinau zu einem Verkehrsunfall, bei dem fünf Personen verletzt wurden, darunter zwei Kleinkinder und ein Säugling. Kurz nach 15 Uhr war der Fahrer eines Ford Focus auf der Hockenheimer Straße in Richtung Relaisstraße unterwegs. An der Kreuzung Durlacher Straße missachtete er die Vorfahrt einer von rechts kommenden 29-jährigen Ford Ka-Fahrerin, worauf beide Fahrzeuge inmitten der Kreuzung kollidierten. Die 29-Jährige und zwei 3 und 5 Jahre alten Kleinkinder sowie ein 2-monatiger Säugling und deren Mutter, die im Ford Focus saßen wurden verletzt. Der Säugling wurde mit einem Rettungswagen zur Untersuchung in eine Klinik gebracht. An der Unfallstelle gab sich der 28-jährige Halter des Ford Focus als verantwortlicher Fahrer aus, was nach derzeitigem Stand der Ermittlungen fraglich erscheint. Laut Aussagen der 29-Jährigen soll ein anderer, bislang unbekannter Mann der Fahrer zum Unfallzeitpunkt gewesen sein, der sich im allgemeinen Trubel Schaulustiger entfernte. Er wird wie folgt beschrieben: ca. Mitte 40; ca. 180 cm; kurze, gaumelierte Haare, möglicherwiese Italiener. Hinweise nimmt das Polizeirevier Mannheim-Neckarau, Tel.: 0621/83397-0 entgegen.']


###############################################################################


text4 = """
25.04.2016 – 13:12

Polizeipräsidium Heilbronn

Heilbronn (ots)
 Lauda-Königshofen: Bereitgelegter Maibaum durchgesägt 
Anscheinend um eine Woche im Datum geirrt hatte sich ein Unbekannter am letzten Wochenende in Lauda-Königshofen - Ortsteil Gerlachsheim. Dieser sägte nämlich kurzerhand den auf dem Kirchplatz zum Aufstellen bereitgelegten Maibaum mit einer Akku-Kettensäge durch. Dieser alte "Brauch" wird eigentlich nur in der Nacht auf den 1.Mai - am aufgestellten Baum - praktiziert. Bis zum Wochenende muss nun ein neuer Baum organisiert werden, was dementsprechend auch mit Kosten verbunden ist. Hinweise zum bislang unbekannten Holzfäller nimmt das Polizeirevier Tauberbischofsheim unter der Telefonnummer 09351 81-0 entgegen. 
Wertheim: Hinweisschild beschädigt 
In der Nacht vom 23. auf den 24. April gegen 02.00 Uhr rissen Unbekannte das auf einem Briefkasten vor dem Gebäude 20 in der Lindenstraße angebrachte Hinweisschild  einer Zahnarztpraxis ab, wodurch dieses zerbrach. Zeugen werden gebeten sich über die Telefonnummer 09342 9189-40 beim Polizeirevier Wertheim zu melden. 
Wertheim: Parkenden Pkw beschädigt 
Ein bislang unbekannter Kfz-Lenker nahm es mit seinen Pflichten im Straßenverkehr anscheinend nicht so genau und fuhr ¬- nachdem er einen in der Carl-Roth-Straße im Bereich der alten Rotkreuzklinik am Straßenrand abgeparkten Toyota Yaris an der hinteren Stoßstange beschädigt hatte - einfach weiter. Der Unfall muss sich zwischen dem 23. April, 08.15 Uhr und dem 24. April, 10.00 Uhr ereignet haben. Sollte der Unfallverursacher nachträglich ermittelt werden, droht diesem eine Anzeige wegen Unerlaubten Entfernens von der Unfallstelle. Hinweise nimmt das Polizeirevier Wertheim unter der Telefonnummer 09342 9189-40 entgegen. 
 
Rückfragen bitte an:

Polizeipräsidium Heilbronn
Telefon: 07131 104-1012
E-Mail: heilbronn.pp@polizei.bwl.de
http://www.polizei-bw.de/
Original-Content von: Polizeipräsidium Heilbronn, übermittelt durch news aktuell
"""



split4 = [
    '2016 – 13:12 Polizeipräsidium Heilbronn  Heilbronn (ots)  Lauda-Königshofen: Bereitgelegter Maibaum durchgesägt Anscheinend um eine Woche im Datum geirrt hatte sich ein Unbekannter am letzten Wochenende in Lauda-Königshofen - Ortsteil Gerlachsheim. Dieser sägte nämlich kurzerhand den auf dem Kirchplatz zum Aufstellen bereitgelegten Maibaum mit einer Akku-Kettensäge durch. Dieser alte "Brauch" wird eigentlich nur in der Nacht auf den 1.Mai - am aufgestellten Baum - praktiziert. Bis zum Wochenende muss nun ein neuer Baum organisiert werden, was dementsprechend auch mit Kosten verbunden ist. Hinweise zum bislang unbekannten Holzfäller nimmt das Polizeirevier Tauberbischofsheim unter der Telefonnummer 09351 81-0 entgegen.',
    'Wertheim: Hinweisschild beschädigt In der Nacht vom 23. auf den 24. April gegen 02.00 Uhr rissen Unbekannte das auf einem Briefkasten vor dem Gebäude 20 in der Lindenstraße angebrachte Hinweisschild einer Zahnarztpraxis ab, wodurch dieses zerbrach. Zeugen werden gebeten sich über die Telefonnummer 09342 9189-40 beim Polizeirevier Wertheim zu melden.',
    'Wertheim: Parkenden Pkw beschädigt Ein bislang unbekannter Kfz-Lenker nahm es mit seinen Pflichten im Straßenverkehr anscheinend nicht so genau und fuhr ¬- nachdem er einen in der Carl-Roth-Straße im Bereich der alten Rotkreuzklinik am Straßenrand abgeparkten Toyota Yaris an der hinteren Stoßstange beschädigt hatte - einfach weiter. Der Unfall muss sich zwischen dem 23. April, 08.15 Uhr und dem 24. April, 10.00 Uhr ereignet haben. Sollte der Unfallverursacher nachträglich ermittelt werden, droht diesem eine Anzeige wegen Unerlaubten Entfernens von der Unfallstelle. Hinweise nimmt das Polizeirevier Wertheim unter der Telefonnummer 09342 9189-40 entgegen.',
    ]

split4_2 = [
    '2016 – 13:12 Polizeipräsidium Heilbronn Heilbronn (ots)  Lauda-Königshofen: Bereitgelegter Maibaum durchgesägt Anscheinend um eine Woche im Datum geirrt hatte sich ein Unbekannter am letzten Wochenende in Lauda-Königshofen - Ortsteil Gerlachsheim. Dieser sägte nämlich kurzerhand den auf dem Kirchplatz zum Aufstellen bereitgelegten Maibaum mit einer Akku-Kettensäge durch. Dieser alte "Brauch" wird eigentlich nur in der Nacht auf den 1.Mai - am aufgestellten Baum - praktiziert. Bis zum Wochenende muss nun ein neuer Baum organisiert werden, was dementsprechend auch mit Kosten verbunden ist. Hinweise zum bislang unbekannten Holzfäller nimmt das Polizeirevier Tauberbischofsheim unter der Telefonnummer 09351 81-0 entgegen.',
    'Wertheim: Hinweisschild beschädigt In der Nacht vom 23. auf den 24. April gegen 02.00 Uhr rissen Unbekannte das auf einem Briefkasten vor dem Gebäude 20 in der Lindenstraße angebrachte Hinweisschild einer Zahnarztpraxis ab, wodurch dieses zerbrach. Zeugen werden gebeten sich über die Telefonnummer 09342 9189-40 beim Polizeirevier Wertheim zu melden.',
    'Wertheim: Parkenden Pkw beschädigt Ein bislang unbekannter Kfz-Lenker nahm es mit seinen Pflichten im Straßenverkehr anscheinend nicht so genau und fuhr ¬- nachdem er einen in der Carl-Roth-Straße im Bereich der alten Rotkreuzklinik am Straßenrand abgeparkten Toyota Yaris an der hinteren Stoßstange beschädigt hatte - einfach weiter. Der Unfall muss sich zwischen dem 23. April, 08.15 Uhr und dem 24. April, 10.00 Uhr ereignet haben. Sollte der Unfallverursacher nachträglich ermittelt werden, droht diesem eine Anzeige wegen Unerlaubten Entfernens von der Unfallstelle. Hinweise nimmt das Polizeirevier Wertheim unter der Telefonnummer 09342 9189-40 entgegen.'
    ]


###############################################################################


text5 = """
12.03.2016 – 10:30

Polizeipräsidium Mannheim

Edingen-Neckarhausen (ots)
 Wegen des Verdachts des gefährlichen Eingriffs in den Straßenverkehr ermittelt die Polizei in Edingen-Neckarhausen gegen einen bislang unbekannten Täter. Vermutlich am frühen Freitagmorgen riss der Unbekannte ein Stationierungszeichen aus dem Boden, das auf der Friedrichsfelder Straße zwischen dem Rad- und Fußweg neben einem Feldgelände, zwischen der Einmündung Lilienstraße und Ortseingang Edingen verankert war und warf es auf die Fahrbahn. Kurz vor 5 Uhr überfuhr eine 49-jährige Nissan-Fahrerin das metallene Stationierungszeichen und riss sich dabei zunächst unbemerkt die Ölwanne auf. Die Autofahrerin kam noch bis zum Amselweg, wo ihr Fahrzeug liegenblieb. Der Sachschaden wird auf über 1000.- Euro geschätzt. Die über eine längere Strecke sich hingezogene Ölspur musste im Laufe des Freitagvormittages durch eine Spezialfirma beseitig werden. Zeugen, die Hinweise auf die Person oder Personen geben können, die das Stationierungszeichen auf die Fahrbahn war, werden gebeten, sich mit dem Polizeiposten Edingen-Neckarhausen, Tel.: 0621/892029 oder mit dem Polizeirevier Ladenburg, Tel.: 06203/9305-0 in Verbindung zu setzen. 
 
Rückfragen bitte an:

Polizeipräsidium Mannheim
Öffentlichkeitsarbeit
Norbert Schätzle
Telefon: 0621 174-1102
E-Mail: mannheim.pp@polizei.bwl.de
http://www.polizei-bw.de/
Original-Content von: Polizeipräsidium Mannheim, übermittelt durch news aktuell
"""


split5 = ['2016 – 10:30 Polizeipräsidium Mannheim Edingen-Neckarhausen (ots) Wegen des Verdachts des gefährlichen Eingriffs in den Straßenverkehr ermittelt die Polizei in Edingen-Neckarhausen gegen einen bislang unbekannten Täter. Vermutlich am frühen Freitagmorgen riss der Unbekannte ein Stationierungszeichen aus dem Boden, das auf der Friedrichsfelder Straße zwischen dem Rad- und Fußweg neben einem Feldgelände, zwischen der Einmündung Lilienstraße und Ortseingang Edingen verankert war und warf es auf die Fahrbahn. Kurz vor 5 Uhr überfuhr eine 49-jährige Nissan-Fahrerin das metallene Stationierungszeichen und riss sich dabei zunächst unbemerkt die Ölwanne auf. Die Autofahrerin kam noch bis zum Amselweg, wo ihr Fahrzeug liegenblieb. Der Sachschaden wird auf über 1000.- Euro geschätzt. Die über eine längere Strecke sich hingezogene Ölspur musste im Laufe des Freitagvormittages durch eine Spezialfirma beseitig werden. Zeugen, die Hinweise auf die Person oder Personen geben können, die das Stationierungszeichen auf die Fahrbahn war, werden gebeten, sich mit dem Polizeiposten Edingen-Neckarhausen, Tel.: 0621/892029 oder mit dem Polizeirevier Ladenburg, Tel.: 06203/9305-0 in Verbindung zu setzen.']


###############################################################################   

text6 = """
"25.05.2016 – 11:24

Polizeipräsidium Reutlingen

Reutlingen (ots)
 Radfahrer tödlich verunglückt (Zeugenaufruf) 
Ein 59-jähriger Reutlinger ist am frühen Mittwochmorgen, kurz nach 2 Uhr, mit seinem Trekkingrad tödlich verunglückt. Der Reutlinger war mit seinem Fahrrad im Bereich der Emil-Adolff-Straße auf dem Fußweg aus Richtung Benzstraße herkommend, über die Echazbrücke, in Richtung der dortigen Einkaufsmärkte unterwegs. Den polizeilichen Ermittlungen zufolge nutze er einen steilen unbefestigten Absatz zu den Parkplätzen als Abkürzung. Hierbei stürzte er so unglücklich, dass er noch am Unfallort an den Folgen seiner schweren Kopfverletzungen verstarb. Die Verkehrspolizei bittet Zeugen die den Unfall möglicherweise beobachtet haben, sich unter der Telefonnummer: 07071/972-8510 zu melden.  (cw) 
Neckartailfingen (ES): Betrunken und auf der falschen Fahrbahnseite unterwegs (Zeugenaufruf) 
Auf der falschen Fahrbahnseite war eine 40-jährige Stuttgarterin am frühen Mittwochmorgen auf der B 312 unterwegs und hat damit beinahe einen Verkehrsunfall verursacht. Die Stuttgarterin fuhr gegen 2.20 Uhr mit ihrem Ford Street Ka auf der Bundesstraße von Metzingen in Richtung Stuttgart. Hierbei nutzte sie allerdings die  linke, anstatt die rechte Fahrbahnseite. Auf Höhe von Neckartailfingen kam ihr ein mit drei Personen besetzter Audi A8, der in Richtung Metzingen unterwegs war, entgegen. Nur dadurch, dass der 19-jährige Audi-Fahrer schnell genug nach rechts ausweichen konnte und auch die Stuttgarterin wieder auf die rechte Spur zog, kam es nicht zum Frontalunfall. Die Stuttgarterin setzte ihre Fahrt in Richtung Stuttgart fort, konnte jedoch im Rahmen einer sofort eingeleiteten Fahndung auf der B 27 angetroffen werden. Bei der Überprüfung ihrer Fahrtauglichkeit stellten die Polizeibeamten einen vorläufigen Wert von mehr als 0,5 Promille fest. Ihr Führerschein wurde noch an Ort und Stelle beschlagnahmt und sie musste eine Blutentnahme über sich ergehen lassen. Verletzt wurde niemand, Sachschaden entstand keiner.  Die Polizei Filderstadt bittet Autofahrer die möglicherweise zuvor durch die lebensgefährliche Fahrweise der Stuttgarterin gefährdet wurden, sich zu melden. Polizeirevier Filderstadt, Telefon: 0711/70913. (cw) 
Frickenhausen (ES): VW Lupo in Flammen aufgegangen 
Ein brennender VW Lupo hat am Dienstagabend, gegen 19.15 Uhr, in der Unteren Straße für Aufregung gesorgt. Eine 35-jährige Kölnerin war mit ihrem Lupo auf der Hauptstraße in Richtung Nürtingen unterwegs. Als sie an der Ampel zur Abzweigung in Richtung Tischardt anhalten musste bemerkte sie, das Rauch aus dem Motorraum aufstieg. Geistesgegenwärtig stellte sie ihr Auto auf dem Parkplatz an der Unteren Straße ab und verständigte die Feuerwehr. Trotz dem schnellen Einsatz der Wehr, war nicht mehr zu verhindern, dass der Motorraum des Lupos völlig ausbrannte. An dem 15 Jahre alten Lupo entstand wirtschaftlicher Totalschaden. Der Wagen wurde abgeschleppt. (cw) 
Nürtingen (ES): Am Steuer eingeschlafen 
Eine völlig übermüdete Autofahrerin hat am frühen Mittwochmorgen in der Bahnhofstraße einen Verkehrsunfall verursacht. Die 49-jährige Nürtingerin war gegen 4.45 Uhr mit ihrem Seat Ibiza auf der Bahnhofstraße in Richtung Steinengrabenstraße unterwegs. Kurz nach der Einmündung Kirchstraße nickte sie am Steuer ein. Hierdurch geriet sie komplett auf den Mittelstreifen. Nachdem sie mehrere Sträucher und Büsche überfahren hatte, knallte ihr Seat gegen einen Baum, wo er zum Stillstand kam. Die Nürtingerin wurde bei dem Unfall leicht verletzt und vom Rettungsdienst zur weiteren Untersuchung ins Krankenhaus gebracht. Ihr Seat, an dem wirtschaftlicher Totalschaden in Höhe von mehreren tausend Euro entstanden ist, musste von einem Abschleppdienst geborgen werden. Gegen die Nürtinger wurde ein Ermittlungsverfahren wegen Straßenverkehrsgefährdung eingeleitet. (cw) 
Filderstadt-Bernhausen (ES): Auf parkendes Fahrzeug aufgefahren 
Auf etwa 21.000 Euro wird der Sachschaden geschätzt, den ein 33-jähriger Denkendorfer bei einem Verkehrsunfall am Dienstag, gegen 15.45 Uhr, in der Karlstraße verursacht hat. Der Denkendorfer war mit seinem Land Rover Freelander auf der Karlstraße unterwegs, als er auf Höhe des Einkaufsmarktes aus noch ungeklärter Ursache zu weit nach rechts kam. Völlig ungebremst krachte er ins Heck eines am rechten Fahrbahnrand geparkten Mercedes A-Klasse. Die Wucht des Aufpralls war so enorm, das der Mercedes trotz eingelegter Fahrstufe ""P"" noch fast 60 Meter nach vorne geschleudert wurde. Der Denkendorfer und seine 41-jährige Beifahrerin waren angegurtet und wurden bei dem Unfall zum Glück nur leicht verletzt. Eine medizinische Versorgung vor Ort war nicht notwendig. Die beiden völlig demolierten Fahrzeuge mussten abgeschleppt werden. (cw) 
Esslingen (ES): Unfall mit drei Fahrzeugen auf der B 10 
Ein Verkehrsunfall mit drei Fahrzeugen hat sich am Dienstagnachmittag auf der B 10 bei Esslingen ereignet. Ein 24-Jähriger wollte mit seinem Lexus kurz nach 15 Uhr an der Anschlussstelle Stadtmitte auf die Bundesstraße in Richtung Göppingen einfahren. Auf dem Beschleunigungsstreifen gab er zunächst viel Gas, um noch vor einem auf dem rechten Fahrstreifen fahrenden Lkw einscheren zu können. Als es ihm jedoch nicht reichte und die Einfädelspur zu Ende ging, bremste der junge Mann auf der nassen Fahrbahn so stark ab, dass sein Pkw ins Schleudern geriet. Der Lexus touchierte als erstes das Führerhaus des Lastwagens eines 42-Jährigen. Anschließend wurde der Lexus quer vor den Lkw gedreht, bis er schließlich auf die linke Fahrspur geriet und gegen den Mercedes eines 52-Jährigen prallte. Dieser wurde letztendlich noch gegen die Mittelleitplanke gedrückt. Das Auto des Unfallverursachers blieb entgegen der Fahrtrichtung auf dem linken Fahrstreifen stehen und musste ebenso wie der Mercedes abgeschleppt werden. Der Mercedeslenker erlitt leichte Verletzungen. Der Schaden wird auf 24.000 Euro geschätzt. Während der Unfallaufnahme kam es zu einem kilometerlangen Rückstau auf der B 10. (ms) 
Esslingen (ES): Lkw mit Bus kollidiert 
Zu einem Verkehrsunfall zwischen einem Lkw und einem Linienbus ist es am Mittwochmorgen in Esslingen gekommen. Ein 53-Jähriger befuhr mit seinem Lastwagen gegen 8.30 Uhr die Neckarstraße in Richtung Bahnhof. Auf Höhe der Pliensaustraße wechselte er auf die Busspur und kollidierte mit dem dort fahrenden Linienbus eines 39-Jährigen. Bei dem Unfall wurde ersten Erkenntnissen nach niemand verletzt. An dem Fahrzeug des Unfallverursachers entstand geringer Schaden. An dem Bus beläuft er sich jedoch auf etwa 10.000 Euro. (ms) 
Esslingen (ES): Tankwart bestohlen (Zeugenaufruf) 
Einem hilfsbereiten Tankwart sind am Dienstagabend mehrere Hundert Euro gestohlen worden. Ein bislang unbekannter Täter betrat kurz vor 19 Uhr die Tankstelle, legte dem Angestellten 50 Zehn-Euroscheine auf den Tresen und bat ihn, diese zu wechseln. Der 20-Jährige holte bereitwillig zwei 100-Euroscheine und sechs 50-Euroscheine aus der Kasse und überreichte das Geld. Der Unbekannte fragte ihn anschließend nach Tabak, worauf sich der junge Mann zum Regal umdrehte. Diesen Moment nutzte der Täter aus, schnappte sich ein Großteil des auf dem Tresen liegenden Geldes und ging aus der Tankstelle. Der Heranwachsende folgte ihm noch, doch der Trickdieb konnte unerkannt entkommen. 
Der Unbekannte ist etwa 30 bis 40 Jahre alt und zirka 175 cm groß. Er hat eine schmächtige Figur, eine Halbglatze sowie ein auffälliges Muttermal im Gesicht. Er sprach gebrochen Deutsch und trug eine hellblaue Regenjacke sowie eine dunkelblaue Jeans. Das Polizeirevier Esslingen bittet unter Telefon 0711/3990-0 um Hinweise nach dem Gesuchten. (ms) 
Filderstadt (ES): Gas- mit Bremspedal verwechselt 
Ein spektakulärer Verkehrsunfall hat sich am Dienstagabend in Bernhausen ereignet, bei dem ein älterer Autofahrer das Gas- mit dem Bremspedal verwechselt hat. Der 79-Jährige war kurz vor 18 Uhr mit seinem Mercedes in der Volmarstraße unterwegs. An einer Bushaltestelle wollte er anhalten, um seine Frau einsteigen zu lassen. Hierbei verwechselte er die Pedale und beschleunigte seinen Pkw, so dass er unkontrolliert davonraste. Das Auto fuhr über den Gehweg zwischen der stehenden Frau und einem verkehrsbedingt haltenden Pkw vorbei auf die Bernhäuser Hauptstraße ein. Anschließend kam der Mercedes von der Fahrbahn ab und prallte frontal gegen die Hauswand eines Imbiss. Der Fahrer erlitt schwere Verletzungen und musste in eine Klinik eingeliefert werden. Sein Fahrzeug war nicht mehr fahrbereit. Der Schaden beläuft sich auf zirka 15.000 Euro. (ms) 
Owen (ES): Zeugen zu Unfall gesucht 
Das Polizeirevier Kirchheim sucht unter Telefon 07021/501-0 nach Zeugen zu einem gefährlichen Überholmanöver, bei dem zwei Fahrzeuge am Dienstagnachmittag bei Owen beschädigt worden sind. Ein 25-jähriger VW Ventolenker befuhr gegen 16 Uhr die L 1210 von Owen kommend in Richtung Beuren. Kurz vor einer langgezogenen Linkskurve überholte er verbotswidrig einen Lastwagen. Als er den Lkw etwa zur Hälfte überholt hatte, kam ihm ein 58-Jähriger mit seinem Mazda entgegen. Um eine Frontalkollision zu vermeiden, wichen der Mazdalenker sowie der Lkw Fahrer jeweils nach rechts aus, so dass alle drei Fahrzeuge nebeneinander Platz hatten. Beim Wiedereinscheren streifte jedoch der Vento das linke vordere Eck des Führerhauses. Hierbei entstand ein Schaden in Höhe von etwa 5000 Euro. (ms) 
Mössingen (TÜ): Zwei Fahrzeuge nicht mehr fahrbereit 
Zwei Autos mussten am Dienstagnachmittag nach einem Verkehrsunfall abgeschleppt werden, nachdem ein Autofahrer beim Ausfahren aus einer Tankstelle den vorfahrtsberechtigten Pkw einer Frau übersehen hatte. Der 55-Jährige bog kurz vor 15 Uhr mit seinem BMW von dem Tankstellengelände nach links auf die Bahnhofstraße in Richtung Ortsmitte ab. Hierbei musste er sich durch eine verkehrsbedingt wartende Fahrzeugkolonne auf der Geradeausspur hindurchtasten. Zu spät erkannte er, dass eine 41-jährige Citroenlenkerin den Linksabbiegestreifen zur Freiherr-vom-Stein-Straße befuhr. Bei der Kollision erlitten beide Beteiligte leichte Verletzungen. Der Unfallverursacher wollte sich selbstständig in ärztliche Behandlung begeben. Die schwangere Frau wurde vorsorglich durch den Rettungsdienst in eine Klinik zur Untersuchung gefahren. Der Schaden beträgt zirka 12.000 Euro. (ms) 
 
Rückfragen bitte an:

Michael Schaal (ms), Telefon 07121/942-1104

Christian Wörner (cw), Telefon 07121/942-1105

Polizeipräsidium Reutlingen
Telefon: 07121 942-0
E-Mail: reutlingen.pp.pressestelle@polizei.bwl.de
http://www.polizei-bw.de/
Original-Content von: Polizeipräsidium Reutlingen, übermittelt durch news aktuell"

"""

split6 = [
 '2016 – 11:24 Polizeipräsidium Reutlingen Reutlingen (ots) Radfahrer tödlich verunglückt (Zeugenaufruf) Ein 59-jähriger Reutlinger ist am frühen Mittwochmorgen, kurz nach 2 Uhr, mit seinem Trekkingrad tödlich verunglückt. Der Reutlinger war mit seinem Fahrrad im Bereich der Emil-Adolff-Straße auf dem Fußweg aus Richtung Benzstraße herkommend, über die Echazbrücke, in Richtung der dortigen Einkaufsmärkte unterwegs. Den polizeilichen Ermittlungen zufolge nutze er einen steilen unbefestigten Absatz zu den Parkplätzen als Abkürzung. Hierbei stürzte er so unglücklich, dass er noch am Unfallort an den Folgen seiner schweren Kopfverletzungen verstarb. Die Verkehrspolizei bittet Zeugen die den Unfall möglicherweise beobachtet haben, sich unter der Telefonnummer: 07071/972-8510 zu melden.',
 '(cw) Neckartailfingen (ES): Betrunken und auf der falschen Fahrbahnseite unterwegs (Zeugenaufruf) Auf der falschen Fahrbahnseite war eine 40-jährige Stuttgarterin am frühen Mittwochmorgen auf der B 312 unterwegs und hat damit beinahe einen Verkehrsunfall verursacht. Die Stuttgarterin fuhr gegen 2.20 Uhr mit ihrem Ford Street Ka auf der Bundesstraße von Metzingen in Richtung Stuttgart. Hierbei nutzte sie allerdings die linke, anstatt die rechte Fahrbahnseite. Auf Höhe von Neckartailfingen kam ihr ein mit drei Personen besetzter Audi A8, der in Richtung Metzingen unterwegs war, entgegen. Nur dadurch, dass der 19-jährige Audi-Fahrer schnell genug nach rechts ausweichen konnte und auch die Stuttgarterin wieder auf die rechte Spur zog, kam es nicht zum Frontalunfall. Die Stuttgarterin setzte ihre Fahrt in Richtung Stuttgart fort, konnte jedoch im Rahmen einer sofort eingeleiteten Fahndung auf der B 27 angetroffen werden. Bei der Überprüfung ihrer Fahrtauglichkeit stellten die Polizeibeamten einen vorläufigen Wert von mehr als 0,5 Promille fest. Ihr Führerschein wurde noch an Ort und Stelle beschlagnahmt und sie musste eine Blutentnahme über sich ergehen lassen. Verletzt wurde niemand, Sachschaden entstand keiner. Die Polizei Filderstadt bittet Autofahrer die möglicherweise zuvor durch die lebensgefährliche Fahrweise der Stuttgarterin gefährdet wurden, sich zu melden.',
 '(cw) Frickenhausen (ES): VW Lupo in Flammen aufgegangen Ein brennender VW Lupo hat am Dienstagabend, gegen 19.15 Uhr, in der Unteren Straße für Aufregung gesorgt. Eine 35-jährige Kölnerin war mit ihrem Lupo auf der Hauptstraße in Richtung Nürtingen unterwegs. Als sie an der Ampel zur Abzweigung in Richtung Tischardt anhalten musste bemerkte sie, das Rauch aus dem Motorraum aufstieg. Geistesgegenwärtig stellte sie ihr Auto auf dem Parkplatz an der Unteren Straße ab und verständigte die Feuerwehr. Trotz dem schnellen Einsatz der Wehr, war nicht mehr zu verhindern, dass der Motorraum des Lupos völlig ausbrannte. An dem 15 Jahre alten Lupo entstand wirtschaftlicher Totalschaden. Der Wagen wurde abgeschleppt.',
 '(cw) Nürtingen (ES): Am Steuer eingeschlafen Eine völlig übermüdete Autofahrerin hat am frühen Mittwochmorgen in der Bahnhofstraße einen Verkehrsunfall verursacht. Die 49-jährige Nürtingerin war gegen 4.45 Uhr mit ihrem Seat Ibiza auf der Bahnhofstraße in Richtung Steinengrabenstraße unterwegs. Kurz nach der Einmündung Kirchstraße nickte sie am Steuer ein. Hierdurch geriet sie komplett auf den Mittelstreifen. Nachdem sie mehrere Sträucher und Büsche überfahren hatte, knallte ihr Seat gegen einen Baum, wo er zum Stillstand kam. Die Nürtingerin wurde bei dem Unfall leicht verletzt und vom Rettungsdienst zur weiteren Untersuchung ins Krankenhaus gebracht. Ihr Seat, an dem wirtschaftlicher Totalschaden in Höhe von mehreren tausend Euro entstanden ist, musste von einem Abschleppdienst geborgen werden. Gegen die Nürtinger wurde ein Ermittlungsverfahren wegen Straßenverkehrsgefährdung eingeleitet.',
 '(cw) Filderstadt-Bernhausen (ES): Auf parkendes Fahrzeug aufgefahren Auf etwa 21.000 Euro wird der Sachschaden geschätzt, den ein 33-jähriger Denkendorfer bei einem Verkehrsunfall am Dienstag, gegen 15.45 Uhr, in der Karlstraße verursacht hat. Der Denkendorfer war mit seinem Land Rover Freelander auf der Karlstraße unterwegs, als er auf Höhe des Einkaufsmarktes aus noch ungeklärter Ursache zu weit nach rechts kam. Völlig ungebremst krachte er ins Heck eines am rechten Fahrbahnrand geparkten Mercedes A-Klasse. Die Wucht des Aufpralls war so enorm, das der Mercedes trotz eingelegter Fahrstufe ""P"" noch fast 60 Meter nach vorne geschleudert wurde. Der Denkendorfer und seine 41-jährige Beifahrerin waren angegurtet und wurden bei dem Unfall zum Glück nur leicht verletzt. Eine medizinische Versorgung vor Ort war nicht notwendig. Die beiden völlig demolierten Fahrzeuge mussten abgeschleppt werden.',
 '(cw) Esslingen (ES): Unfall mit drei Fahrzeugen auf der B 10 Ein Verkehrsunfall mit drei Fahrzeugen hat sich am Dienstagnachmittag auf der B 10 bei Esslingen ereignet. Ein 24-Jähriger wollte mit seinem Lexus kurz nach 15 Uhr an der Anschlussstelle Stadtmitte auf die Bundesstraße in Richtung Göppingen einfahren. Auf dem Beschleunigungsstreifen gab er zunächst viel Gas, um noch vor einem auf dem rechten Fahrstreifen fahrenden Lkw einscheren zu können. Als es ihm jedoch nicht reichte und die Einfädelspur zu Ende ging, bremste der junge Mann auf der nassen Fahrbahn so stark ab, dass sein Pkw ins Schleudern geriet. Der Lexus touchierte als erstes das Führerhaus des Lastwagens eines 42-Jährigen. Anschließend wurde der Lexus quer vor den Lkw gedreht, bis er schließlich auf die linke Fahrspur geriet und gegen den Mercedes eines 52-Jährigen prallte. Dieser wurde letztendlich noch gegen die Mittelleitplanke gedrückt. Das Auto des Unfallverursachers blieb entgegen der Fahrtrichtung auf dem linken Fahrstreifen stehen und musste ebenso wie der Mercedes abgeschleppt werden. Der Mercedeslenker erlitt leichte Verletzungen. Der Schaden wird auf 24.000 Euro geschätzt. Während der Unfallaufnahme kam es zu einem kilometerlangen Rückstau auf der B 10.',
 '(ms) Esslingen (ES): Lkw mit Bus kollidiert Zu einem Verkehrsunfall zwischen einem Lkw und einem Linienbus ist es am Mittwochmorgen in Esslingen gekommen. Ein 53-Jähriger befuhr mit seinem Lastwagen gegen 8.30 Uhr die Neckarstraße in Richtung Bahnhof. Auf Höhe der Pliensaustraße wechselte er auf die Busspur und kollidierte mit dem dort fahrenden Linienbus eines 39-Jährigen. Bei dem Unfall wurde ersten Erkenntnissen nach niemand verletzt. An dem Fahrzeug des Unfallverursachers entstand geringer Schaden. An dem Bus beläuft er sich jedoch auf etwa 10.000 Euro.',
 '(ms) Esslingen (ES): Tankwart bestohlen (Zeugenaufruf) Einem hilfsbereiten Tankwart sind am Dienstagabend mehrere Hundert Euro gestohlen worden. Ein bislang unbekannter Täter betrat kurz vor 19 Uhr die Tankstelle, legte dem Angestellten 50 Zehn-Euroscheine auf den Tresen und bat ihn, diese zu wechseln. Der 20-Jährige holte bereitwillig zwei 100-Euroscheine und sechs 50-Euroscheine aus der Kasse und überreichte das Geld. Der Unbekannte fragte ihn anschließend nach Tabak, worauf sich der junge Mann zum Regal umdrehte. Diesen Moment nutzte der Täter aus, schnappte sich ein Großteil des auf dem Tresen liegenden Geldes und ging aus der Tankstelle. Der Heranwachsende folgte ihm noch, doch der Trickdieb konnte unerkannt entkommen. Der Unbekannte ist etwa 30 bis 40 Jahre alt und zirka 175 cm groß. Er hat eine schmächtige Figur, eine Halbglatze sowie ein auffälliges Muttermal im Gesicht. Er sprach gebrochen Deutsch und trug eine hellblaue Regenjacke sowie eine dunkelblaue Jeans. Das Polizeirevier Esslingen bittet unter Telefon 0711/3990-0 um Hinweise nach dem Gesuchten.',
 '(ms) Filderstadt (ES): Gas- mit Bremspedal verwechselt Ein spektakulärer Verkehrsunfall hat sich am Dienstagabend in Bernhausen ereignet, bei dem ein älterer Autofahrer das Gas- mit dem Bremspedal verwechselt hat. Der 79-Jährige war kurz vor 18 Uhr mit seinem Mercedes in der Volmarstraße unterwegs. An einer Bushaltestelle wollte er anhalten, um seine Frau einsteigen zu lassen. Hierbei verwechselte er die Pedale und beschleunigte seinen Pkw, so dass er unkontrolliert davonraste. Das Auto fuhr über den Gehweg zwischen der stehenden Frau und einem verkehrsbedingt haltenden Pkw vorbei auf die Bernhäuser Hauptstraße ein. Anschließend kam der Mercedes von der Fahrbahn ab und prallte frontal gegen die Hauswand eines Imbiss. Der Fahrer erlitt schwere Verletzungen und musste in eine Klinik eingeliefert werden. Sein Fahrzeug war nicht mehr fahrbereit. Der Schaden beläuft sich auf zirka 15.000 Euro.',
 '(ms) Owen (ES): Zeugen zu Unfall gesucht Das Polizeirevier Kirchheim sucht unter Telefon 07021/501-0 nach Zeugen zu einem gefährlichen Überholmanöver, bei dem zwei Fahrzeuge am Dienstagnachmittag bei Owen beschädigt worden sind. Ein 25-jähriger VW Ventolenker befuhr gegen 16 Uhr die L 1210 von Owen kommend in Richtung Beuren. Kurz vor einer langgezogenen Linkskurve überholte er verbotswidrig einen Lastwagen. Als er den Lkw etwa zur Hälfte überholt hatte, kam ihm ein 58-Jähriger mit seinem Mazda entgegen. Um eine Frontalkollision zu vermeiden, wichen der Mazdalenker sowie der Lkw Fahrer jeweils nach rechts aus, so dass alle drei Fahrzeuge nebeneinander Platz hatten. Beim Wiedereinscheren streifte jedoch der Vento das linke vordere Eck des Führerhauses. Hierbei entstand ein Schaden in Höhe von etwa 5000 Euro.',
 '(ms) Mössingen (TÜ): Zwei Fahrzeuge nicht mehr fahrbereit Zwei Autos mussten am Dienstagnachmittag nach einem Verkehrsunfall abgeschleppt werden, nachdem ein Autofahrer beim Ausfahren aus einer Tankstelle den vorfahrtsberechtigten Pkw einer Frau übersehen hatte. Der 55-Jährige bog kurz vor 15 Uhr mit seinem BMW von dem Tankstellengelände nach links auf die Bahnhofstraße in Richtung Ortsmitte ab. Hierbei musste er sich durch eine verkehrsbedingt wartende Fahrzeugkolonne auf der Geradeausspur hindurchtasten. Zu spät erkannte er, dass eine 41-jährige Citroenlenkerin den Linksabbiegestreifen zur Freiherr-vom-Stein-Straße befuhr. Bei der Kollision erlitten beide Beteiligte leichte Verletzungen. Der Unfallverursacher wollte sich selbstständig in ärztliche Behandlung begeben. Die schwangere Frau wurde vorsorglich durch den Rettungsdienst in eine Klinik zur Untersuchung gefahren. Der Schaden beträgt zirka 12.000 Euro. (ms)',
 ]

###############################################################################

text7 = """
25.11.2016 – 09:19

Polizeipräsidium Reutlingen

Reutlingen (ots)
 Gemeinsame Pressemitteilung der Staatsanwaltschaft Tübingen und des Polizeipräsidiums Reutlingen 
Tübingen 
Eine aus dem ehemaligen Jugoslawien stammende Tätergruppierung im Alter zwischen 19 und 50 Jahren steht in dringendem Verdacht, seit Juni 2015 rund 300 Diebstähle von hochwertigen Fahrrädern und etwa 100 Einbrüche in landwirtschaftliche Lagerhallen und Wertstoffhöfe begangen zu haben. Bei ihren Beutezügen soll die Gruppierung Diebesgut im Gesamtwert von rund 250.000 Euro erlangt haben. Auf das Konto der Gruppierung soll auch der Brand einer Lagerhalle in Tübingen-Hagelloch im Oktober 2016 gehen, bei dem ein Schaden von über einer Million Euro entstanden war. Gegen sieben Tatverdächtige wurden mittlerweile Haftbefehle erlassen. 
Nach einem signifikanten Anstieg der Fahrraddiebstähle im Bereich von Tübingen ab Mitte des 2. Halbjahres 2016, richteten sich die Ermittlungen  zunächst gegen die Benutzer eines dunklen Transporters, der im Zusammenhang mit dem Diebstahl von hochwertigen Fahrrädern aufgefallen war. In der Folge konnten weitere Personen ermittelt werden, die im Verdacht standen, an den Diebstählen beteiligt gewesen zu sein. Schnell erhärtete sich dieser Verdacht, als Beamte der Bundespolizei am 07.09.2016 auf der A8 im Bereich von Traunstein/Bayern zwei bosnische Staatsangehörige in einem Kleintransporter Fiat Ducato, mit österreichischer Zulassung, kurz vor dem Grenzübertritt kontrollierten. Im Transporter befanden sich zahlreiche im Landkreis Tübingen gestohlene Fahrräder. Beim Polizeipräsidium Reutlingen wurde daraufhin die gemeinsame, neunköpfige Ermittlungsgruppe "Ducato" aus Beamten des Kriminalkommissariats und des Polizeireviers Tübingen eingerichtet. 
Durch verdeckte Maßnahmen konnten in der Folge nach und nach die Täterstrukturen und die einzelnen Taten nachvollzogen werden. So wurde auch bekannt, dass die Tätergruppierung ab Oktober 2016 ihr Tätigkeitsfeld auf Einbrüche in Werk- und Lagerhallen sowie Wertstoffzentren ausdehnte. Ziel waren Baumaschinen, Garten- und Elektrogeräte, sowie Metallschrott und Kraftstoffe. 
Erlangte Wertstoffe wurden über eigene Firmen in den legalen Umlauf gebracht. Erbeutete Maschinen wie Notstromaggregate, Motorsägen o. ä. wurden in unterschiedlichen Depots zwischengelagert, um sie dann von als Touristen getarnten Transporteuren nach Tuzla/Bosnien bringen zu lassen. Dort betrieb die Familie des mutmaßlichen Anführers der Gruppierung eine Firma für Gebrauchtmaschinen. Im Rahmen einer Durchsuchungsmaßnahme in den dortigen Firmenräumen beschlagnahmte die bosnische Polizei Waren im Wert von 200.000 Euro. 
Zwei der drei mutmaßlichen Anführer der Gruppierung hielten sich als Touristen im Bereich Tübingen auf. Der Dritte betrieb im hiesigen Bereich einen Wertstoffhandel. Die eigentlichen Diebstahlstaten selbst, die sich zunächst auf  den Landkreis Tübingen beschränkten und anschließend auch auf benachbarte  Kreise ausgedehnt wurden, sollen von zur Gruppierung gehörenden Asylberwerbern aus Bosnien und Serbien begangen worden sein. 
Im Rahmen der Ermittlungen dürfte auch der Brand einer landwirtschaftlichen Lagerhalle mit einem Millionenschaden am 23.10.2016 in Tübingen-Hagelloch aufgeklärt worden sein. Das Feuer soll nach einem Einbruch zur Verdeckung von Spuren vorsätzlich von einem 20-Jährigen gelegt worden sein. 
Am Abend des 20.11.2016 nahmen Polizeibeamte bei einer allgemeinen Fahrzeugkontrolle in Tübingen-Weilheim zwei zur Gruppierung gehörende Tatverdächtige fest, weil sie in ihrem Fahrzeug Diebesgut mitführten, das sie zuvor in einem Schuppengebiet in Dußlingen und Gomaringen erbeutet hatten. 
Als bekannt wurde, dass eine Transportfahrt nach Tuzla akut bevorstehen soll, wurden über die Staatsanwaltschaft Tübingen beim zuständigen Amtsgericht Tübingen Durchsuchungs- und Beschlagnahmebeschlüsse für zwei Schrotthandlungen im Kreis Tübingen sowie acht Wohnungen in Tübingen, Gomaringen, Mössingen, Dettingen/Erms und Eberbach beantragt. 
Mehr als 80 Beamte durchsuchten am Dienstagmorgen alle zehn Objekte. Dabei konnten sämtliche Beschuldigte angetroffen und festgenommen werden. Insgesamt sieben Transportfahrzeuge sowie Bargeld und Wertstoffe im Gesamtwert von etwa 200.000 Euro wurden sichergestellt. 
Am Dienstag und Mittwoch wurden sieben Beschuldigte dem Haftrichter beim Amtsgericht Tübingen vorgeführt, der die von der Staatsanwaltschaft beantragten Haftbefehle in Vollzug setzte und die Untersuchungshaft anordnete. Die Festgenommenen wurden in verschiedene Haftanstalten eingeliefert. 
Zum Teil legten die Beschuldigten Geständnisse ab, die jetzt noch ausgewertet werden müssen. 
 
Rückfragen bitte an:

Josef Hönes (jh), Tel. 07121/942-1102

Polizeipräsidium Reutlingen
Telefon: 07121 942-0
E-Mail: reutlingen.pp.pressestelle@polizei.bwl.de
http://www.polizei-bw.de/
Original-Content von: Polizeipräsidium Reutlingen, übermittelt durch news aktuell
"""

# Split ist genaugenommen eigentlich "falsch", da das erste Snippet die Überschrift ist.
# Dennoch ist dieser Fehler absolut zu tolerieren und nicht wirklich zu beheben.
split7 = [
    '2016 – 09:19 Polizeipräsidium Reutlingen Reutlingen (ots) Gemeinsame Pressemitteilung der Staatsanwaltschaft Tübingen und des Polizeipräsidiums Reutlingen',
    'Tübingen Eine aus dem ehemaligen Jugoslawien stammende Tätergruppierung im Alter zwischen 19 und 50 Jahren steht in dringendem Verdacht, seit Juni 2015 rund 300 Diebstähle von hochwertigen Fahrrädern und etwa 100 Einbrüche in landwirtschaftliche Lagerhallen und Wertstoffhöfe begangen zu haben. Bei ihren Beutezügen soll die Gruppierung Diebesgut im Gesamtwert von rund 250.000 Euro erlangt haben. Auf das Konto der Gruppierung soll auch der Brand einer Lagerhalle in Tübingen-Hagelloch im Oktober 2016 gehen, bei dem ein Schaden von über einer Million Euro entstanden war. Gegen sieben Tatverdächtige wurden mittlerweile Haftbefehle erlassen. Nach einem signifikanten Anstieg der Fahrraddiebstähle im Bereich von Tübingen ab Mitte des 2. Halbjahres 2016, richteten sich die Ermittlungen zunächst gegen die Benutzer eines dunklen Transporters, der im Zusammenhang mit dem Diebstahl von hochwertigen Fahrrädern aufgefallen war. In der Folge konnten weitere Personen ermittelt werden, die im Verdacht standen, an den Diebstählen beteiligt gewesen zu sein. Schnell erhärtete sich dieser Verdacht, als Beamte der Bundespolizei am 07.09.2016 auf der A8 im Bereich von Traunstein/Bayern zwei bosnische Staatsangehörige in einem Kleintransporter Fiat Ducato, mit österreichischer Zulassung, kurz vor dem Grenzübertritt kontrollierten. Im Transporter befanden sich zahlreiche im Landkreis Tübingen gestohlene Fahrräder. Beim Polizeipräsidium Reutlingen wurde daraufhin die gemeinsame, neunköpfige Ermittlungsgruppe "Ducato" aus Beamten des Kriminalkommissariats und des Polizeireviers Tübingen eingerichtet. Durch verdeckte Maßnahmen konnten in der Folge nach und nach die Täterstrukturen und die einzelnen Taten nachvollzogen werden. So wurde auch bekannt, dass die Tätergruppierung ab Oktober 2016 ihr Tätigkeitsfeld auf Einbrüche in Werk- und Lagerhallen sowie Wertstoffzentren ausdehnte. Ziel waren Baumaschinen, Garten- und Elektrogeräte, sowie Metallschrott und Kraftstoffe. Erlangte Wertstoffe wurden über eigene Firmen in den legalen Umlauf gebracht. Erbeutete Maschinen wie Notstromaggregate, Motorsägen o. ä. wurden in unterschiedlichen Depots zwischengelagert, um sie dann von als Touristen getarnten Transporteuren nach Tuzla/Bosnien bringen zu lassen. Dort betrieb die Familie des mutmaßlichen Anführers der Gruppierung eine Firma für Gebrauchtmaschinen. Im Rahmen einer Durchsuchungsmaßnahme in den dortigen Firmenräumen beschlagnahmte die bosnische Polizei Waren im Wert von 200.000 Euro. Zwei der drei mutmaßlichen Anführer der Gruppierung hielten sich als Touristen im Bereich Tübingen auf. Der Dritte betrieb im hiesigen Bereich einen Wertstoffhandel. Die eigentlichen Diebstahlstaten selbst, die sich zunächst auf den Landkreis Tübingen beschränkten und anschließend auch auf benachbarte Kreise ausgedehnt wurden, sollen von zur Gruppierung gehörenden Asylberwerbern aus Bosnien und Serbien begangen worden sein. Im Rahmen der Ermittlungen dürfte auch der Brand einer landwirtschaftlichen Lagerhalle mit einem Millionenschaden am 23.10.2016 in Tübingen-Hagelloch aufgeklärt worden sein. Das Feuer soll nach einem Einbruch zur Verdeckung von Spuren vorsätzlich von einem 20-Jährigen gelegt worden sein. Am Abend des 20.11.2016 nahmen Polizeibeamte bei einer allgemeinen Fahrzeugkontrolle in Tübingen-Weilheim zwei zur Gruppierung gehörende Tatverdächtige fest, weil sie in ihrem Fahrzeug Diebesgut mitführten, das sie zuvor in einem Schuppengebiet in Dußlingen und Gomaringen erbeutet hatten. Als bekannt wurde, dass eine Transportfahrt nach Tuzla akut bevorstehen soll, wurden über die Staatsanwaltschaft Tübingen beim zuständigen Amtsgericht Tübingen Durchsuchungs- und Beschlagnahmebeschlüsse für zwei Schrotthandlungen im Kreis Tübingen sowie acht Wohnungen in Tübingen, Gomaringen, Mössingen, Dettingen/Erms und Eberbach beantragt. Mehr als 80 Beamte durchsuchten am Dienstagmorgen alle zehn Objekte. Dabei konnten sämtliche Beschuldigte angetroffen und festgenommen werden. Insgesamt sieben Transportfahrzeuge sowie Bargeld und Wertstoffe im Gesamtwert von etwa 200.000 Euro wurden sichergestellt. Am Dienstag und Mittwoch wurden sieben Beschuldigte dem Haftrichter beim Amtsgericht Tübingen vorgeführt, der die von der Staatsanwaltschaft beantragten Haftbefehle in Vollzug setzte und die Untersuchungshaft anordnete. Die Festgenommenen wurden in verschiedene Haftanstalten eingeliefert. Zum Teil legten die Beschuldigten Geständnisse ab, die jetzt noch ausgewertet werden müssen.',
    ]


###############################################################################


text8 = """
16.06.2016 – 09:14

Polizeipräsidium Freiburg

Freiburg (ots)
 Am Abend des 15.06.2016 wurde der Polizei gegen 18:15 Uhr folgender Sachverhalt gemeldet. 
Ein 10jähriges Mädchen befuhr kurz zuvor mit ihrem Fahrrad die Bötzinger Straße Richtung Ortsausgang, als sie plötzlich von einem jungen Mann in ein dortiges Gebüsch gezerrt wurde. 
Dies nahmen unabhängig voneinander zwei Passanten wahr. Der 44jährige sowie der 61jährige Mann reagierten sofort und rannten Richtung Gebüsch, woraufhin der unbekannte Täter auf seinem blauen Mountainbike flüchtete. 
Der Täter wurde folgendermaßen beschrieben: Männlich, jugendlich, kräftige Statur (mollig), rundes Gesicht, blond und etwa 170 cm groß. Er trug ein schwarzes T-Shirt mit einem hellen Aufdruck (Geist oder Schädel), eine Cargohose, ein Basecap, evtl. eine Brille und flüchtete mit einem blauen Mountainbike. 
Die Kriminalpolizei hat die Ermittlungen aufgenommen und bittet mögliche weitere Zeugen, die Hinweise auf den Tatverdächtigen geben können sich unter Tel: 0761-8825777 zu melden. 
lr 
 
Rückfragen bitte an:
Laura Riske
Polizeipräsidium Freiburg
Stabsstelle Öffentlichkeitsarbeit
Telefon: 0761 882-1011
E-Mail: freiburg.pp@polizei.bwl.de
http://www.polizei-bw.de/
Original-Content von: Polizeipräsidium Freiburg, übermittelt durch news aktuell
"""


split8 = ['2016 – 09:14 Polizeipräsidium Freiburg Freiburg (ots) Am Abend des 15.06.2016 wurde der Polizei gegen 18:15 Uhr folgender Sachverhalt gemeldet. Ein 10jähriges Mädchen befuhr kurz zuvor mit ihrem Fahrrad die Bötzinger Straße Richtung Ortsausgang, als sie plötzlich von einem jungen Mann in ein dortiges Gebüsch gezerrt wurde. Dies nahmen unabhängig voneinander zwei Passanten wahr. Der 44jährige sowie der 61jährige Mann reagierten sofort und rannten Richtung Gebüsch, woraufhin der unbekannte Täter auf seinem blauen Mountainbike flüchtete. Der Täter wurde folgendermaßen beschrieben: Männlich, jugendlich, kräftige Statur (mollig), rundes Gesicht, blond und etwa 170 cm groß. Er trug ein schwarzes T-Shirt mit einem hellen Aufdruck (Geist oder Schädel), eine Cargohose, ein Basecap, evtl. eine Brille und flüchtete mit einem blauen Mountainbike. Die Kriminalpolizei hat die Ermittlungen aufgenommen und bittet mögliche weitere Zeugen, die Hinweise auf den Tatverdächtigen geben können sich unter Tel: 0761-8825777 zu melden. lr']



###############################################################################


text9 = """
12.03.2016 – 10:30

Polizeipräsidium Mannheim

Edingen-Neckarhausen (ots)
 Wegen des Verdachts des gefährlichen Eingriffs in den Straßenverkehr ermittelt die Polizei in Edingen-Neckarhausen gegen einen bislang unbekannten Täter. Vermutlich am frühen Freitagmorgen riss der Unbekannte ein Stationierungszeichen aus dem Boden, das auf der Friedrichsfelder Straße zwischen dem Rad- und Fußweg neben einem Feldgelände, zwischen der Einmündung Lilienstraße und Ortseingang Edingen verankert war und warf es auf die Fahrbahn. Kurz vor 5 Uhr überfuhr eine 49-jährige Nissan-Fahrerin das metallene Stationierungszeichen und riss sich dabei zunächst unbemerkt die Ölwanne auf. Die Autofahrerin kam noch bis zum Amselweg, wo ihr Fahrzeug liegenblieb. Der Sachschaden wird auf über 1000.- Euro geschätzt. Die über eine längere Strecke sich hingezogene Ölspur musste im Laufe des Freitagvormittages durch eine Spezialfirma beseitig werden. Zeugen, die Hinweise auf die Person oder Personen geben können, die das Stationierungszeichen auf die Fahrbahn war, werden gebeten, sich mit dem Polizeiposten Edingen-Neckarhausen, Tel.: 0621/892029 oder mit dem Polizeirevier Ladenburg, Tel.: 06203/9305-0 in Verbindung zu setzen. 
 
Rückfragen bitte an:

Polizeipräsidium Mannheim
Öffentlichkeitsarbeit
Norbert Schätzle
Telefon: 0621 174-1102
E-Mail: mannheim.pp@polizei.bwl.de
http://www.polizei-bw.de/
Original-Content von: Polizeipräsidium Mannheim, übermittelt durch news aktuell
"""

split9 = ['2016 – 10:30 Polizeipräsidium Mannheim Edingen-Neckarhausen (ots) Wegen des Verdachts des gefährlichen Eingriffs in den Straßenverkehr ermittelt die Polizei in Edingen-Neckarhausen gegen einen bislang unbekannten Täter. Vermutlich am frühen Freitagmorgen riss der Unbekannte ein Stationierungszeichen aus dem Boden, das auf der Friedrichsfelder Straße zwischen dem Rad- und Fußweg neben einem Feldgelände, zwischen der Einmündung Lilienstraße und Ortseingang Edingen verankert war und warf es auf die Fahrbahn. Kurz vor 5 Uhr überfuhr eine 49-jährige Nissan-Fahrerin das metallene Stationierungszeichen und riss sich dabei zunächst unbemerkt die Ölwanne auf. Die Autofahrerin kam noch bis zum Amselweg, wo ihr Fahrzeug liegenblieb. Der Sachschaden wird auf über 1000.- Euro geschätzt. Die über eine längere Strecke sich hingezogene Ölspur musste im Laufe des Freitagvormittages durch eine Spezialfirma beseitig werden. Zeugen, die Hinweise auf die Person oder Personen geben können, die das Stationierungszeichen auf die Fahrbahn war, werden gebeten, sich mit dem Polizeiposten Edingen-Neckarhausen, Tel.: 0621/892029 oder mit dem Polizeirevier Ladenburg, Tel.: 06203/9305-0 in Verbindung zu setzen.']



###############################################################################


text10 = """
09.03.2016 – 13:52

Polizeipräsidium Heilbronn

Heilbronn (ots)
 Massenbachhausen: Mehrfacher Überschlag - leichte Verletzungen Einen Schutzengel hatten die Insassen eines Ford Focus bei einem Unfall am Dienstagvormittag. Eine 26-Jährige fuhr mit ihrem PKW von Heilbronn-Kirchhausen in Richtung Massenbachhausen. Aus bislang unbekannten Gründen geriet das Fahrzeug in einer Linkskurve auf des rechte Bankett. Als die junge Frau gegensteuern wollte, geriet der Ford ins Schleudern, kam nach links von der Fahrbahn ab, überschlug sich, wurde wieder auf die Straße zurückgeschleudert und überschlug sich dort mehrfach. Wie durch ein Wunder erlitten die Fahrerin, ihr 30-jähriger Beifahrer und ihr elf Monate alter Sohn lediglich leichte Verletzungen. Am Ford entstand Totalschaden. 
Bad Rappenau-Fürfeld: Alarmanlage verscheucht Einbrecher 
Die Tür zu einer Kfz-Werkstatt in der Fürfelder Wilhelm-Hauff-Straße hebelte ein Unbekannter in der Nacht zum Mittwoch auf. Kurz nach Mitternacht gelangte der Mann so in das Gebäude, wo dann aber die Alarmanlage auslöste. Als er ohne Beute flüchtete, wurde er von einer Zeugin gesehen. Der mit einem dunklen Kapuzenshirt bekleidete Dieb ließ eine Sporttasche, in der ein Navigationsgerät lag, zurück. Der verursachte Sachschaden beläuft sich auf rund 500 Euro. 
Heilbronn: Diagnosegerät gestohlen 
Ein mehrere Tausend Euro teures Diagnosegerät stahlen Unbekannte in der Nacht zum Mittwoch aus der Werkstatt eines Heilbronner Autohauses. Die Einbrecher wuchteten die Werkstatttüre auf und gelangten durch diese in das Innere des Gebäudes. Dort brachen sie eine weitere Türe auf und nahmen das Diagnosegerät für Smart-PKW mit. Hinweise auf die Täter hat die Polizei keine. 
Heilbronn: Nach Unfall geflüchtet 
Über 1.000 Euro Schaden richtete ein Unbekannter bei einem Unfall am Montag in Heilbronn an und flüchtete. Ein 49-Jähriger parkte seinen Opel Astra in der Richard-Wagner-Straße von 11 bis 15 Uhr. In dieser Zeit fuhr der Unfallverursacher vermutlich beim Ein- oder Ausparken gegen die Fahrerseite des Astras. Da er wegfuhr, ohne seine Personalien zu hinterlassen, sucht die Polizei Zeugen, die sich beim Revier Heilbronn, Telefon 07131 104-2500, melden möchten. 
Güglingen: Auto nach Unfall in Flammen 
Völlig ausgebrannt ist in der Nacht zum Mittwoch ein PKW nach einem Unfall bei Güglingen. Ein 30-Jähriger fuhr gegen 1 Uhr mit einem VW Golf von Eibensbach in Richtung Güglingen. Auf Höhe einer Parkbucht kam das Auto aus unbekannten Gründen von der Fahrbahn ab, überschlug sich mehrfach, blieb auf dem Dach liegen und fing Feuer. Der Fahrer konnte rechtzeitig aus dem Golf klettern, übergab die Fahrzeugschlüssel einem Zeugen, nannte diesem den Namen des Besitzers und ging zu Fuß in Richtung Güglingen weg. Die Straße musste aufgrund der Lösch- und der anschließenden Bergungsarbeiten bis nach 4 Uhr gesperrt werden. Der Grund, warum der 30-Jährige wegging, liegt vermutlich darin, weil er nicht im Besitz eines Führerscheins ist. Jetzt wird gegen ihn und den Fahrzeughalter ermittelt. 
Schwaigern: Einbrecher in Wohnhaus 
Schmuckstücke und eine Uhr fielen einem Einbrecher in die Hände, der am Montagabend, kurz vor Mitternacht, in ein Wohnhaus in der Schwaigerner Ostendstraße einstieg. Der Dieb kletterte gegen 23.30 Uhr auf einen Balkon des Reihenhauses und wuchtete ein Fenster auf. Als er seine Beute hatte, kam die Bewohnerin nach Hause, er ergriff die Flucht. Die 42-Jährige hörte noch seine Schritte in der Wohnung, bekam ihn aber nicht mehr zu Gesicht. Wer am Montagabend, in der Zeit zwischen 23 Uhr und Mitternacht im Bereich der Ostendstraße eine verdächtige Person beobachtet hat oder sonstige Hinwesie geben kann, wird gebeten, sich mit dem Polizeiposten Leintal, Telefon 07138 810630, in Verbindung zu setzen. 
Neckarsulm: Rabiat und uneinsichtig 
Nicht nur weil er ordentlich alkoholischen Getränken zugesprochen hatte, sondern weil er sich aggressiv gebärdete und sogar auf den Wirt einer Gaststätte in Neckarsulm los ging, wurde am Mittwoch, kurz nach Mitternacht, die Polizei alarmiert. Obwohl die Beamten mit zwei Streifen anrückten, zeigte sich der 47-Jährige völlig uneinsichtig und weigerte sich, nach Hause zu gehen. Am Ende stellte er den Polizisten die klare Frage, "wollt ihr ein paar auf´s Maul" und griff einen Beamten mit erhobenen Fäusten an. Nachdem ihm deshalb Handschließen angelegt worden waren, durfte er in einem Streifenwagen mitfahren und ein Bett in einer Zelle des Polizeireviers benutzen, bis er seinen Rausch ausgeschlafen hatte. 
Neckarsulm: Unfallflüchtiger gesucht 
Einen weißen PKW und dessen Fahrer sucht die Polizei nach einem Unfall am Dienstagnachmittag in Neckarsulm. Der Unbekannte fuhr in der Zeit zwischen 13.30 Uhr und 16.15 mit seinem Auto durch die Goethestraße und streifte mit diesem einen vor der Christian-Schmidt-Schule geparkten blauen VW-Transporter. An diesem entstand ein Unfallschaden von mindestens 1.500 Euro. Die Polizei fand an den Beschädigungen weiße Lackantragungen. Der Unfallverursacher fuhr weiter, ohne seine Personalien zu hinterlassen. Zeugen werden gebeten, sich mit dem Polizeirevier Neckarsulm, Telefon 07132 93710, in Verbindung zu setzen. 
Heilbronn: Frau beraubt 
Von drei Männern wurde am Dienstagabend in Heilbronn eine Frau beraubt. Wie die 31-Jährige der Polizei mitteilte, war sie kurz nach 21 Uhr zu Fuß in der Unteren Neckarstraße unterwegs, als die Täter zu ihr heran traten. Einer hielt sie von hinten fest, ein anderer durchsuchte ihre Sporttasche und ihre Jackentaschen. Er fand 20 Euro Bargeld, das er einsteckte. Die Frau trat nach dem vor ihr stehenden Täter und traf ihn am Bein. Zu dieser Zeit fuhr in der Nähe ein Rettungswagen mit eingeschaltetem Signalhorn. Dies hörte das Trio und floh in Richtung Eishalle. Die Männer sprachen in einer ausländischen, vermutlich arabischen Sprache. Alle waren etwa 25 Jahre alt, hatten ein arabisches Aussehen und sportlich-schlanke Figuren. Zwei fielen auf durch eine so genannte Bushidoo-Frisur, also hinten und an der Seite kurz, oben ein etwas längeres Deckhaar. Beide sind Bartträger. Der eine war bekleidet mit einer dunklen Steppjacke, einem roten Oberteil und weißen Nike Air-Schuhen. Der andere trug eine hüftlange Bomberjacke. Der dritte Täter hatte ebenfalls einen Bart, aber mit Konturen. An ihm war das dünne, spitze Gesicht auffällig. Hinweise auf das Trio gehen an die Kriminalpolizei Heilbronn, Telefon 07131 104-4444. 
 
Rückfragen bitte an:

Polizeipräsidium Heilbronn
Telefon: 07131 104-1012
E-Mail: heilbronn.pp@polizei.bwl.de
http://www.polizei-bw.de/
Original-Content von: Polizeipräsidium Heilbronn, übermittelt durch news aktuell
"""


split10 = [
 '2016 – 13:52 Polizeipräsidium Heilbronn Heilbronn (ots)  Massenbachhausen: Mehrfacher Überschlag - leichte Verletzungen Einen Schutzengel hatten die Insassen eines Ford Focus bei einem Unfall am Dienstagvormittag. Eine 26-Jährige fuhr mit ihrem PKW von Heilbronn-Kirchhausen in Richtung Massenbachhausen. Aus bislang unbekannten Gründen geriet das Fahrzeug in einer Linkskurve auf des rechte Bankett. Als die junge Frau gegensteuern wollte, geriet der Ford ins Schleudern, kam nach links von der Fahrbahn ab, überschlug sich, wurde wieder auf die Straße zurückgeschleudert und überschlug sich dort mehrfach. Wie durch ein Wunder erlitten die Fahrerin, ihr 30-jähriger Beifahrer und ihr elf Monate alter Sohn lediglich leichte Verletzungen. Am Ford entstand Totalschaden.',
 'Bad Rappenau-Fürfeld: Alarmanlage verscheucht Einbrecher Die Tür zu einer Kfz-Werkstatt in der Fürfelder Wilhelm-Hauff-Straße hebelte ein Unbekannter in der Nacht zum Mittwoch auf. Kurz nach Mitternacht gelangte der Mann so in das Gebäude, wo dann aber die Alarmanlage auslöste. Als er ohne Beute flüchtete, wurde er von einer Zeugin gesehen. Der mit einem dunklen Kapuzenshirt bekleidete Dieb ließ eine Sporttasche, in der ein Navigationsgerät lag, zurück. Der verursachte Sachschaden beläuft sich auf rund 500 Euro.',
 'Heilbronn: Diagnosegerät gestohlen Ein mehrere Tausend Euro teures Diagnosegerät stahlen Unbekannte in der Nacht zum Mittwoch aus der Werkstatt eines Heilbronner Autohauses. Die Einbrecher wuchteten die Werkstatttüre auf und gelangten durch diese in das Innere des Gebäudes. Dort brachen sie eine weitere Türe auf und nahmen das Diagnosegerät für Smart-PKW mit. Hinweise auf die Täter hat die Polizei keine.',
 'Heilbronn: Nach Unfall geflüchtet Über 1.000 Euro Schaden richtete ein Unbekannter bei einem Unfall am Montag in Heilbronn an und flüchtete. Ein 49-Jähriger parkte seinen Opel Astra in der Richard-Wagner-Straße von 11 bis 15 Uhr. In dieser Zeit fuhr der Unfallverursacher vermutlich beim Ein- oder Ausparken gegen die Fahrerseite des Astras. Da er wegfuhr, ohne seine Personalien zu hinterlassen, sucht die Polizei Zeugen, die sich beim Revier Heilbronn, Telefon 07131 104-2500, melden möchten.',
 'Güglingen: Auto nach Unfall in Flammen Völlig ausgebrannt ist in der Nacht zum Mittwoch ein PKW nach einem Unfall bei Güglingen. Ein 30-Jähriger fuhr gegen 1 Uhr mit einem VW Golf von Eibensbach in Richtung Güglingen. Auf Höhe einer Parkbucht kam das Auto aus unbekannten Gründen von der Fahrbahn ab, überschlug sich mehrfach, blieb auf dem Dach liegen und fing Feuer. Der Fahrer konnte rechtzeitig aus dem Golf klettern, übergab die Fahrzeugschlüssel einem Zeugen, nannte diesem den Namen des Besitzers und ging zu Fuß in Richtung Güglingen weg. Die Straße musste aufgrund der Lösch- und der anschließenden Bergungsarbeiten bis nach 4 Uhr gesperrt werden. Der Grund, warum der 30-Jährige wegging, liegt vermutlich darin, weil er nicht im Besitz eines Führerscheins ist. Jetzt wird gegen ihn und den Fahrzeughalter ermittelt.',
 'Schwaigern: Einbrecher in Wohnhaus Schmuckstücke und eine Uhr fielen einem Einbrecher in die Hände, der am Montagabend, kurz vor Mitternacht, in ein Wohnhaus in der Schwaigerner Ostendstraße einstieg. Der Dieb kletterte gegen 23.30 Uhr auf einen Balkon des Reihenhauses und wuchtete ein Fenster auf. Als er seine Beute hatte, kam die Bewohnerin nach Hause, er ergriff die Flucht. Die 42-Jährige hörte noch seine Schritte in der Wohnung, bekam ihn aber nicht mehr zu Gesicht. Wer am Montagabend, in der Zeit zwischen 23 Uhr und Mitternacht im Bereich der Ostendstraße eine verdächtige Person beobachtet hat oder sonstige Hinwesie geben kann, wird gebeten, sich mit dem Polizeiposten Leintal, Telefon 07138 810630, in Verbindung zu setzen.',
 'Neckarsulm: Rabiat und uneinsichtig Nicht nur weil er ordentlich alkoholischen Getränken zugesprochen hatte, sondern weil er sich aggressiv gebärdete und sogar auf den Wirt einer Gaststätte in Neckarsulm los ging, wurde am Mittwoch, kurz nach Mitternacht, die Polizei alarmiert. Obwohl die Beamten mit zwei Streifen anrückten, zeigte sich der 47-Jährige völlig uneinsichtig und weigerte sich, nach Hause zu gehen. Am Ende stellte er den Polizisten die klare Frage, "wollt ihr ein paar auf´s Maul" und griff einen Beamten mit erhobenen Fäusten an. Nachdem ihm deshalb Handschließen angelegt worden waren, durfte er in einem Streifenwagen mitfahren und ein Bett in einer Zelle des Polizeireviers benutzen, bis er seinen Rausch ausgeschlafen hatte.',
 'Neckarsulm: Unfallflüchtiger gesucht Einen weißen PKW und dessen Fahrer sucht die Polizei nach einem Unfall am Dienstagnachmittag in Neckarsulm. Der Unbekannte fuhr in der Zeit zwischen 13.30 Uhr und 16.15 mit seinem Auto durch die Goethestraße und streifte mit diesem einen vor der Christian-Schmidt-Schule geparkten blauen VW-Transporter. An diesem entstand ein Unfallschaden von mindestens 1.500 Euro. Die Polizei fand an den Beschädigungen weiße Lackantragungen. Der Unfallverursacher fuhr weiter, ohne seine Personalien zu hinterlassen. Zeugen werden gebeten, sich mit dem Polizeirevier Neckarsulm, Telefon 07132 93710, in Verbindung zu setzen.',
 'Heilbronn: Frau beraubt Von drei Männern wurde am Dienstagabend in Heilbronn eine Frau beraubt. Wie die 31-Jährige der Polizei mitteilte, war sie kurz nach 21 Uhr zu Fuß in der Unteren Neckarstraße unterwegs, als die Täter zu ihr heran traten. Einer hielt sie von hinten fest, ein anderer durchsuchte ihre Sporttasche und ihre Jackentaschen. Er fand 20 Euro Bargeld, das er einsteckte. Die Frau trat nach dem vor ihr stehenden Täter und traf ihn am Bein. Zu dieser Zeit fuhr in der Nähe ein Rettungswagen mit eingeschaltetem Signalhorn. Dies hörte das Trio und floh in Richtung Eishalle. Die Männer sprachen in einer ausländischen, vermutlich arabischen Sprache. Alle waren etwa 25 Jahre alt, hatten ein arabisches Aussehen und sportlich-schlanke Figuren. Zwei fielen auf durch eine so genannte Bushidoo-Frisur, also hinten und an der Seite kurz, oben ein etwas längeres Deckhaar. Beide sind Bartträger. Der eine war bekleidet mit einer dunklen Steppjacke, einem roten Oberteil und weißen Nike Air-Schuhen. Der andere trug eine hüftlange Bomberjacke. Der dritte Täter hatte ebenfalls einen Bart, aber mit Konturen. An ihm war das dünne, spitze Gesicht auffällig. Hinweise auf das Trio gehen an die Kriminalpolizei Heilbronn, Telefon 07131 104-4444.',
 ]

split10_2 = [
 '2016 – 13:52 Polizeipräsidium Heilbronn Heilbronn (ots) Massenbachhausen: Mehrfacher Überschlag - leichte Verletzungen Einen Schutzengel hatten die Insassen eines Ford Focus bei einem Unfall am Dienstagvormittag. Eine 26-Jährige fuhr mit ihrem PKW von Heilbronn-Kirchhausen in Richtung Massenbachhausen. Aus bislang unbekannten Gründen geriet das Fahrzeug in einer Linkskurve auf des rechte Bankett. Als die junge Frau gegensteuern wollte, geriet der Ford ins Schleudern, kam nach links von der Fahrbahn ab, überschlug sich, wurde wieder auf die Straße zurückgeschleudert und überschlug sich dort mehrfach. Wie durch ein Wunder erlitten die Fahrerin, ihr 30-jähriger Beifahrer und ihr elf Monate alter Sohn lediglich leichte Verletzungen. Am Ford entstand Totalschaden.',
 'Bad Rappenau-Fürfeld: Alarmanlage verscheucht Einbrecher Die Tür zu einer Kfz-Werkstatt in der Fürfelder Wilhelm-Hauff-Straße hebelte ein Unbekannter in der Nacht zum Mittwoch auf. Kurz nach Mitternacht gelangte der Mann so in das Gebäude, wo dann aber die Alarmanlage auslöste. Als er ohne Beute flüchtete, wurde er von einer Zeugin gesehen. Der mit einem dunklen Kapuzenshirt bekleidete Dieb ließ eine Sporttasche, in der ein Navigationsgerät lag, zurück. Der verursachte Sachschaden beläuft sich auf rund 500 Euro.',
 'Heilbronn: Diagnosegerät gestohlen Ein mehrere Tausend Euro teures Diagnosegerät stahlen Unbekannte in der Nacht zum Mittwoch aus der Werkstatt eines Heilbronner Autohauses. Die Einbrecher wuchteten die Werkstatttüre auf und gelangten durch diese in das Innere des Gebäudes. Dort brachen sie eine weitere Türe auf und nahmen das Diagnosegerät für Smart-PKW mit. Hinweise auf die Täter hat die Polizei keine.',
 'Heilbronn: Nach Unfall geflüchtet Über 1.000 Euro Schaden richtete ein Unbekannter bei einem Unfall am Montag in Heilbronn an und flüchtete. Ein 49-Jähriger parkte seinen Opel Astra in der Richard-Wagner-Straße von 11 bis 15 Uhr. In dieser Zeit fuhr der Unfallverursacher vermutlich beim Ein- oder Ausparken gegen die Fahrerseite des Astras. Da er wegfuhr, ohne seine Personalien zu hinterlassen, sucht die Polizei Zeugen, die sich beim Revier Heilbronn, Telefon 07131 104-2500, melden möchten.',
 'Güglingen: Auto nach Unfall in Flammen Völlig ausgebrannt ist in der Nacht zum Mittwoch ein PKW nach einem Unfall bei Güglingen. Ein 30-Jähriger fuhr gegen 1 Uhr mit einem VW Golf von Eibensbach in Richtung Güglingen. Auf Höhe einer Parkbucht kam das Auto aus unbekannten Gründen von der Fahrbahn ab, überschlug sich mehrfach, blieb auf dem Dach liegen und fing Feuer. Der Fahrer konnte rechtzeitig aus dem Golf klettern, übergab die Fahrzeugschlüssel einem Zeugen, nannte diesem den Namen des Besitzers und ging zu Fuß in Richtung Güglingen weg. Die Straße musste aufgrund der Lösch- und der anschließenden Bergungsarbeiten bis nach 4 Uhr gesperrt werden. Der Grund, warum der 30-Jährige wegging, liegt vermutlich darin, weil er nicht im Besitz eines Führerscheins ist. Jetzt wird gegen ihn und den Fahrzeughalter ermittelt.',
 'Schwaigern: Einbrecher in Wohnhaus Schmuckstücke und eine Uhr fielen einem Einbrecher in die Hände, der am Montagabend, kurz vor Mitternacht, in ein Wohnhaus in der Schwaigerner Ostendstraße einstieg. Der Dieb kletterte gegen 23.30 Uhr auf einen Balkon des Reihenhauses und wuchtete ein Fenster auf. Als er seine Beute hatte, kam die Bewohnerin nach Hause, er ergriff die Flucht. Die 42-Jährige hörte noch seine Schritte in der Wohnung, bekam ihn aber nicht mehr zu Gesicht. Wer am Montagabend, in der Zeit zwischen 23 Uhr und Mitternacht im Bereich der Ostendstraße eine verdächtige Person beobachtet hat oder sonstige Hinwesie geben kann, wird gebeten, sich mit dem Polizeiposten Leintal, Telefon 07138 810630, in Verbindung zu setzen.',
 'Neckarsulm: Rabiat und uneinsichtig Nicht nur weil er ordentlich alkoholischen Getränken zugesprochen hatte, sondern weil er sich aggressiv gebärdete und sogar auf den Wirt einer Gaststätte in Neckarsulm los ging, wurde am Mittwoch, kurz nach Mitternacht, die Polizei alarmiert. Obwohl die Beamten mit zwei Streifen anrückten, zeigte sich der 47-Jährige völlig uneinsichtig und weigerte sich, nach Hause zu gehen. Am Ende stellte er den Polizisten die klare Frage, "wollt ihr ein paar auf´s Maul" und griff einen Beamten mit erhobenen Fäusten an. Nachdem ihm deshalb Handschließen angelegt worden waren, durfte er in einem Streifenwagen mitfahren und ein Bett in einer Zelle des Polizeireviers benutzen, bis er seinen Rausch ausgeschlafen hatte.',
 'Neckarsulm: Unfallflüchtiger gesucht Einen weißen PKW und dessen Fahrer sucht die Polizei nach einem Unfall am Dienstagnachmittag in Neckarsulm. Der Unbekannte fuhr in der Zeit zwischen 13.30 Uhr und 16.15 mit seinem Auto durch die Goethestraße und streifte mit diesem einen vor der Christian-Schmidt-Schule geparkten blauen VW-Transporter. An diesem entstand ein Unfallschaden von mindestens 1.500 Euro. Die Polizei fand an den Beschädigungen weiße Lackantragungen. Der Unfallverursacher fuhr weiter, ohne seine Personalien zu hinterlassen. Zeugen werden gebeten, sich mit dem Polizeirevier Neckarsulm, Telefon 07132 93710, in Verbindung zu setzen.',
 'Heilbronn: Frau beraubt Von drei Männern wurde am Dienstagabend in Heilbronn eine Frau beraubt. Wie die 31-Jährige der Polizei mitteilte, war sie kurz nach 21 Uhr zu Fuß in der Unteren Neckarstraße unterwegs, als die Täter zu ihr heran traten. Einer hielt sie von hinten fest, ein anderer durchsuchte ihre Sporttasche und ihre Jackentaschen. Er fand 20 Euro Bargeld, das er einsteckte. Die Frau trat nach dem vor ihr stehenden Täter und traf ihn am Bein. Zu dieser Zeit fuhr in der Nähe ein Rettungswagen mit eingeschaltetem Signalhorn. Dies hörte das Trio und floh in Richtung Eishalle. Die Männer sprachen in einer ausländischen, vermutlich arabischen Sprache. Alle waren etwa 25 Jahre alt, hatten ein arabisches Aussehen und sportlich-schlanke Figuren. Zwei fielen auf durch eine so genannte Bushidoo-Frisur, also hinten und an der Seite kurz, oben ein etwas längeres Deckhaar. Beide sind Bartträger. Der eine war bekleidet mit einer dunklen Steppjacke, einem roten Oberteil und weißen Nike Air-Schuhen. Der andere trug eine hüftlange Bomberjacke. Der dritte Täter hatte ebenfalls einen Bart, aber mit Konturen. An ihm war das dünne, spitze Gesicht auffällig. Hinweise auf das Trio gehen an die Kriminalpolizei Heilbronn, Telefon 07131 104-4444.',
 ]



###############################################################################


text11 = """
25.03.2016 – 10:00

Polizeipräsidium Ludwigsburg

Ludwigsburg (ots)
 Weil im Schönbuch: Brand von Container 
Am Donnerstag gegen 17.30 Uhr wurde in einem Container an der Seesteige in Weil im Schönbuch ein Brand festgestellt. Darin befanden sich Holzdielen für das Seenachtsfest, welche durch unbekannte Täter entzündet worden waren. Der Schaden wird auf ca. 1.000 Euro beziffert. Neben einem Streifenwagen der Polizei war die Feuerwehr mit 15 Einsatzkräften und drei Fahrzeugen vor Ort. 
Böblingen: Rauchentwicklung in Flüchtlingsunterkunft 
Am frühen Freitag gegen 00.40 Uhr löste in einer Böblinger Flüchtlingsunterkunft in der Sindelfinger Straße ein Brandalarm aus. Bei Eintreffen der Einsatzkräfte war die Küche im Dachgeschoss stark verraucht. Ursächlich war verbranntes Essen auf dem Herd. Dabei wurden keine Personen verletzt und es entstand kein Sachschaden. Die Polizei war mit zwei Streifenwagen und die Feuerwehr mit vier Fahrzeugen und 21 Einsatzkräften vor Ort. 
 
Rückfragen bitte an:

Polizeipräsidium Ludwigsburg
Telefon: 07141 18-9
E-Mail: ludwigsburg.pp@polizei.bwl.de
http://www.polizei-bw.de/
Original-Content von: Polizeipräsidium Ludwigsburg, übermittelt durch news aktuell
"""


split11 = [
    '2016 – 10:00 Polizeipräsidium Ludwigsburg Ludwigsburg (ots) Weil im Schönbuch: Brand von Container Am Donnerstag gegen 17.30 Uhr wurde in einem Container an der Seesteige in Weil im Schönbuch ein Brand festgestellt. Darin befanden sich Holzdielen für das Seenachtsfest, welche durch unbekannte Täter entzündet worden waren. Der Schaden wird auf ca. 1.000 Euro beziffert. Neben einem Streifenwagen der Polizei war die Feuerwehr mit 15 Einsatzkräften und drei Fahrzeugen vor Ort.',
    'Böblingen: Rauchentwicklung in Flüchtlingsunterkunft Am frühen Freitag gegen 00.40 Uhr löste in einer Böblinger Flüchtlingsunterkunft in der Sindelfinger Straße ein Brandalarm aus. Bei Eintreffen der Einsatzkräfte war die Küche im Dachgeschoss stark verraucht. Ursächlich war verbranntes Essen auf dem Herd. Dabei wurden keine Personen verletzt und es entstand kein Sachschaden. Die Polizei war mit zwei Streifenwagen und die Feuerwehr mit vier Fahrzeugen und 21 Einsatzkräften vor Ort.',
    ]


###############################################################################

text12 = """
31.08.2016 – 11:00

Polizeipräsidium Heilbronn

Heilbronn (ots)
 Hohenlohekreis 
Öhringen-Ohrnberg:  Feuer im Keller 
Mit einem Sachschaden in fünfstelliger Euro-Höhe und einem Leichtverletzten endete ein Brand am Dienstagabend in Öhringen-Ohrnberg. Im Kellerraum eines Wohnhauses in der Friedrichstraße hatte, vermutlich aufgrund eines technischen Defektes, eine Tiefkühltruhe Feuer gefangen. Vier weitere Kühlgeräte wurden dadurch entzündet und gingen in Flammen auf. Durch die Hitzeeinwirkung zerbrach das Kellerfenster, so dass das Feuer auch die Hausfassade und eine angrenzende Garage in Mitleidenschaft zog. 55 Feuerwehrleute der umliegenden Wehren Baumerlenbach, Möglingen, Ohrnberg und Öhringen waren vor Ort und löschten den Brand. Ein Rettungsteam brachte einen 76-jährigen Hausbewohner mit Verdacht auf eine Rauchgasvergiftung vorsorglich ins Krankenhaus. 
Öhringen:  Hase gegen Motorrad 
Am Dienstagmorgen, gegen 6 Uhr, kam einem Hasen beim Überqueren der Landesstraße zwischen Bitzfeld und Bretzfeld ein Motorrad in die Quere. Das Langohr überlebte die Kollision mit der Kawasaki des 40-jährigen Motorradfahrers nicht. Der Biker indes hatte Glück und wurde nicht verletzt. An seiner Maschine entstand ein Schaden in Höhe von 200 Euro. 
Künzelsau/Ingelfingen:  Gefährlich überholt und geflüchtet - Zeugen gesucht! 
Einen Verkehrsunfall hat ein bislang noch nicht ermittelter Fahrzeugführer am Dienstagabend bei Ingelfingen verursacht. Gegen 21.15 Uhr überholte der Unbekannte auf der Landesstraße in Richtung Künzelsau trotz Gegenverkehrs einen weißen VW Golf, besetzt mit einer jungen Fahrschülerin und deren 43 Jahre alten Fahrlehrer. Ein entgegenkommender Fiat-Lenker musste, um einen Zusammenstoß mit dem überholenden Auto zu vermeiden, abbremsen und nach rechts ausweichen. Der hinter dem 63-Jährigen befindliche 18-jährige Audi-Fahrer bremste seinen A 6 ebenfalls ab und lenkte nach rechts. Eine nachfolgende 38 Jahre alte Ford-Fahrerin erkannte die Situation allerdings zu spät und konnte nicht mehr rechtzeitig anhalten. Die Frau fuhr mit ihrem Pkw auf den Audi des 18-Jährigen auf. Dabei erlitt sie leichte Verletzungen und musste zur medizinischen Behandlung ins Krankenhaus. Die junge Frau am Steuer des Fahrschulautos erlitt einen Schock. Am Ford Fiesta und dem Audi-Kombi entstand Sachschaden in Höhe von 7.000 Euro. Der Überholer fuhr unterdessen davon, ohne sich um den Verkehrsunfall zu kümmern. Er war mit einem Renault Twingo, neueren Baujahres, mit ÖHR-Zulassung unterwegs. Die Polizei Künzelsau sucht Zeugen zu der Unfallflucht. Diese werden gebeten, sich unter der Telefonnummer 07940 9400 zu melden. 
Künzelsau:  Schild kam geflogen - 1.000 Euro Sachschaden 
Wie aus dem Nichts schleuderte am Dienstagnachmittag auf der Bundesstraße 19 bei Künzelsau offenbar ein unbekannter Gegenstand gegen das Auto einer Verkehrsteilnehmerin. Die 29-Jährige war gegen 14.30 Uhr mit ihrem VW Passat in Richtung Gaisbach unterwegs als im Verlauf einer Linkskurve, etwa 100 Meter vor der Ausfahrt "Nord", ein blaues Schild oder ähnliches gegen ihren Pkw flog. Dabei wurde sowohl die Frontscheibe wie auch die Motorhaube des VW beschädigt. Der Gegenstand konnte nach dem Unfall nicht mehr aufgefunden werden. Auch ist es nicht nachvollziehbar, woher er stammt. Hinweise nimmt die Polizei in Künzelsau unter der Telefonnummer 07940 9400 entgegen. 
Künzelsau:  Parkplatzrempler ermittelt 
Nach einem missglückten Rangiermanöver in einem Künzelsauer Parkhaus in der Bergstraße ist ein Autofahrer an Dienstagvormittag einfach weitergefahren. Er hatte mit seinem Audi A 4 einen dort abgestellten BMW touchiert und einen Schaden von über 1.000 Euro verursacht. Zeugen hatten den Vorfall allerdings beobachtet und das Kennzeichen des Audi notiert. Der Fahrer, ein 89-jähriger Mann, konnte somit schnell ermittelt werden. Er gab an, den Anstoß nicht bemerkt zu haben. Gegen ihn werden nun verkehrsrechtliche Maßnahmen eingeleitet. 
Pfedelbach-Windischenbach:  Audi gestohlen 
Seinen Augen glaubte wohl ein Autobesitzer in Pfedelbach-Windischenbach am Mittwochmorgen nicht zu trauen. Der Mann hatte am Mittwochnachmittag, gegen 15.30 Uhr, seinen Audi vor dem Wohnhaus im Birnbaumweg abgestellt. Als er morgens, gegen 6.30 Uhr, losfahren wollte, war das Auto weg. Offenbar war es Dieben gelungen, den schwarzen Audi A 5, Typ B8, mit dem amtlichen Kennzeichen KÜN-PM 136, auf bislang nicht bekannte Weise zu starten und zu entwenden. Das Fahrzeug hatte einen Wert von etwa 25.000 Euro. Die Öhringer Polizei nimmt unter der Telefonnummer 07941 9300 sachdienliche Hinweise zu der Tat oder dem Verbleib des Autos entgegen. 
Für Rückfragen stehen wir Ihnen unter der Telefonnummer 07131 104-1010 gerne zur Verfügung. 
 
Rückfragen bitte an:

Polizeipräsidium Heilbronn
Telefon: 07131 104-1010
E-Mail: heilbronn.pp.stab.oe@polizei.bwl.de
http://www.polizei-bw.de/
Original-Content von: Polizeipräsidium Heilbronn, übermittelt durch news aktuell
"""

split12 = [
 '2016 – 11:00 Polizeipräsidium Heilbronn Heilbronn (ots) Hohenlohekreis  Öhringen-Ohrnberg: Feuer im Keller Mit einem Sachschaden in fünfstelliger Euro-Höhe und einem Leichtverletzten endete ein Brand am Dienstagabend in Öhringen-Ohrnberg. Im Kellerraum eines Wohnhauses in der Friedrichstraße hatte, vermutlich aufgrund eines technischen Defektes, eine Tiefkühltruhe Feuer gefangen. Vier weitere Kühlgeräte wurden dadurch entzündet und gingen in Flammen auf. Durch die Hitzeeinwirkung zerbrach das Kellerfenster, so dass das Feuer auch die Hausfassade und eine angrenzende Garage in Mitleidenschaft zog. 55 Feuerwehrleute der umliegenden Wehren Baumerlenbach, Möglingen, Ohrnberg und Öhringen waren vor Ort und löschten den Brand. Ein Rettungsteam brachte einen 76-jährigen Hausbewohner mit Verdacht auf eine Rauchgasvergiftung vorsorglich ins Krankenhaus.',
 'Öhringen: Hase gegen Motorrad Am Dienstagmorgen, gegen 6 Uhr, kam einem Hasen beim Überqueren der Landesstraße zwischen Bitzfeld und Bretzfeld ein Motorrad in die Quere. Das Langohr überlebte die Kollision mit der Kawasaki des 40-jährigen Motorradfahrers nicht. Der Biker indes hatte Glück und wurde nicht verletzt. An seiner Maschine entstand ein Schaden in Höhe von 200 Euro.',
 'Künzelsau/Ingelfingen: Gefährlich überholt und geflüchtet - Zeugen gesucht! Einen Verkehrsunfall hat ein bislang noch nicht ermittelter Fahrzeugführer am Dienstagabend bei Ingelfingen verursacht. Gegen 21.15 Uhr überholte der Unbekannte auf der Landesstraße in Richtung Künzelsau trotz Gegenverkehrs einen weißen VW Golf, besetzt mit einer jungen Fahrschülerin und deren 43 Jahre alten Fahrlehrer. Ein entgegenkommender Fiat-Lenker musste, um einen Zusammenstoß mit dem überholenden Auto zu vermeiden, abbremsen und nach rechts ausweichen. Der hinter dem 63-Jährigen befindliche 18-jährige Audi-Fahrer bremste seinen A 6 ebenfalls ab und lenkte nach rechts. Eine nachfolgende 38 Jahre alte Ford-Fahrerin erkannte die Situation allerdings zu spät und konnte nicht mehr rechtzeitig anhalten. Die Frau fuhr mit ihrem Pkw auf den Audi des 18-Jährigen auf. Dabei erlitt sie leichte Verletzungen und musste zur medizinischen Behandlung ins Krankenhaus. Die junge Frau am Steuer des Fahrschulautos erlitt einen Schock. Am Ford Fiesta und dem Audi-Kombi entstand Sachschaden in Höhe von 7.000 Euro. Der Überholer fuhr unterdessen davon, ohne sich um den Verkehrsunfall zu kümmern. Er war mit einem Renault Twingo, neueren Baujahres, mit ÖHR-Zulassung unterwegs. Die Polizei Künzelsau sucht Zeugen zu der Unfallflucht. Diese werden gebeten, sich unter der Telefonnummer 07940 9400 zu melden.',
 'Künzelsau: Schild kam geflogen - 1.000 Euro Sachschaden Wie aus dem Nichts schleuderte am Dienstagnachmittag auf der Bundesstraße 19 bei Künzelsau offenbar ein unbekannter Gegenstand gegen das Auto einer Verkehrsteilnehmerin. Die 29-Jährige war gegen 14.30 Uhr mit ihrem VW Passat in Richtung Gaisbach unterwegs als im Verlauf einer Linkskurve, etwa 100 Meter vor der Ausfahrt "Nord", ein blaues Schild oder ähnliches gegen ihren Pkw flog. Dabei wurde sowohl die Frontscheibe wie auch die Motorhaube des VW beschädigt. Der Gegenstand konnte nach dem Unfall nicht mehr aufgefunden werden. Auch ist es nicht nachvollziehbar, woher er stammt. Hinweise nimmt die Polizei in Künzelsau unter der Telefonnummer 07940 9400 entgegen.',
 'Künzelsau: Parkplatzrempler ermittelt Nach einem missglückten Rangiermanöver in einem Künzelsauer Parkhaus in der Bergstraße ist ein Autofahrer an Dienstagvormittag einfach weitergefahren. Er hatte mit seinem Audi A 4 einen dort abgestellten BMW touchiert und einen Schaden von über 1.000 Euro verursacht. Zeugen hatten den Vorfall allerdings beobachtet und das Kennzeichen des Audi notiert. Der Fahrer, ein 89-jähriger Mann, konnte somit schnell ermittelt werden. Er gab an, den Anstoß nicht bemerkt zu haben. Gegen ihn werden nun verkehrsrechtliche Maßnahmen eingeleitet.',
 'Pfedelbach-Windischenbach: Audi gestohlen Seinen Augen glaubte wohl ein Autobesitzer in Pfedelbach-Windischenbach am Mittwochmorgen nicht zu trauen. Der Mann hatte am Mittwochnachmittag, gegen 15.30 Uhr, seinen Audi vor dem Wohnhaus im Birnbaumweg abgestellt. Als er morgens, gegen 6.30 Uhr, losfahren wollte, war das Auto weg. Offenbar war es Dieben gelungen, den schwarzen Audi A 5, Typ B8, mit dem amtlichen Kennzeichen KÜN-PM 136, auf bislang nicht bekannte Weise zu starten und zu entwenden. Das Fahrzeug hatte einen Wert von etwa 25.000 Euro. Die Öhringer Polizei nimmt unter der Telefonnummer 07941 9300 sachdienliche Hinweise zu der Tat oder dem Verbleib des Autos entgegen. Für Rückfragen stehen wir Ihnen unter der Telefonnummer 07131 104-1010 gerne zur Verfügung.',
 ]



###############################################################################


text13 = """
05.02.2016 – 09:46

Polizeipräsidium Aalen

Rems-Murr-Kreis: (ots)
 Schorndorf: Von Fahrbahn abgekommen 
Ein 36-jähriger Golf-Fahrer war offenbar durch das Bedienen seines Autoradios derart abgelenkt, dass er beim Befahren der B 29 zwischen Urbach und Schorndorf vorausfahrende zu spät wahrnahm. Er musste zur Vermeidung eines Unfalls nach rechts ausweichen. Hierbei verlor er die Kontrolle über sein Auto und prallte in die Leitschutzplanken. Der Autofahrer hatte Glück und blieb bei dem Unfall am Donnerstagabend gegen 21 Uhr unverletzt. Sein Auto, an dem ein Sachschaden in Höhe von ca. 5000 Euro entstand, musste abgeschleppt werden. 
Schorndorf: Auffahrunfall 
Zwischen Schorndorf und Miedelsbach erkannte ein 38-jähriger Corsa-Fahrer auf der Umgehungsstraße zu spät das Halten vorausfahrender Autos. Er krachte auf das Fahrzeugheck einer Mercedes-Fahrerin. Beim Unfall, der sich am Donnerstag gegen 17.30 Uhr ereignete, blieben die Insassen unverletzt. Es entstand Sachschaden in Höhe von ca. 6000 Euro. 
Alfdorf: Auto übersehen 
Ein 20-jähriger VW-Lenker befuhr am Donnerstag gegen 15 Uhr die Hauptstraße und beabsichtigte nach links auf den Kundenparkplatz eines Lebensmittelgeschäft einzubiegen. Dabei übersah er einen Pkw Mitsubishi, der ihm entgegen kam. Der 50-jährige Autofahrer konnte dem abbiegenden Auto nicht mehr ausweichen. Beim Zusammenstoß entstand an den Unfallautos 10000 Euro Sachschaden. 
Fellbach: Auffahrunfall 
2000 Euro ist die Schadensbilanz eines Auffahrunfalls, welcher sich am Donnterstag gegen 18.30 Uhr in der Schorndorf Straße ereignete. Ein 22-jähriger Toyota-Fahrer war vor einer Ampelanlage unachtsam und fuhr auf den vor ihm haltenden Golf auf. 
Kernen im Remstal: Unfallflucht 
Ein Unfallverursacher beschädigte einen in der Sudentenstraße zur Einmündung Kerlterstraße geparkten VW Polo und entfernte sich anschließend von der Unfallstelle. Der Verursacher hinterließ einen Sachschaden in Höhe von ca. 1500 Euro. An Hand der Unfallspuren ist davon auszugehen, dass ein Lkw am Unfall beteiligt war. Hinweise zum Unfallgeschehen, welches sich zwischen Mittwoch- und Donnerstagnachmittag ereignete, nimmt die Polizei in Fellbach unter Tel. 0711/57720 entgegen. 
Waiblingen: Unfall zwischen zwei jungen Verkehrsteilnehmern 
Am Donnerstagnachmittag ereignete sich gegen 16:30 Uhr ein Verkehrsunfall, bei dem zwei  junge Verkehrsteilnehmer beteiligt waren. Ein 21-Jähriger befuhr mit seinem VW-Golf die Emil-Münz-Straße in Richtung Eisentalstraße. Beim Einfahren in den dortigen Einmündungsbereich übersah er eine von rechts kommende 19-jährige VW-Golf-Fahrerin. Es kam zum Zusammenstoß. Bei dem Unfall wurde niemand verletzt, es entstand allerdings ein Sachschaden von insgesamt ca. 2000 Euro. 
Waiblingen: Unfallverursacher ging flüchtig 
Gegen 24 Uhr am Donnerstag fuhr ein bislang noch unbekannter Fahrzeugführer rückwärts gegen ein Verkehrszeichen im Bereich des Taxi-Rondells beim Bahnhof und entfernte sich anschließend unerlaubt. Es gibt Hinweise auf den Fahrer, die Ermittlungen dauern derzeit noch an. 
Korb: Unfall beim Rückwärtsfahren 
Ein Schaden in bislang noch unbekannter Höhe entstand bei einem Verkehrsunfall am Donnerstagabend gegen 22.30 Uhr. Ein 23 jähriger Skoda-Fahrer hielt am rechten Fahrbahnrand der Steinstraße an. Gerade als eine 55-Jährige mit ihrem VW an dem Skoda vorbeifahren wollte setzte der 23-Jährige zurück um einem anderen Auto auszuweichen, welches zu diesem Zeitpunkt in die Straße einfuhr. Es kam zur Kollision zwischen dem Skoda und dem VW. 
Weinstadt: Unter Drogeneinfluss unterwegs 
Gegen 22:30 Uhr am Donnerstag fiel zwei Polizeibeamten ein Volvo-Fahrer auf, welcher mit überhöhter Geschwindigkeit und ohne beim Abbiegen zu blinken die Bahnhofstraße in Richtung Theodor-Heuss-Straße befuhr. Bei einer daraufhin durchgeführten Kontrolle stellten die Polizisten Anzeichen dafür fest, dass der 32-jährige Volvo-Fahrer unter Drogeneinfluss stand. Ein noch vor Ort durchgeführter Drogenschnelltest bestätigte diese Vermutung. Dem 32-Jährigen wurde die Weiterfahrt untersagt. Auch musste er zu einer richterlich angeordneten Blutentnahme mit ins Krankenhaus kommen. Bringt auch diese entsprechende Ergebnisse, muss der Mann mit führerscheinrechtlichen Konsequenzen rechnen. 
Waiblingen: Unfall zwischen Lkw und Pkw 
Ein 74 Jahre alter BMW-Fahrer wollte am Donnerstagvormittag in einen Parkplatz bei der Heinrich-Küderli-Straße einfahren. Dabei streifte er in Folge von Unachtsamkeit die gerade hochfahrende Ladebordwand eines auf dem Parkplatz befindlichen Lkw. Hierbei entstand ein Schaden von ca. 400 Euro. 
Waiblingen: Hilfslieferung gestohlen 
Im Zeitraum zwischen Dienstag und Donnerstag drang ein bislang unbekannter Dieb in einen Keller in der Salierstraße ein. Von dort entwendete er 500 Paar Schuhe in Originalkartons im Wert von ca. 2000 Euro, welche eigentlich für den Versand nach Afrika bestimmt waren. Mögliche Zeugen werden gebeten, sich unter der Tel: 07151 950 422 bei der Polizei in Waiblingen zu melden. 
Waiblingen: Unbekannter zerkratzt Auto 
Ein bislang unbekannter Täter verursachte am Donnerstagnachmittag zwischen 14:30 Uhr und 17 Uhr einen Schaden von ca. 1500 Euro an einem in der Fronackerstraße geparkten Pkw Renault, indem er die komplette rechte Fahrzeugseite zerkratzte. Hinweise nimmt die Polizei in Waiblingen unter der Tel: 07151 950 422 entgegen. 
Remshalden: Unfall nach Vorfahrtsverstoß 
Eine 28-jährige VW-Lenkerin wollte am Donnerstagvormittag gegen 10:30 Uhr von der Falkenstraße nach links in die Wilhelm-Enßle-Straße abbiegen. Hierbei übersah sie einen von rechts heranfahrenden 74 Jahre alten Audi-Fahrer. Es kam zum Zusammenstoß, bei welchem ein Schaden in noch unbekannter Höhe entstand. 
Waiblingen: Autoscheibe eingeschlagen 
Bei einem in der Badstraße abgestellten Pkw wurde durch einen bislang unbekannten Täter die hintere linke Scheibe eingeschlagen. Der Vorfall ereignete sich im Zeitraum von 22:15 Uhr am Mittwoch und 06:30 Uhr am Donnerstag. Nach derzeitigem Kenntnisstand entwendete der Dieb ein Klappmesser aus dem Ford Fiesta. Hinweise nimmt die Polizei in Waiblingen unter der Tel: 07151 950 422 entgegen. 
Murrhardt: Rollerfahrer gestürzt 
Ein 55-jähriger Rollerfahrer befuhr am Donnerstagabend gegen 22 Uhr die L 1066 zwischen Murrhardt und Fornsbach. In einer Linkskurve kam der Biker nach rechts von der Fahrbahn ab und stürzte. Der Verletzte wurde an der Unfallstelle von einem Passanten ohnmächtig angetroffen. Wie sich später in einer Klinik herausstellte, war der Zweiradfahrer erheblich alkoholisiert, weshalb ein Blutprobe erhoben wurde. Zudem stellte sich heraus, dass der Roller nicht zugelassen war und der 55-Jährige nicht in Besitz der erforderlichen Fahrerlaubnis war. Der Motorradfahrer muss nun mit einer Strafanzeige rechnen. 
Backnang: Von Fahrbahn abgekommen 
Ein 57-jähriger Opel-Fahrer befuhr am Donnerstag gegen 15.15 Uhr die B 14 in Richtung Stuttgart. Bei der Anschlussstelle Backnang Mitte überfuhr er in einer Linkskurve infolge Unachtsamkeit eine Verkehrsinsel. Anschließend kam der Unfallwagen an einer Böschung zum Stehen. Beim Unfall entstand Sachschaden in Höhe von ca. 6000 Euro. Weil am Unterboden des Unfallwagens die Ölwanne beschädigt worden war, wurde zur Säuberung und Absicherung der Unfallstelle die Straßenmeisterei hinzugezogen. 
Backnang: Unfallflucht 
In der Schöntaler Straße beschädigte ein Unfallverursacher beim Vorbeifahren den Außenspiegel eines dort geparkten VW Golfs. Hinweise zum Unfallgeschehen, welches sich am Donnerstag zwischen 10 Uhr und 12 Uhr ereignete, nimmt die Polizei in Backnang unter Tel. 07191/9090 entgegen. 
Schwaikheim: Vorfahrt  nicht gewährt - Verkehrsunfall 
2000 Euro Schaden ist die Bilanz eines Verkehrsunfalles, der sich am Donnerstag gegen 13 Uhr ereignete. Eine 43-jährige Ford-Fahrerin befuhr mit ihrem Pkw die Brunnenstraße und übersah dabei eine 37 Jährige, welchem mit ihrem VW aus der Aispachstraße in die Brunnenstraße einfahren wollte. Im Kreuzungsbereich kam es zum Zusammenstoß, verletzt wurde niemand. 
 
Rückfragen bitte an:

Polizeipräsidium Aalen
Öffentlichkeitsarbeit
Telefon: 07361 580-105
E-Mail: aalen.pp.stab.oe@polizei.bwl.de
http://www.polizei-bw.de/
Original-Content von: Polizeipräsidium Aalen, übermittelt durch news aktuell
"""

split13 = [
 '2016 – 09:46 Polizeipräsidium Aalen  Rems-Murr-Kreis: (ots)  Schorndorf: Von Fahrbahn abgekommen Ein 36-jähriger Golf-Fahrer war offenbar durch das Bedienen seines Autoradios derart abgelenkt, dass er beim Befahren der B 29 zwischen Urbach und Schorndorf vorausfahrende zu spät wahrnahm. Er musste zur Vermeidung eines Unfalls nach rechts ausweichen. Hierbei verlor er die Kontrolle über sein Auto und prallte in die Leitschutzplanken. Der Autofahrer hatte Glück und blieb bei dem Unfall am Donnerstagabend gegen 21 Uhr unverletzt. Sein Auto, an dem ein Sachschaden in Höhe von ca. 5000 Euro entstand, musste abgeschleppt werden.',
 'Schorndorf: Auffahrunfall Zwischen Schorndorf und Miedelsbach erkannte ein 38-jähriger Corsa-Fahrer auf der Umgehungsstraße zu spät das Halten vorausfahrender Autos. Er krachte auf das Fahrzeugheck einer Mercedes-Fahrerin. Beim Unfall, der sich am Donnerstag gegen 17.30 Uhr ereignete, blieben die Insassen unverletzt. Es entstand Sachschaden in Höhe von ca. 6000 Euro.',
 'Alfdorf: Auto übersehen Ein 20-jähriger VW-Lenker befuhr am Donnerstag gegen 15 Uhr die Hauptstraße und beabsichtigte nach links auf den Kundenparkplatz eines Lebensmittelgeschäft einzubiegen. Dabei übersah er einen Pkw Mitsubishi, der ihm entgegen kam. Der 50-jährige Autofahrer konnte dem abbiegenden Auto nicht mehr ausweichen. Beim Zusammenstoß entstand an den Unfallautos 10000 Euro Sachschaden.',
 'Fellbach: Auffahrunfall 2000 Euro ist die Schadensbilanz eines Auffahrunfalls, welcher sich am Donnterstag gegen 18.30 Uhr in der Schorndorf Straße ereignete. Ein 22-jähriger Toyota-Fahrer war vor einer Ampelanlage unachtsam und fuhr auf den vor ihm haltenden Golf auf.',
 'Kernen im Remstal: Unfallflucht Ein Unfallverursacher beschädigte einen in der Sudentenstraße zur Einmündung Kerlterstraße geparkten VW Polo und entfernte sich anschließend von der Unfallstelle. Der Verursacher hinterließ einen Sachschaden in Höhe von ca. 1500 Euro. An Hand der Unfallspuren ist davon auszugehen, dass ein Lkw am Unfall beteiligt war. Hinweise zum Unfallgeschehen, welches sich zwischen Mittwoch- und Donnerstagnachmittag ereignete, nimmt die Polizei in Fellbach unter Tel. 0711/57720 entgegen.',
 'Waiblingen: Unfall zwischen zwei jungen Verkehrsteilnehmern Am Donnerstagnachmittag ereignete sich gegen 16:30 Uhr ein Verkehrsunfall, bei dem zwei junge Verkehrsteilnehmer beteiligt waren. Ein 21-Jähriger befuhr mit seinem VW-Golf die Emil-Münz-Straße in Richtung Eisentalstraße. Beim Einfahren in den dortigen Einmündungsbereich übersah er eine von rechts kommende 19-jährige VW-Golf-Fahrerin. Es kam zum Zusammenstoß. Bei dem Unfall wurde niemand verletzt, es entstand allerdings ein Sachschaden von insgesamt ca. 2000 Euro.',
 'Waiblingen: Unfallverursacher ging flüchtig Gegen 24 Uhr am Donnerstag fuhr ein bislang noch unbekannter Fahrzeugführer rückwärts gegen ein Verkehrszeichen im Bereich des Taxi-Rondells beim Bahnhof und entfernte sich anschließend unerlaubt. Es gibt Hinweise auf den Fahrer, die Ermittlungen dauern derzeit noch an.',
 'Korb: Unfall beim Rückwärtsfahren Ein Schaden in bislang noch unbekannter Höhe entstand bei einem Verkehrsunfall am Donnerstagabend gegen 22.30 Uhr. Ein 23 jähriger Skoda-Fahrer hielt am rechten Fahrbahnrand der Steinstraße an. Gerade als eine 55-Jährige mit ihrem VW an dem Skoda vorbeifahren wollte setzte der 23-Jährige zurück um einem anderen Auto auszuweichen, welches zu diesem Zeitpunkt in die Straße einfuhr. Es kam zur Kollision zwischen dem Skoda und dem VW.',
 'Weinstadt: Unter Drogeneinfluss unterwegs Gegen 22:30 Uhr am Donnerstag fiel zwei Polizeibeamten ein Volvo-Fahrer auf, welcher mit überhöhter Geschwindigkeit und ohne beim Abbiegen zu blinken die Bahnhofstraße in Richtung Theodor-Heuss-Straße befuhr. Bei einer daraufhin durchgeführten Kontrolle stellten die Polizisten Anzeichen dafür fest, dass der 32-jährige Volvo-Fahrer unter Drogeneinfluss stand. Ein noch vor Ort durchgeführter Drogenschnelltest bestätigte diese Vermutung. Dem 32-Jährigen wurde die Weiterfahrt untersagt. Auch musste er zu einer richterlich angeordneten Blutentnahme mit ins Krankenhaus kommen. Bringt auch diese entsprechende Ergebnisse, muss der Mann mit führerscheinrechtlichen Konsequenzen rechnen.',
 'Waiblingen: Unfall zwischen Lkw und Pkw Ein 74 Jahre alter BMW-Fahrer wollte am Donnerstagvormittag in einen Parkplatz bei der Heinrich-Küderli-Straße einfahren. Dabei streifte er in Folge von Unachtsamkeit die gerade hochfahrende Ladebordwand eines auf dem Parkplatz befindlichen Lkw. Hierbei entstand ein Schaden von ca. 400 Euro.',
 'Waiblingen: Hilfslieferung gestohlen Im Zeitraum zwischen Dienstag und Donnerstag drang ein bislang unbekannter Dieb in einen Keller in der Salierstraße ein. Von dort entwendete er 500 Paar Schuhe in Originalkartons im Wert von ca. 2000 Euro, welche eigentlich für den Versand nach Afrika bestimmt waren. Mögliche Zeugen werden gebeten, sich unter der Tel: 07151 950 422 bei der Polizei in Waiblingen zu melden.',
 'Waiblingen: Unbekannter zerkratzt Auto Ein bislang unbekannter Täter verursachte am Donnerstagnachmittag zwischen 14:30 Uhr und 17 Uhr einen Schaden von ca. 1500 Euro an einem in der Fronackerstraße geparkten Pkw Renault, indem er die komplette rechte Fahrzeugseite zerkratzte. Hinweise nimmt die Polizei in Waiblingen unter der Tel: 07151 950 422 entgegen.',
 'Remshalden: Unfall nach Vorfahrtsverstoß Eine 28-jährige VW-Lenkerin wollte am Donnerstagvormittag gegen 10:30 Uhr von der Falkenstraße nach links in die Wilhelm-Enßle-Straße abbiegen. Hierbei übersah sie einen von rechts heranfahrenden 74 Jahre alten Audi-Fahrer. Es kam zum Zusammenstoß, bei welchem ein Schaden in noch unbekannter Höhe entstand.',
 'Waiblingen: Autoscheibe eingeschlagen Bei einem in der Badstraße abgestellten Pkw wurde durch einen bislang unbekannten Täter die hintere linke Scheibe eingeschlagen. Der Vorfall ereignete sich im Zeitraum von 22:15 Uhr am Mittwoch und 06:30 Uhr am Donnerstag. Nach derzeitigem Kenntnisstand entwendete der Dieb ein Klappmesser aus dem Ford Fiesta. Hinweise nimmt die Polizei in Waiblingen unter der Tel: 07151 950 422 entgegen.',
 'Murrhardt: Rollerfahrer gestürzt Ein 55-jähriger Rollerfahrer befuhr am Donnerstagabend gegen 22 Uhr die L 1066 zwischen Murrhardt und Fornsbach. In einer Linkskurve kam der Biker nach rechts von der Fahrbahn ab und stürzte. Der Verletzte wurde an der Unfallstelle von einem Passanten ohnmächtig angetroffen. Wie sich später in einer Klinik herausstellte, war der Zweiradfahrer erheblich alkoholisiert, weshalb ein Blutprobe erhoben wurde. Zudem stellte sich heraus, dass der Roller nicht zugelassen war und der 55-Jährige nicht in Besitz der erforderlichen Fahrerlaubnis war. Der Motorradfahrer muss nun mit einer Strafanzeige rechnen.',
 'Backnang: Von Fahrbahn abgekommen Ein 57-jähriger Opel-Fahrer befuhr am Donnerstag gegen 15.15 Uhr die B 14 in Richtung Stuttgart. Bei der Anschlussstelle Backnang Mitte überfuhr er in einer Linkskurve infolge Unachtsamkeit eine Verkehrsinsel. Anschließend kam der Unfallwagen an einer Böschung zum Stehen. Beim Unfall entstand Sachschaden in Höhe von ca. 6000 Euro. Weil am Unterboden des Unfallwagens die Ölwanne beschädigt worden war, wurde zur Säuberung und Absicherung der Unfallstelle die Straßenmeisterei hinzugezogen.',
 'Backnang: Unfallflucht In der Schöntaler Straße beschädigte ein Unfallverursacher beim Vorbeifahren den Außenspiegel eines dort geparkten VW Golfs. Hinweise zum Unfallgeschehen, welches sich am Donnerstag zwischen 10 Uhr und 12 Uhr ereignete, nimmt die Polizei in Backnang unter Tel. 07191/9090 entgegen.',
 'Schwaikheim: Vorfahrt nicht gewährt - Verkehrsunfall 2000 Euro Schaden ist die Bilanz eines Verkehrsunfalles, der sich am Donnerstag gegen 13 Uhr ereignete. Eine 43-jährige Ford-Fahrerin befuhr mit ihrem Pkw die Brunnenstraße und übersah dabei eine 37 Jährige, welchem mit ihrem VW aus der Aispachstraße in die Brunnenstraße einfahren wollte. Im Kreuzungsbereich kam es zum Zusammenstoß, verletzt wurde niemand.',
 ]


###############################################################################


text14 = """
13.10.2016 – 08:58

Polizeipräsidium Ludwigsburg

Ludwigsburg (ots)
 Renningen: Vordach einer Firma beschädigt 
Ohne sich um den angerichteten Sachschaden von etwa 4.000 Euro zu kümmern, machte sich ein bislang unbekannter Fahrzeuglenker davon, der zwischen Dienstag 18.00 Uhr und Mittwoch 06.00 Uhr eine Unfallflucht in der Benzstraße im Industriegebiet in Renningen verübte. Der Unbekannte, der vermutlich einen LKW fuhr, beschädigte wohl beim Rangieren das Vordach eines Firmengebäudes in knapp drei Metern Höhe. Sachdienliche Hinweise zum Verursacher nimmt das Polizeirevier Leonberg, Tel. 07152/605-0, entgegen. 
Rutesheim: Vorfahrtsunfall 
Eine leicht verletzte Person und zwei nicht mehr fahrbereite PKW sind die Bilanz eines Unfalls, der sich am Mittwoch kurz vor 19.30 Uhr in der Pforzheimer Straße in Rutesheim ereignete. Ein 21 Jahre alter Nissan-Fahrer wollte von der Drescherstraße nach links in die Pforzheimer Straße abbiegen und übersah hierbei vermutlich aus Unachtsamkeit den Mercedes einer 18-jährigen Fahrerin, die stadteinwärts unterwegs war. In der Folge nahm er der jungen Frau die Vorfahrt und die beiden PKW kollidierten. Die Frau erlitt leichte Verletzungen. Der entstandene Gesamtsachschaden wurde auf etwa 8.000 Euro geschätzt. 
Böblingen: Verkehrsunfallflucht mit 12.000 Euro Sachschaden 
Ein Sachschaden von etwa 12.000 Euro hinterließ eine 76-jährige Ford-Fahrerin am Mittwoch, nachdem sie gegen 11.30 Uhr im Bereich des Graf-Zeppelin-Platzes beim Rangieren gegen einen Bentley gestoßen war und sich anschließend kurzerhand aus dem Staub machte. Eine Zeugin griff jedoch sofort zum Telefon und übermittelte der Polizei das Kennzeichen des Ford und die Beschreibung der Fahrerin. Anhand dieser Angaben konnten die Beamten die 76-Jährige schließlich ermitteln. Sie muss nun mit einer Anzeige wegen Verkehrsunfallflucht rechnen. 
 
Rückfragen bitte an:

Polizeipräsidium Ludwigsburg
Telefon: 07141 18-9
E-Mail: ludwigsburg.pp@polizei.bwl.de
http://www.polizei-bw.de/
Original-Content von: Polizeipräsidium Ludwigsburg, übermittelt durch news aktuell
"""

split14 = [
 '2016 – 08:58 Polizeipräsidium Ludwigsburg Ludwigsburg (ots)  Renningen: Vordach einer Firma beschädigt Ohne sich um den angerichteten Sachschaden von etwa 4.000 Euro zu kümmern, machte sich ein bislang unbekannter Fahrzeuglenker davon, der zwischen Dienstag 18.00 Uhr und Mittwoch 06.00 Uhr eine Unfallflucht in der Benzstraße im Industriegebiet in Renningen verübte. Der Unbekannte, der vermutlich einen LKW fuhr, beschädigte wohl beim Rangieren das Vordach eines Firmengebäudes in knapp drei Metern Höhe. Sachdienliche Hinweise zum Verursacher nimmt das Polizeirevier Leonberg, Tel. 07152/605-0, entgegen.',
 'Rutesheim: Vorfahrtsunfall Eine leicht verletzte Person und zwei nicht mehr fahrbereite PKW sind die Bilanz eines Unfalls, der sich am Mittwoch kurz vor 19.30 Uhr in der Pforzheimer Straße in Rutesheim ereignete. Ein 21 Jahre alter Nissan-Fahrer wollte von der Drescherstraße nach links in die Pforzheimer Straße abbiegen und übersah hierbei vermutlich aus Unachtsamkeit den Mercedes einer 18-jährigen Fahrerin, die stadteinwärts unterwegs war. In der Folge nahm er der jungen Frau die Vorfahrt und die beiden PKW kollidierten. Die Frau erlitt leichte Verletzungen. Der entstandene Gesamtsachschaden wurde auf etwa 8.000 Euro geschätzt.',
 'Böblingen: Verkehrsunfallflucht mit 12.000 Euro Sachschaden Ein Sachschaden von etwa 12.000 Euro hinterließ eine 76-jährige Ford-Fahrerin am Mittwoch, nachdem sie gegen 11.30 Uhr im Bereich des Graf-Zeppelin-Platzes beim Rangieren gegen einen Bentley gestoßen war und sich anschließend kurzerhand aus dem Staub machte. Eine Zeugin griff jedoch sofort zum Telefon und übermittelte der Polizei das Kennzeichen des Ford und die Beschreibung der Fahrerin. Anhand dieser Angaben konnten die Beamten die 76-Jährige schließlich ermitteln. Sie muss nun mit einer Anzeige wegen Verkehrsunfallflucht rechnen.',
 ]



###############################################################################


text15 = """
22.06.2016 – 13:04

Polizeipräsidium Reutlingen

Reutlingen (ots)
 Nach dem Sieg der deutschen Nationalmannschaft gegen Nordirland strömten in Reutlingen zahlreiche Fans aus den verschiedenen Public-Viewing-Veranstaltungen in die Karlstraße, um ausgiebig zu feiern. Da sich zeitweise bis zu 500 Personen auf der Fahrbahn aufhielten und diese blockierten, musste die Karlstraße und die Eberhardstraße für etwa eine Stunde für den Verkehr komplett gesperrt werden. An einem Autokorso, der sich um die Fanmeile bildete, nahmen etwa 400 Fahrzeuge teil. Auch nach den Gruppenspielen Türkei gegen Tschechien und Kroatien gegen Spanien feierten türkische und kroatische Fans jeweils den Sieg ihrer Mannschaft in der Karlstraße, wo sich in Spitzenzeiten bis zu 1.000 Personen aufhielten. Die Fahrbahn wurde für etwa eineinhalb Stunden gesperrt. An einem Autokorso nahmen etwa 250 Fahrzeuge von Anhängern der beiden siegreichen Mannschaften teil. Eine tätliche Auseinandersetzung, die sich gegen Mitternacht nach einem Streit zwischen mehreren Feiernden auf dem Marktplatz entwickelt hatte und bei der eine Person leicht verletzt wurde, wurde von den Einsatzkräften der Polizei beendet. Die Ermittlungen zu den Umständen und den Beteiligten dauern noch an. 
Bei den Siegesfeiern wurde mehrfach Pyrotechnik gezündet, insgesamt fünf als Verursacher identifizierte Personen werden wegen Verstoßes gegen das Sprengstoffgesetz zur Anzeige gebracht. Gegen fünf weitere Beschuldigte wird wegen Beleidigung der Einsatzkräfte der Polizei ermittelt. 
Nach Ende des Deutschlandspiels kam es gegen 20.15 Uhr im Bereich des P&R-Parkplatzes in der Bahnhofstraße zu einer fremdenfeindlichen Straftat. Ein alkoholisierter und polizeilich bereits bekannter 24-Jähriger aus einer Reutlinger Kreisgemeinde und seine zwei 19 und 26 Jahre alten Begleiter beleidigten mehrfach einen 19-Jährigen aufgrund seiner dunklen Hautfarbe mit rassistischen Äußerungen. Nachdem der Geschädigte Schutz bei Bekannten suchte, kam es zum Streit zwischen den beiden Gruppierungen, bei dem der Pkw, in dem die Beschuldigten saßen, bespuckt worden sein soll. Als die drei Verdächtigen ausstiegen, soll der 24-Jährige dem 19-Jährigen einen Kopfstoß versetzt haben. Außerdem zeigte er den Hiltergruß. Gegen alle drei Beschuldigten wird wegen Beleidigung, gegen den 24-Jährigen zusätzlich wegen gefährlicher Körperverletzung und Verwendens von Kennzeichen verfassungswidriger Organisationen ermittelt. Die drei Männer wurden nach ihrer vorübergehenden Festnahme wieder entlassen und erhielten entsprechende Platzverweise, denen sie nachkamen.  Der 19-jährige Geschädigte trug keine sichtbaren Verletzungen davon, eine ärztliche Behandlung war nicht erforderlich. 
Esslingen (ES): 
Ein Autokorso mit etwa 50 Fahrzeugen auf dem Altstadtring verlief nach dem Deutschlandspiel ohne besondere Vorkommnisse. Am Korso türkischer Fans nahmen später im Bereich der Ulmer-/Neckar-/Berliner Straße 400 bis 500 Fahrzeuge teil. Teilweise musste die Polizei wegen Beschleunigungsfahrten im Korso oder gefährlichem Hinauslehnen aus den Fahrzeugen einschreiten. Durch rund 300 auf dem Bahnhofsvorplatz und vor dem alten Zollamt feiernden Fans kam es zur Blockade der Berliner Straße und zu entsprechenden Verkehrsbehinderungen. 
Nachdem die Korsofahrzeuge über Ableitungen und Sperrungen sukzessive aus der Stadt geleitet wurden lösten sich der Korso und die Jubelfeier um 23.30 Uhr nach und nach auf. 
Gegen 23.20 Uhr kam es im Korso auf der Südtangente auf Höhe der Kandlerstraße zu einem Auffahrunfall, bei dem Sachschaden in Höhe von 2.500 Euro entstand. Der 20-jährige Unfallverursacher bemerkte zu spät, dass der Korso zum Stehen kam und prallte mit seinem Mercedes ins Heck eines vor ihm stehenden BMW. Verletzt wurde niemand. 
Nürtingen (ES): 
Nach dem Sieg der türkischen und kroatischen Mannschaft kam der Verkehr in der Bahnhofstraße durch etwa 300 dort feiernde Fans zum Erliegen. Der Stadtverkehr wurde umgeleitet. Von Unbekannten wurden vereinzelt bengalische Feuer abgebrannt. Gegen 23:45 Uhr wurde die Fahrbahn der Bahnhofstraße nach Gesprächen der Einsatzkräfte mit den Fans wieder geräumt. Auch eine etwa halbstündige Anschlussfeier auf dem Schillerplatz löste sich gegen 0:15 Uhr nach Ansprache der Fans auf. 
Rottenburg (TÜ): 
Ein Autokorso mit etwa 100 Fahrzeugen und eine Fanfeier mit etwa 50 Fans am Kreisverkehr zur Tübinger Straße verliefen nach Ende des Spiels Deutschland - Nordirland ohne besondere Vorkommnisse. 
Nach den Gruppenspielen der türkischen und der kroatischen Mannschaft bildete sich ein Korso mit etwa 70 Fahrzeugen, wobei zahlreiche Fahrzeuginsassen - teilweise auch Kinder unter den Augen der Eltern - gefährliche Verhaltensweisen an den Tag legten, in Cabrios standen oder sich komplett aus den Fenstern oder Schiebedächern lehnten. Die Fahrbahn der Tübinger Straße wurde am Kreisverkehr teilweise von den etwa 100 Feiernden belagert, Fahrzeuge, die nicht am Korso teilnehmen wollten, wurden teilweise blockiert. Immer wieder musste die Polizei einschreiten. 
Einen 31-jährigen Rottenburger, der sich immer wieder bei fließendem Korsoverkehr auf die Fahrbahn begab und die einschreitenden Polizeibeamten auf das Übelste beleidigte, nahmen die Beamten vorübergehend mit auf das Polizeirevier. Der unter Alkoholeinfluss stehende Mann muss sich wegen Beleidigung verantworten. 
Gegen 23.45 Uhr hatte sich der Korso aufgelöst und der größte Teil der Personen hatte sich auf den Nachhauseweg begeben. Um aber den verbliebenen Anwesenden mit seinen vermeintlichen Fahrkünsten zu imponieren, fuhr ein 19-Jähriger mit seinem BMW aus Richtung Tübinger Straße viel zu schnell in den Kreisverkehr ein und driftete durch die Kurve. An der Ausfahrt zur Poststraße in Richtung Bahnhof wollte er mit deutlich überhöhter Geschwindigkeit ausfahren. Ein Aufprall seines linken Vorderrads am Fahrbahnteiler an der Ausfahrt verhinderte, dass sein Wagen in die noch feiernden Personen raste. Schleudernd nahm er doch noch die vorgesehene Richtung. Nach etwa 30 Metern, die der Wagen schlingernd in der Poststraße zurücklegte, kam der BMW aber nach rechts von der Fahrbahn ab und prallte gegen einen Baum. Der Fahrer wurde leicht verletzt, eine ärztliche Behandlung lehnte er ab. An seinem Fahrzeug entstand wirtschaftlicher Totalschaden in Höhe von 2.000 Euro. Der Schaden am Baum dürfte 1.500 Euro betragen. 
Ansonsten verliefen die Feiern und Korsos in anderen Kommunen im Zuständigkeitsbereich des Polizeipräsidiums Reutlingen weitgehend ohne besondere Vorkommnisse. Nur in Einzelfällen schritt die Polizei wegen des Zündens von Pyrotechnik oder gefährlicher Verhaltensweisen der Fans oder Korsoteilnehmer ein.  (ak) 
 
Rückfragen bitte an:

Andrea Kopp (ak), Tel. 07121/942-1101

Polizeipräsidium Reutlingen
Telefon: 07121 942-0
E-Mail: reutlingen.pp.pressestelle@polizei.bwl.de
http://www.polizei-bw.de/
Original-Content von: Polizeipräsidium Reutlingen, übermittelt durch news aktuell
"""


split15 = [
    '2016 – 13:04 Polizeipräsidium Reutlingen Reutlingen (ots) Nach dem Sieg der deutschen Nationalmannschaft gegen Nordirland strömten in Reutlingen zahlreiche Fans aus den verschiedenen Public-Viewing-Veranstaltungen in die Karlstraße, um ausgiebig zu feiern. Da sich zeitweise bis zu 500 Personen auf der Fahrbahn aufhielten und diese blockierten, musste die Karlstraße und die Eberhardstraße für etwa eine Stunde für den Verkehr komplett gesperrt werden. An einem Autokorso, der sich um die Fanmeile bildete, nahmen etwa 400 Fahrzeuge teil. Auch nach den Gruppenspielen Türkei gegen Tschechien und Kroatien gegen Spanien feierten türkische und kroatische Fans jeweils den Sieg ihrer Mannschaft in der Karlstraße, wo sich in Spitzenzeiten bis zu 1.000 Personen aufhielten. Die Fahrbahn wurde für etwa eineinhalb Stunden gesperrt. An einem Autokorso nahmen etwa 250 Fahrzeuge von Anhängern der beiden siegreichen Mannschaften teil. Eine tätliche Auseinandersetzung, die sich gegen Mitternacht nach einem Streit zwischen mehreren Feiernden auf dem Marktplatz entwickelt hatte und bei der eine Person leicht verletzt wurde, wurde von den Einsatzkräften der Polizei beendet. Die Ermittlungen zu den Umständen und den Beteiligten dauern noch an. Bei den Siegesfeiern wurde mehrfach Pyrotechnik gezündet, insgesamt fünf als Verursacher identifizierte Personen werden wegen Verstoßes gegen das Sprengstoffgesetz zur Anzeige gebracht. Gegen fünf weitere Beschuldigte wird wegen Beleidigung der Einsatzkräfte der Polizei ermittelt. Nach Ende des Deutschlandspiels kam es gegen 20.15 Uhr im Bereich des P&R-Parkplatzes in der Bahnhofstraße zu einer fremdenfeindlichen Straftat. Ein alkoholisierter und polizeilich bereits bekannter 24-Jähriger aus einer Reutlinger Kreisgemeinde und seine zwei 19 und 26 Jahre alten Begleiter beleidigten mehrfach einen 19-Jährigen aufgrund seiner dunklen Hautfarbe mit rassistischen Äußerungen. Nachdem der Geschädigte Schutz bei Bekannten suchte, kam es zum Streit zwischen den beiden Gruppierungen, bei dem der Pkw, in dem die Beschuldigten saßen, bespuckt worden sein soll. Als die drei Verdächtigen ausstiegen, soll der 24-Jährige dem 19-Jährigen einen Kopfstoß versetzt haben. Außerdem zeigte er den Hiltergruß. Gegen alle drei Beschuldigten wird wegen Beleidigung, gegen den 24-Jährigen zusätzlich wegen gefährlicher Körperverletzung und Verwendens von Kennzeichen verfassungswidriger Organisationen ermittelt. Die drei Männer wurden nach ihrer vorübergehenden Festnahme wieder entlassen und erhielten entsprechende Platzverweise, denen sie nachkamen. Der 19-jährige Geschädigte trug keine sichtbaren Verletzungen davon, eine ärztliche Behandlung war nicht erforderlich.',
    'Esslingen (ES): Ein Autokorso mit etwa 50 Fahrzeugen auf dem Altstadtring verlief nach dem Deutschlandspiel ohne besondere Vorkommnisse. Am Korso türkischer Fans nahmen später im Bereich der Ulmer-/Neckar-/Berliner Straße 400 bis 500 Fahrzeuge teil. Teilweise musste die Polizei wegen Beschleunigungsfahrten im Korso oder gefährlichem Hinauslehnen aus den Fahrzeugen einschreiten. Durch rund 300 auf dem Bahnhofsvorplatz und vor dem alten Zollamt feiernden Fans kam es zur Blockade der Berliner Straße und zu entsprechenden Verkehrsbehinderungen. Nachdem die Korsofahrzeuge über Ableitungen und Sperrungen sukzessive aus der Stadt geleitet wurden lösten sich der Korso und die Jubelfeier um 23.30 Uhr nach und nach auf. Gegen 23.20 Uhr kam es im Korso auf der Südtangente auf Höhe der Kandlerstraße zu einem Auffahrunfall, bei dem Sachschaden in Höhe von 2.500 Euro entstand. Der 20-jährige Unfallverursacher bemerkte zu spät, dass der Korso zum Stehen kam und prallte mit seinem Mercedes ins Heck eines vor ihm stehenden BMW. Verletzt wurde niemand.',
    'Nürtingen (ES): Nach dem Sieg der türkischen und kroatischen Mannschaft kam der Verkehr in der Bahnhofstraße durch etwa 300 dort feiernde Fans zum Erliegen. Der Stadtverkehr wurde umgeleitet. Von Unbekannten wurden vereinzelt bengalische Feuer abgebrannt. Gegen 23:45 Uhr wurde die Fahrbahn der Bahnhofstraße nach Gesprächen der Einsatzkräfte mit den Fans wieder geräumt. Auch eine etwa halbstündige Anschlussfeier auf dem Schillerplatz löste sich gegen 0:15 Uhr nach Ansprache der Fans auf.',
    'Rottenburg (TÜ): Ein Autokorso mit etwa 100 Fahrzeugen und eine Fanfeier mit etwa 50 Fans am Kreisverkehr zur Tübinger Straße verliefen nach Ende des Spiels Deutschland - Nordirland ohne besondere Vorkommnisse. Nach den Gruppenspielen der türkischen und der kroatischen Mannschaft bildete sich ein Korso mit etwa 70 Fahrzeugen, wobei zahlreiche Fahrzeuginsassen - teilweise auch Kinder unter den Augen der Eltern - gefährliche Verhaltensweisen an den Tag legten, in Cabrios standen oder sich komplett aus den Fenstern oder Schiebedächern lehnten. Die Fahrbahn der Tübinger Straße wurde am Kreisverkehr teilweise von den etwa 100 Feiernden belagert, Fahrzeuge, die nicht am Korso teilnehmen wollten, wurden teilweise blockiert. Immer wieder musste die Polizei einschreiten. Einen 31-jährigen Rottenburger, der sich immer wieder bei fließendem Korsoverkehr auf die Fahrbahn begab und die einschreitenden Polizeibeamten auf das Übelste beleidigte, nahmen die Beamten vorübergehend mit auf das Polizeirevier. Der unter Alkoholeinfluss stehende Mann muss sich wegen Beleidigung verantworten. Gegen 23.45 Uhr hatte sich der Korso aufgelöst und der größte Teil der Personen hatte sich auf den Nachhauseweg begeben. Um aber den verbliebenen Anwesenden mit seinen vermeintlichen Fahrkünsten zu imponieren, fuhr ein 19-Jähriger mit seinem BMW aus Richtung Tübinger Straße viel zu schnell in den Kreisverkehr ein und driftete durch die Kurve. An der Ausfahrt zur Poststraße in Richtung Bahnhof wollte er mit deutlich überhöhter Geschwindigkeit ausfahren. Ein Aufprall seines linken Vorderrads am Fahrbahnteiler an der Ausfahrt verhinderte, dass sein Wagen in die noch feiernden Personen raste. Schleudernd nahm er doch noch die vorgesehene Richtung. Nach etwa 30 Metern, die der Wagen schlingernd in der Poststraße zurücklegte, kam der BMW aber nach rechts von der Fahrbahn ab und prallte gegen einen Baum. Der Fahrer wurde leicht verletzt, eine ärztliche Behandlung lehnte er ab. An seinem Fahrzeug entstand wirtschaftlicher Totalschaden in Höhe von 2.000 Euro. Der Schaden am Baum dürfte 1.500 Euro betragen. Ansonsten verliefen die Feiern und Korsos in anderen Kommunen im Zuständigkeitsbereich des Polizeipräsidiums Reutlingen weitgehend ohne besondere Vorkommnisse. Nur in Einzelfällen schritt die Polizei wegen des Zündens von Pyrotechnik oder gefährlicher Verhaltensweisen der Fans oder Korsoteilnehmer ein. (ak)',
    ]



###############################################################################

text16 = """
24.06.2016 – 10:47

Polizeipräsidium Mannheim

Mannheim (ots)
 Am Donnerstagabend wurden zwischen 17 Uhr und kurz vor Mitternacht mehrere Autos in Mannheim-Wallstadt und Mannheim-Vogelstang beschädigt. 
Der oder die bislang unbekannten Täter schlugen im Mudauer Ring und in der Kormoranstraße insgesamt an fünf Autos die Scheiben ein. Aus den Fahrzeugen wurde nichts entwendet. 
Auf der Vogelstang im Eisenacher Weg wurden ebenfalls an zwei Autos die Scheiben eingeschlagen. Auch hier wurde nichts aus den Fahrzeugen gestohlen. Es entstand Sachschaden in bislang unbekannter Höhe. 
Ob ein Tatzusammenhang besteht, ist bislang Gegenstand der Ermittlungen. 
Weitere Geschädigte und Zeugen, die im genannten Zeitraum verdächtige Beobachtungen gemacht haben, werden gebeten, sich mit dem Polizeirevier Mannheim-Käfertal unter Tel.: 0621/71849-0 in Verbindung zu setzen. 
 
Rückfragen bitte an:

Polizeipräsidium Mannheim
Stabsstelle Öffentlichkeitsarbeit
Nadine Maier
Telefon: 0621 174-1107
E-Mail: mannheim.pp.stab.oe@polizei.bwl.de
http://www.polizei-bw.de/
Original-Content von: Polizeipräsidium Mannheim, übermittelt durch news aktuell
"""

split16 = ['2016 – 10:47 Polizeipräsidium Mannheim Mannheim (ots) Am Donnerstagabend wurden zwischen 17 Uhr und kurz vor Mitternacht mehrere Autos in Mannheim-Wallstadt und Mannheim-Vogelstang beschädigt. Der oder die bislang unbekannten Täter schlugen im Mudauer Ring und in der Kormoranstraße insgesamt an fünf Autos die Scheiben ein. Aus den Fahrzeugen wurde nichts entwendet. Auf der Vogelstang im Eisenacher Weg wurden ebenfalls an zwei Autos die Scheiben eingeschlagen. Auch hier wurde nichts aus den Fahrzeugen gestohlen. Es entstand Sachschaden in bislang unbekannter Höhe. Ob ein Tatzusammenhang besteht, ist bislang Gegenstand der Ermittlungen. Weitere Geschädigte und Zeugen, die im genannten Zeitraum verdächtige Beobachtungen gemacht haben, werden gebeten, sich mit dem Polizeirevier Mannheim-Käfertal unter Tel.: 0621/71849-0 in Verbindung zu setzen.']



###############################################################################

text17 = """
16.06.2016 – 12:08

Polizeipräsidium Ludwigsburg

Ludwigsburg (ots)
 Renningen, Malmsheim: Versuchter Wohnungseinbruch 
Aufmerksamen Zeugen fielen am Mittwochmorgen zwei Männer auf, die vermutlich versuchten, in ein Wohnhaus in der Heimsheimer Straße einzudringen. Einer der beiden versuchte wohl gegen 10:40 Uhr die Eingangstür aufzubrechen, indem er mit Gewalt dagegen stieß, während der andere die Umgebung beobachtete. Mutmaßlich bemerkten sie, dass sie beobachtet wurden, so dass sie das Weite suchten, ohne ins Gebäudeinnere gelangt zu sein. Sie konnten im Rahmen einer polizeilichen Fahndung nicht mehr angetroffen werden. Es handelte sich um zwei Männer, die wahrscheinlich osteuropäischer Herkunft sind und einen dunkleren, olivfarbenen Teint haben. Der eine wurde als etwa 1,75 Meter groß beschrieben. Er hat dunkle Haare, ein rundes Gesicht und war bekleidet mit einem dunklen Trainingsanzug. Sein Komplize ist mit 1,80 Meter etwas größer, hat einen dicken Bauch und ebenfalls ein rundes Gesicht. Neben einem dunklen Trainingsanzug trug er ein weißes T-Shirt. Zeugen, die Hinweise zu den beiden Männern geben können, werden gebeten, sich mit dem Polizeiposten Renningen, Tel. 07159/8045-0, in Verbindung zu setzen. 
Gerlingen / Leonberg: Streit auf offener Straße - Zeugen gesucht 
Das Polizeirevier Leonberg, Tel. 07152/605-0, sucht Zeugen, die Hinweise zu einem Vorfall geben können, der sich am Mittwoch gegen 17:00 Uhr auf der Landesstraße 1180 zwischen Gerlingen-Schillerhöhe und Leonberg ereignete. Nach Verlassen eines Tankstellengeländes fuhr eine 27-jährige Mercedes-Lenkerin im stockenden Verkehr auf die Landesstraße in Richtung Leonberg ein. Zu diesem Zeitpunkt befand sich hinter ihr eine bislang unbekannte Frau in einem dunklen PKW, die hupte, als der Verkehr vor der 27-Jährigen wieder anrollte. Kurz vor dem Kreisverkehr zur Füllerstraße geriet der Verkehr erneut ins Stocken. Plötzlich scherte die Unbekannte nach rechts aus und überholte den Mercedes im Bereich einer Bußhaltestelle. Anschließend fuhr sie wieder nach links auf die Durchgangsfahrbahn ein und hielt unvermittelt vor dem Mercedes an. Sie stieg aus und ging zu der 27-jährigen Mercedes-Lenkerin, die ihre Fensterscheibe geöffnet hatte. Die Frauen gerieten in Streit, der in eine handfeste Auseinandersetzung ausartete. Anschließend stieg die Fremde wieder in ihr Auto ein und fuhr vermutlich im Bereich des Kreisverkehrs in Richtung "Neue Ramtelstraße" davon. 
Herrenberg: Ins Schleudern geraten 
Einen Sachschaden in Höhe von 7.000 Euro forderte ein Verkehrsunfall, der sich am Mittwoch kurz nach 09:00 Uhr auf der Bundesstraße 28 ereignet hat. Vermutlich aus Unachtsamkeit verlor die 32 Jahre alte Fahrerin eines Smart die Kontrolle über den Wagen, als sie in Oberjettingen unterwegs war. Sie geriet in den Gegenverkehr und touchierte einen BMW, an dessen Steuer eine 44-Jährige saß. Glücklicherweise blieben die Fahrerinnen unverletzt. Beide Autos mussten abgeschleppt werden. 
Altdorf: Unfall verursacht und geflüchtet 
Ein bislang unbekannter Fahrzeuglenker verursachte am Mttwoch gegen 16:45 Uhr einen Verkehrsunfall, bei dem ein 16-jähriger Motorradfahrer leicht verletzt wurde und entfernte sich von der Unfallstelle. Der Biker war auf der Maurener Straße von Altdorf in Richtung Mauren unterwegs. Nach dem Wasserturm kam ihm der Pkw, der an der Engstelle nicht am rechten Fahrbahnrand fuhr, entgegen. Um einen Zusammenstoß zu vermeiden, musste der 16-Jährige nach rechts ausweichen. Er verlor die Kontrolle über das Motorrad, stürzte und wurde verletzt. Der Autofahrer indes setzte seine Fahrt unbeirrt fort. Vermutlich handelte es sich bei dem Pkw um einen grauen Kombi. Zeugen, die Hinweise zum Unfallverursacher geben können, melden sich bitte beim Polizeirevier Böblingen unter Tel. 07031/13-2500. 
Gäufelden: Holzkisten in Brand gesetzt 
Bislang unbekannte Täter trieben am Mittwo
ch gegen 21:35 Uhr in der Mötzinger Straße in Gäufelden ihr Unwesen. Im Bereich eines Sportheims wurden mehrere Holzkisten mutmaßlich in Brand gesetzt, so dass die alarmierte Freiwillige Feuerwehr Gäufelden mit drei Fahrzeugen und 13 Wehrleuten ausrückte. Vor Ort konnten sie den in Flammen stehenden Holzstapel schnell löschen. Ein aufmerksamer Zeuge konnte vor dem Brand zwei dunkel gekleidete männliche Personen erkennen, die sich im Bereich des Holzstapels aufhielten. Kurz darauf gab es einen lauten Knall und die beiden Männer liefen zu Fuß auf einem Feldweg in Richtung Bondorf davon. Kurz darauf begann das Holz zu brennen. Personen kamen glücklicher Weise nicht zu Schaden. Zeugen, die verdächtige Beobachtungen gemacht haben oder Hinweise zu den beiden Männern geben können, werden gebeten, sich mit dem Polizeirevier Herrenberg, Tel. 07032/2708-0, in Verbindung zu setzen. 
 
Rückfragen bitte an:

Polizeipräsidium Ludwigsburg
Telefon: 07141 18-9
E-Mail: ludwigsburg.pp@polizei.bwl.de
http://www.polizei-bw.de/
Original-Content von: Polizeipräsidium Ludwigsburg, übermittelt durch news aktuell
"""


split17 = [
 '2016 – 12:08 Polizeipräsidium Ludwigsburg Ludwigsburg (ots) Renningen, Malmsheim: Versuchter Wohnungseinbruch Aufmerksamen Zeugen fielen am Mittwochmorgen zwei Männer auf, die vermutlich versuchten, in ein Wohnhaus in der Heimsheimer Straße einzudringen. Einer der beiden versuchte wohl gegen 10:40 Uhr die Eingangstür aufzubrechen, indem er mit Gewalt dagegen stieß, während der andere die Umgebung beobachtete. Mutmaßlich bemerkten sie, dass sie beobachtet wurden, so dass sie das Weite suchten, ohne ins Gebäudeinnere gelangt zu sein. Sie konnten im Rahmen einer polizeilichen Fahndung nicht mehr angetroffen werden. Es handelte sich um zwei Männer, die wahrscheinlich osteuropäischer Herkunft sind und einen dunkleren, olivfarbenen Teint haben. Der eine wurde als etwa 1,75 Meter groß beschrieben. Er hat dunkle Haare, ein rundes Gesicht und war bekleidet mit einem dunklen Trainingsanzug. Sein Komplize ist mit 1,80 Meter etwas größer, hat einen dicken Bauch und ebenfalls ein rundes Gesicht. Neben einem dunklen Trainingsanzug trug er ein weißes T-Shirt. Zeugen, die Hinweise zu den beiden Männern geben können, werden gebeten, sich mit dem Polizeiposten Renningen, Tel. 07159/8045-0, in Verbindung zu setzen.',
 'Gerlingen / Leonberg: Streit auf offener Straße - Zeugen gesucht Das Polizeirevier Leonberg, Tel. 07152/605-0, sucht Zeugen, die Hinweise zu einem Vorfall geben können, der sich am Mittwoch gegen 17:00 Uhr auf der Landesstraße 1180 zwischen Gerlingen-Schillerhöhe und Leonberg ereignete. Nach Verlassen eines Tankstellengeländes fuhr eine 27-jährige Mercedes-Lenkerin im stockenden Verkehr auf die Landesstraße in Richtung Leonberg ein. Zu diesem Zeitpunkt befand sich hinter ihr eine bislang unbekannte Frau in einem dunklen PKW, die hupte, als der Verkehr vor der 27-Jährigen wieder anrollte. Kurz vor dem Kreisverkehr zur Füllerstraße geriet der Verkehr erneut ins Stocken. Plötzlich scherte die Unbekannte nach rechts aus und überholte den Mercedes im Bereich einer Bußhaltestelle. Anschließend fuhr sie wieder nach links auf die Durchgangsfahrbahn ein und hielt unvermittelt vor dem Mercedes an. Sie stieg aus und ging zu der 27-jährigen Mercedes-Lenkerin, die ihre Fensterscheibe geöffnet hatte. Die Frauen gerieten in Streit, der in eine handfeste Auseinandersetzung ausartete. Anschließend stieg die Fremde wieder in ihr Auto ein und fuhr vermutlich im Bereich des Kreisverkehrs in Richtung "Neue Ramtelstraße" davon.',
 'Herrenberg: Ins Schleudern geraten Einen Sachschaden in Höhe von 7.000 Euro forderte ein Verkehrsunfall, der sich am Mittwoch kurz nach 09:00 Uhr auf der Bundesstraße 28 ereignet hat. Vermutlich aus Unachtsamkeit verlor die 32 Jahre alte Fahrerin eines Smart die Kontrolle über den Wagen, als sie in Oberjettingen unterwegs war. Sie geriet in den Gegenverkehr und touchierte einen BMW, an dessen Steuer eine 44-Jährige saß. Glücklicherweise blieben die Fahrerinnen unverletzt. Beide Autos mussten abgeschleppt werden.',
 'Altdorf: Unfall verursacht und geflüchtet Ein bislang unbekannter Fahrzeuglenker verursachte am Mttwoch gegen 16:45 Uhr einen Verkehrsunfall, bei dem ein 16-jähriger Motorradfahrer leicht verletzt wurde und entfernte sich von der Unfallstelle. Der Biker war auf der Maurener Straße von Altdorf in Richtung Mauren unterwegs. Nach dem Wasserturm kam ihm der Pkw, der an der Engstelle nicht am rechten Fahrbahnrand fuhr, entgegen. Um einen Zusammenstoß zu vermeiden, musste der 16-Jährige nach rechts ausweichen. Er verlor die Kontrolle über das Motorrad, stürzte und wurde verletzt. Der Autofahrer indes setzte seine Fahrt unbeirrt fort. Vermutlich handelte es sich bei dem Pkw um einen grauen Kombi. Zeugen, die Hinweise zum Unfallverursacher geben können, melden sich bitte beim Polizeirevier Böblingen unter Tel. 07031/13-2500.',
 'Gäufelden: Holzkisten in Brand gesetzt Bislang unbekannte Täter trieben am Mittwo ch gegen 21:35 Uhr in der Mötzinger Straße in Gäufelden ihr Unwesen. Im Bereich eines Sportheims wurden mehrere Holzkisten mutmaßlich in Brand gesetzt, so dass die alarmierte Freiwillige Feuerwehr Gäufelden mit drei Fahrzeugen und 13 Wehrleuten ausrückte. Vor Ort konnten sie den in Flammen stehenden Holzstapel schnell löschen. Ein aufmerksamer Zeuge konnte vor dem Brand zwei dunkel gekleidete männliche Personen erkennen, die sich im Bereich des Holzstapels aufhielten. Kurz darauf gab es einen lauten Knall und die beiden Männer liefen zu Fuß auf einem Feldweg in Richtung Bondorf davon. Kurz darauf begann das Holz zu brennen. Personen kamen glücklicher Weise nicht zu Schaden. Zeugen, die verdächtige Beobachtungen gemacht haben oder Hinweise zu den beiden Männern geben können, werden gebeten, sich mit dem Polizeirevier Herrenberg, Tel. 07032/2708-0, in Verbindung zu setzen.',
 ]


###############################################################################


text18 = """
26.11.2015 – 14:30


Polizeipräsidium Ulm


Ulm (ots)

 Der Unbekannte brach zwischen 10 Uhr und 18.30 Uhr im Wohngebiet Diegelsberg in ein Einfamilienhaus ein. Am Gebäude in der Sonnenhalde kletterte der Täter auf den Balkon im ersten Obergeschoss und wuchtete dort das Schlafzimmerfenster auf. Im Haus durchwühlte der Dieb Schränke und erbeutete hochwertige Uhren und Schmuck. Um weniger aufzufallen, hatte der Einbrecher einen Bewegungsmelder der Außenbeleuchtung abgeschlagen. 

Spezialisten der Polizei sicherten die Spuren der Tat. Das Polizeirevier Uhingen (07161 / 93810) bittet um Mitteilung von verdächtigen Beobachtungen. 

Verständigen Sie im Falle von verdächtigen Wahrnehmungen umgehend die Polizei. Geräusche von splitterndem Holz, Glasbruch oder hochgeschobenen Rollläden können ebenso Anzeichen eines Einbruchs sein wie zum Beispiel fremde Personen auf dem eigenen - oder dem Nachbargrundstück. Wählen sie in solchen Fällen den Notruf 110, damit die Polizei schnell zur Stelle ist. 

Tobias Schmidberger, Pressestelle, Telefon: 0731 188 1111, E-Mail: ulm.pp.stab.oe@polizei.bwl.de 

+++2164025 

 

Rückfragen bitte an:

Polizeipräsidium Ulm
Telefon: 0731 188-0
E-Mail: ulm.pp@polizei.bwl.de
http://www.polizei-bw.de/

Original-Content von: Polizeipräsidium Ulm, übermittelt durch news aktuell
"""


split18 = ['2015 – 14:30 Polizeipräsidium Ulm Ulm (ots) Der Unbekannte brach zwischen 10 Uhr und 18.30 Uhr im Wohngebiet Diegelsberg in ein Einfamilienhaus ein. Am Gebäude in der Sonnenhalde kletterte der Täter auf den Balkon im ersten Obergeschoss und wuchtete dort das Schlafzimmerfenster auf. Im Haus durchwühlte der Dieb Schränke und erbeutete hochwertige Uhren und Schmuck. Um weniger aufzufallen, hatte der Einbrecher einen Bewegungsmelder der Außenbeleuchtung abgeschlagen. Spezialisten der Polizei sicherten die Spuren der Tat. Das Polizeirevier Uhingen (07161 / 93810) bittet um Mitteilung von verdächtigen Beobachtungen. Verständigen Sie im Falle von verdächtigen Wahrnehmungen umgehend die Polizei. Geräusche von splitterndem Holz, Glasbruch oder hochgeschobenen Rollläden können ebenso Anzeichen eines Einbruchs sein wie zum Beispiel fremde Personen auf dem eigenen - oder dem Nachbargrundstück. Wählen sie in solchen Fällen den Notruf 110, damit die Polizei schnell zur Stelle ist.']


###############################################################################

text19 = """
07.12.2015 – 14:07


Polizeipräsidium Mannheim


Mannheim (ots)

 In eine Kfz-/Zweirad-Werkstatt in der Heinrich-Lanz-Straße brachen zwischen Samstag- und Sonntagmittag, 14 Uhr bislang unbekannte Täter ein. Sie verschafften sich über eine aufgebrochene Türe Zugang, durchsuchten verschiedene Räumlichkeiten und stahlen bisherigen Erkenntnissen zufolge Bargeld, eine EC-Karte wie auch ein Laptop. Die angerichtete Sachschadenshöhe beträgt mehrere tausend Euro. Zeugen, die zur Tatzeit verdächtige Beobachtungen gemacht haben, werden gebeten, sich mit dem Polizeirevier Mannheim-Oststadt, Tel.: 0621/174-3310, in Verbindung zu setzen. 

 

Rückfragen bitte an:

Polizeipräsidium Mannheim
Öffentlichkeitsarbeit
Ulrike Mathes
Telefon: 0621 174-1106
E-Mail: mannheim.pp.stab.oe@polizei.bwl.de
http://www.polizei-bw.de/

Original-Content von: Polizeipräsidium Mannheim, übermittelt durch news aktuell
"""


split19 = ['2015 – 14:07 Polizeipräsidium Mannheim Mannheim (ots) In eine Kfz-/Zweirad-Werkstatt in der Heinrich-Lanz-Straße brachen zwischen Samstag- und Sonntagmittag, 14 Uhr bislang unbekannte Täter ein. Sie verschafften sich über eine aufgebrochene Türe Zugang, durchsuchten verschiedene Räumlichkeiten und stahlen bisherigen Erkenntnissen zufolge Bargeld, eine EC-Karte wie auch ein Laptop. Die angerichtete Sachschadenshöhe beträgt mehrere tausend Euro. Zeugen, die zur Tatzeit verdächtige Beobachtungen gemacht haben, werden gebeten, sich mit dem Polizeirevier Mannheim-Oststadt, Tel.: 0621/174-3310, in Verbindung zu setzen.']


###############################################################################


text20 = """
19.07.2015 – 18:21


Polizeipräsidium Freiburg


Freiburg (ots)

 Landkreis Breisgau-Hochschwarzwald 

Gemeinde Schluchsee 

Am Sonntagnachmittag 19.07.2015 gegen 16:35 Uhr wurde über die Integrierte Leitstelle von Feuerwehr und Rettungsdienst mitgeteilt, dass auf dem Schluchsee in Nähe der Staumauer ein Segelboot gekentert sei. Weitere Daten seien dort nicht bekannt. 

Nachdem zunächst unklar war, wie viele Personen an Bord gewesen waren, wurde gemeinsam mit den Kräften des Rettungsdienstes mit der Suche begonnen. Da der Notarzt mit dem Rettungshubschrauber unterwegs war, wurde durch diesen auch aus der Luft nach möglichen in Not geratenen Personen gesucht. 

Vor Ort konnte ein 3,5 m langes Kleinsegelboot gekentert am südlichen Seeufer, ca. 2 km von der Staumauer entfernt festgestellt werden. 

Nachdem es kurzfristig Meldungen über zwei Personen bei dem Boot gab, konnte abschließend festgestellt werden, dass ein 48 - jähriger Bootseigner eines Kleinsegelbootes (3,50 m Länge, Einmaster) - welches ohne Segelschein geführt werden darf - mit diesem Boot gekentert war. Er konnte sich selbst in Sicherheit bringen. 

Das Boot wurde auf Eigeninitiative zur Anlegestelle abgeschleppt und hierbei leicht beschädigt. Gekentert sei er nach eigenen Angaben aufgrund einer Windböe. Eine zweite Person sei definitiv nicht beteiligt gewesen. Der Bootsführer wurde nach eigenen Angaben nicht verletzt. 

FLZ/mt 

 

Rückfragen bitte an:

Polizeipräsidium Freiburg
Telefon: 0761/882-0
E-Mail: freiburg.pp@polizei.bwl.de
http://www.polizei-bw.de/

Original-Content von: Polizeipräsidium Freiburg, übermittelt durch news aktuell
"""


split20 = ['2015 – 18:21 Polizeipräsidium Freiburg Freiburg (ots) Landkreis Breisgau-Hochschwarzwald Gemeinde Schluchsee Am Sonntagnachmittag 19.07.2015 gegen 16:35 Uhr wurde über die Integrierte Leitstelle von Feuerwehr und Rettungsdienst mitgeteilt, dass auf dem Schluchsee in Nähe der Staumauer ein Segelboot gekentert sei. Weitere Daten seien dort nicht bekannt. Nachdem zunächst unklar war, wie viele Personen an Bord gewesen waren, wurde gemeinsam mit den Kräften des Rettungsdienstes mit der Suche begonnen. Da der Notarzt mit dem Rettungshubschrauber unterwegs war, wurde durch diesen auch aus der Luft nach möglichen in Not geratenen Personen gesucht. Vor Ort konnte ein 3,5 m langes Kleinsegelboot gekentert am südlichen Seeufer, ca. 2 km von der Staumauer entfernt festgestellt werden. Nachdem es kurzfristig Meldungen über zwei Personen bei dem Boot gab, konnte abschließend festgestellt werden, dass ein 48 - jähriger Bootseigner eines Kleinsegelbootes (3,50 m Länge, Einmaster) - welches ohne Segelschein geführt werden darf - mit diesem Boot gekentert war. Er konnte sich selbst in Sicherheit bringen. Das Boot wurde auf Eigeninitiative zur Anlegestelle abgeschleppt und hierbei leicht beschädigt. Gekentert sei er nach eigenen Angaben aufgrund einer Windböe. Eine zweite Person sei definitiv nicht beteiligt gewesen. Der Bootsführer wurde nach eigenen Angaben nicht verletzt. FLZ/mt']


###############################################################################

text21 = """
13.03.2015 – 11:08


Polizeipräsidium Ludwigsburg


Ludwigsburg (ots)

 Bietigheim-Bissingen: Unfall auf dem Gehweg 

Am Mittwoch ereignete sich gegen 17.45 Uhr auf dem Gehweg im Kreuzungsbereich der Stuttgarter und der Freiberger Straße ein Unfall zwischen einem 16-jährigen Radfahrer und einem 38 Jahre alten Mann, der mit einem Tretroller unterwegs war. Der 38-Jährige befuhr den Gehweg der Stuttgart Straße in Richtung Freiberger Straße, als ihm plötzlich der Radler entgegenkam. Da dieser wohl aufgrund der abschüssig verlaufenden Strecke sehr zügig fuhr, kam es zu einer Kollision der beiden. Der 38-Jährige erlitt hierdurch leichte Verletzungen. Sein Tretroller brach entzwei. Am Fahrrad entstand ein Sachschaden über etwa 250 Euro. 

Bietigheim-Bissingen: Wohnungsbrand 

Nachdem die Bewohner eines Mehrfamilienhauses in der Löchgauer Straße am Donnerstag gegen 21.30 Uhr bemerkten, dass aus einer der Wohnungen Rauch quoll, verständigten sie die Feuerwehr und verließen anschließend das Haus. Glücklicherweise befand sich, wie die Wehrleute der alarmierten Freiwillige Feuerwehr Bietigheim-Bissingen feststellte, niemand in der Wohnung. Für den entstandenen Schwelbrand, den die 21 Einsatzkräfte, die mit vier Fahrzeugen vor Ort waren, schnell löschen konnten, war mutmaßlich eine nicht vollständig abgelöschte Zigarettenkippe verantwortlich. Der betreffende Bewohner wird die nächsten Tage in seiner Zweit-Wohnung verbringen. Der entstandene Sachschaden wurde auf etwa 1.500 Euro geschätzt. 

Kornwestheim: B 27 - Drei Unfälle innerhalb weniger Minuten 

Insgesamt neun Fahrzeuge waren am Mittwoch gegen 16.40 Uhr auf der Bundesstraße 27 im Bereich der Auffahrt "Autokino" in Fahrtrichtung Stuttgart in drei Unfälle verwickelt. Zunächst wollte eine 61-jährige Fiat-Lenkerin auf die B 27 auffahren. Aufgrund des stockenden Verkehrs, der dort herrschte, musste sie ihren PKW am Ende des Beschleunigungsstreifens jedoch anhalten. Vermutlich aus Unachtsamkeit übersah dies die hinter ihr her fahrende 32 Jahre alte VW-Fahrerin und prallte mit so großer Wucht gegen den Fiat, dass dieser etwa 50 Meter nach vorne weg katapultiert wurde. Als nun ein weiterer bislang unbekannter Fahrzeuglenker, der ebenfalls auf dem Beschleunigungsstreifen unterwegs war, den Unfall vor sich bemerkte, zog er wohl ohne zu blinken nach links direkt auf den linken Fahrstreifen. Dies führte dazu, dass der dort fahrende 50 Jahre alte Daimler-Benz-Lenker stark abbremsen musste, was sein 59-jähriger Hintermann zu spät erkannte und mit seinem Renault daraufhin gegen den Daimler-Benz prallte. Der Unbekannte, der eventuell mit einem weißen LKW mit Pritsche unterwegs war, fuhr anschließend unbeirrt weiter. Eine 36-jährige BMW-Fahrerin, die ebenfalls auf der linken Spur unterwegs war, erkannte den zweiten Unfall rechtzeitig und hielt, wie auch der 44 Jahre alte VW-Fahrer und die 21-jährige Mercedes-Lenkerin hinter ihr, an. Ein 28 Jahre alter Fahrer eines weiteren BMW stellte wohl zu spät fest, dass die Fahrzeuge vor ihm angehalten hatten, fuhr auf den Mercedes auf und schob die drei PKW ineinander. Die 61-jährige Fiat-Lenkerin erlitt glücklicherweise als Einzige leichte Verletzungen. Der VW der 32 Jahre alten Frau war nicht mehr fahrbereit und musste abgeschleppt werden. Der Gesamtsachschaden beläuft sich auf etwa 15.000 Euro. Das Polizeirevier Kornwestheim, Tel. 07154/1313-0, sucht nun Zeugen, die Hinweise zu dem unbekannten Fahrzeuglenker geben können. 

Benningen an Neckar: Einbruch in Kellerräume 

Auf noch ungeklärte Weise gelangten bislang unbekannte Täter zwischen Dienstag 21.00 Uhr und Donnerstag 11.00 Uhr in das Untergeschoss eines aus drei Mehrfamilienhäusern bestehenden Komplexes in der Beihinger Straße. Anschließend machte sich die Eindringlinge an den Kellerparzellen zu schaffen und brachen insgesamt neun Räume auf. Während die Diebe in sechs der Abstellräume wohl nichts Stehlenswertes fanden, entwendeten sie aus den restlichen drei ein älteres Fernsehgerät, bedienten sich aus einer Gefriertruhe und stahlen einen Einkaufstrolley. Der Wert des Diebesguts wurde mit etwa 300 Euro angegeben. Der angerichtete Sachschaden beträgt 500 Euro. Hinweise nimmt das Polizeirevier Marbach am Neckar, Tel. 07144/900-0, entgegen. 

Oberriexingen: Feuerwehreinsatz 

Die Freiwilligen Feuerwehren Oberriexingen und Sersheim rückten am Donnerstag kurz vor 15.00 Uhr mit insgesamt 24 Einsatzkräften zu einem Brand in die Hauffstraße aus. Aus noch ungeklärter Ursache war im Bereich einer Firma gelagerter Müll, bestehend aus Eimern, Tapeten- und Teppichresten, in Brand geraten. Damit es zu keiner Beschädigung der danebenstehenden Abfalltonnen kommen konnte, wurden diese durch die Wehrleute entfernt. Anschließend konnte das Feuer zügig gelöscht werden. Es entstand kein Sachschaden. 

 

Rückfragen bitte an:

Polizeipräsidium Ludwigsburg
Telefon: 07141 18-9
E-Mail: ludwigsburg.pp@polizei.bwl.de
http://www.polizei-bw.de/

Original-Content von: Polizeipräsidium Ludwigsburg, übermittelt durch news aktuell
"""


split21 = [
 '2015 – 11:08 Polizeipräsidium Ludwigsburg Ludwigsburg (ots)  Bietigheim-Bissingen: Unfall auf dem Gehweg Am Mittwoch ereignete sich gegen 17.45 Uhr auf dem Gehweg im Kreuzungsbereich der Stuttgarter und der Freiberger Straße ein Unfall zwischen einem 16-jährigen Radfahrer und einem 38 Jahre alten Mann, der mit einem Tretroller unterwegs war. Der 38-Jährige befuhr den Gehweg der Stuttgart Straße in Richtung Freiberger Straße, als ihm plötzlich der Radler entgegenkam. Da dieser wohl aufgrund der abschüssig verlaufenden Strecke sehr zügig fuhr, kam es zu einer Kollision der beiden. Der 38-Jährige erlitt hierdurch leichte Verletzungen. Sein Tretroller brach entzwei. Am Fahrrad entstand ein Sachschaden über etwa 250 Euro.',
 'Bietigheim-Bissingen: Wohnungsbrand Nachdem die Bewohner eines Mehrfamilienhauses in der Löchgauer Straße am Donnerstag gegen 21.30 Uhr bemerkten, dass aus einer der Wohnungen Rauch quoll, verständigten sie die Feuerwehr und verließen anschließend das Haus. Glücklicherweise befand sich, wie die Wehrleute der alarmierten Freiwillige Feuerwehr Bietigheim-Bissingen feststellte, niemand in der Wohnung. Für den entstandenen Schwelbrand, den die 21 Einsatzkräfte, die mit vier Fahrzeugen vor Ort waren, schnell löschen konnten, war mutmaßlich eine nicht vollständig abgelöschte Zigarettenkippe verantwortlich. Der betreffende Bewohner wird die nächsten Tage in seiner Zweit-Wohnung verbringen. Der entstandene Sachschaden wurde auf etwa 1.500 Euro geschätzt.',
 'Kornwestheim: B 27 - Drei Unfälle innerhalb weniger Minuten Insgesamt neun Fahrzeuge waren am Mittwoch gegen 16.40 Uhr auf der Bundesstraße 27 im Bereich der Auffahrt "Autokino" in Fahrtrichtung Stuttgart in drei Unfälle verwickelt. Zunächst wollte eine 61-jährige Fiat-Lenkerin auf die B 27 auffahren. Aufgrund des stockenden Verkehrs, der dort herrschte, musste sie ihren PKW am Ende des Beschleunigungsstreifens jedoch anhalten. Vermutlich aus Unachtsamkeit übersah dies die hinter ihr her fahrende 32 Jahre alte VW-Fahrerin und prallte mit so großer Wucht gegen den Fiat, dass dieser etwa 50 Meter nach vorne weg katapultiert wurde. Als nun ein weiterer bislang unbekannter Fahrzeuglenker, der ebenfalls auf dem Beschleunigungsstreifen unterwegs war, den Unfall vor sich bemerkte, zog er wohl ohne zu blinken nach links direkt auf den linken Fahrstreifen. Dies führte dazu, dass der dort fahrende 50 Jahre alte Daimler-Benz-Lenker stark abbremsen musste, was sein 59-jähriger Hintermann zu spät erkannte und mit seinem Renault daraufhin gegen den Daimler-Benz prallte. Der Unbekannte, der eventuell mit einem weißen LKW mit Pritsche unterwegs war, fuhr anschließend unbeirrt weiter. Eine 36-jährige BMW-Fahrerin, die ebenfalls auf der linken Spur unterwegs war, erkannte den zweiten Unfall rechtzeitig und hielt, wie auch der 44 Jahre alte VW-Fahrer und die 21-jährige Mercedes-Lenkerin hinter ihr, an. Ein 28 Jahre alter Fahrer eines weiteren BMW stellte wohl zu spät fest, dass die Fahrzeuge vor ihm angehalten hatten, fuhr auf den Mercedes auf und schob die drei PKW ineinander. Die 61-jährige Fiat-Lenkerin erlitt glücklicherweise als Einzige leichte Verletzungen. Der VW der 32 Jahre alten Frau war nicht mehr fahrbereit und musste abgeschleppt werden. Der Gesamtsachschaden beläuft sich auf etwa 15.000 Euro. Das Polizeirevier Kornwestheim, Tel. 07154/1313-0, sucht nun Zeugen, die Hinweise zu dem unbekannten Fahrzeuglenker geben können.',
 'Benningen an Neckar: Einbruch in Kellerräume Auf noch ungeklärte Weise gelangten bislang unbekannte Täter zwischen Dienstag 21.00 Uhr und Donnerstag 11.00 Uhr in das Untergeschoss eines aus drei Mehrfamilienhäusern bestehenden Komplexes in der Beihinger Straße. Anschließend machte sich die Eindringlinge an den Kellerparzellen zu schaffen und brachen insgesamt neun Räume auf. Während die Diebe in sechs der Abstellräume wohl nichts Stehlenswertes fanden, entwendeten sie aus den restlichen drei ein älteres Fernsehgerät, bedienten sich aus einer Gefriertruhe und stahlen einen Einkaufstrolley. Der Wert des Diebesguts wurde mit etwa 300 Euro angegeben. Der angerichtete Sachschaden beträgt 500 Euro. Hinweise nimmt das Polizeirevier Marbach am Neckar, Tel. 07144/900-0, entgegen.',
 'Oberriexingen: Feuerwehreinsatz Die Freiwilligen Feuerwehren Oberriexingen und Sersheim rückten am Donnerstag kurz vor 15.00 Uhr mit insgesamt 24 Einsatzkräften zu einem Brand in die Hauffstraße aus. Aus noch ungeklärter Ursache war im Bereich einer Firma gelagerter Müll, bestehend aus Eimern, Tapeten- und Teppichresten, in Brand geraten. Damit es zu keiner Beschädigung der danebenstehenden Abfalltonnen kommen konnte, wurden diese durch die Wehrleute entfernt. Anschließend konnte das Feuer zügig gelöscht werden. Es entstand kein Sachschaden.']



###############################################################################


text22 = """
18.05.2015 – 15:16


Polizeipräsidium Mannheim


Wiesloch/Rhein-Neckar-Kreis (ots)

 Am Samstagmorgen, in der Zeit zwischen 2.30 Uhr und 3 Uhr brachen bislang unbekannte Täter in einen Gartencenter in der Hauptstraße ein. Im Büro öffneten sie gewaltsam mehrere Schränke und entwendeten über 3.000,- Euro Bargeld. 

Ob ein Tatzusammenhang mit Einbrüchen in eine Baumschule am 13.05.2015 in Ladenburg und am 05.05.2015 in einen Blumenhandel in Mannheim-Sandhofen, bei dem aus einem Tresor rund 10.000,- Euro entwendet worden waren, besteht, ist Gegenstand der Ermittlungen. 

Zeugen werden gebeten, sich mit dem Polizeirevier Wiesloch unter Telefon 06222/57090 in Verbindung zu setzen. 

 

Rückfragen bitte an:

Polizeipräsidium Mannheim
Heiko Kranz
Telefon: 0621 174 1104
E-Mail: mannheim.pp@polizei.bwl.de
http://www.polizei-bw.de/

Original-Content von: Polizeipräsidium Mannheim, übermittelt durch news aktuell
"""

split22 = ['2015 – 15:16 Polizeipräsidium Mannheim Wiesloch/Rhein-Neckar-Kreis (ots) Am Samstagmorgen, in der Zeit zwischen 2.30 Uhr und 3 Uhr brachen bislang unbekannte Täter in einen Gartencenter in der Hauptstraße ein. Im Büro öffneten sie gewaltsam mehrere Schränke und entwendeten über 3.000,- Euro Bargeld. Ob ein Tatzusammenhang mit Einbrüchen in eine Baumschule am 13.05.2015 in Ladenburg und am 05.05.2015 in einen Blumenhandel in Mannheim-Sandhofen, bei dem aus einem Tresor rund 10.000,- Euro entwendet worden waren, besteht, ist Gegenstand der Ermittlungen. Zeugen werden gebeten, sich mit dem Polizeirevier Wiesloch unter Telefon 06222/57090 in Verbindung zu setzen.']


###############################################################################


text23 = """
24.02.2015 – 12:01


Polizeipräsidium Ulm


Ulm (ots)

 Kurz nach 11 Uhr hatte ein Zeuge die Polizei verständigt. Er hatte beobachtet, wie in einem Kastenwagen Menschen auf der Ladefläche transportiert werden. In Sorge um die Insassen rief der Zeuge die Polizei an. Eine Polizeistreife stellte kurz darauf das Auto und zog es bei Gruibingen aus dem Verkehr. Tatsächlich waren in dem Ford Transit 18 Personen, obwohl er nur neun Sitze hat. Zehn Kinder und acht Erwachsene zwängten sich auf den Sitzen oder im Laderaum auf dem Boden. Dabei war das Auto total marode. Die Seitentür fiel beim Öffnen aus der Halterung und schloss schon gar nicht mehr richtig. Ebenso Fahrer- und Beifahrertür. Die Sitze waren teils nicht richtig mit dem Fahrzeug verschraubt, was bei einem Unfall schwerwiegende Folgen gehabt hätte. Sicherheitsgurte gab es nur ganz vorne und die waren kaputt. Ein Sachverständiger stellte kurz darauf fest, dass die hinteren Bremen nicht funktionierten, die Lenkung war defekt und auch sonst war der Wagen so marode, dass die Polizei ihn sofort aus dem Verkehr zog. Den 49-jährigen Fahrer erwartet jetzt eine Anzeige. 

Weil die Insassen jetzt zunächst festsaßen, nahm die Polizei Kontakt zur Gemeinde auf, damit die Serben nicht auf der Straße saßen. Denn nur sechs aus der Gruppe, eine Familie, konnten gleich mit Bus und Zug weiterreisen. Für die anderen verzögerte sich die Weiterreise bis zur Personalienfeststellung und den ersten Ermittlungen. Die Gemeinde stellte ihnen daraufhin für die Nacht ein Quartier zur Verfügung. Nachdem am Dienstag die ersten Maßnahmen abgeschlossen waren, konnten auch diese Zwölf, eine zehnköpfige Familie und der Fahrer mit Ehefrau, die sichere Weiterreise mit Bus und Zug antreten. 

+++++++++++++++++ 0320217 0322463 

Wolfgang Jürgens, Telefon: 0731 188 1111, E-Mail: ulm.pp.stab.oe@polizei.bwl.de 

 

Rückfragen bitte an:

Polizeipräsidium Ulm
Telefon: 0731 188-0
E-Mail: ulm.pp@polizei.bwl.de
http://www.polizei-bw.de/

Original-Content von: Polizeipräsidium Ulm, übermittelt durch news aktuell
"""


split23 = ['2015 – 12:01 Polizeipräsidium Ulm Ulm (ots) Kurz nach 11 Uhr hatte ein Zeuge die Polizei verständigt. Er hatte beobachtet, wie in einem Kastenwagen Menschen auf der Ladefläche transportiert werden. In Sorge um die Insassen rief der Zeuge die Polizei an. Eine Polizeistreife stellte kurz darauf das Auto und zog es bei Gruibingen aus dem Verkehr. Tatsächlich waren in dem Ford Transit 18 Personen, obwohl er nur neun Sitze hat. Zehn Kinder und acht Erwachsene zwängten sich auf den Sitzen oder im Laderaum auf dem Boden. Dabei war das Auto total marode. Die Seitentür fiel beim Öffnen aus der Halterung und schloss schon gar nicht mehr richtig. Ebenso Fahrer- und Beifahrertür. Die Sitze waren teils nicht richtig mit dem Fahrzeug verschraubt, was bei einem Unfall schwerwiegende Folgen gehabt hätte. Sicherheitsgurte gab es nur ganz vorne und die waren kaputt. Ein Sachverständiger stellte kurz darauf fest, dass die hinteren Bremen nicht funktionierten, die Lenkung war defekt und auch sonst war der Wagen so marode, dass die Polizei ihn sofort aus dem Verkehr zog. Den 49-jährigen Fahrer erwartet jetzt eine Anzeige. Weil die Insassen jetzt zunächst festsaßen, nahm die Polizei Kontakt zur Gemeinde auf, damit die Serben nicht auf der Straße saßen. Denn nur sechs aus der Gruppe, eine Familie, konnten gleich mit Bus und Zug weiterreisen. Für die anderen verzögerte sich die Weiterreise bis zur Personalienfeststellung und den ersten Ermittlungen. Die Gemeinde stellte ihnen daraufhin für die Nacht ein Quartier zur Verfügung. Nachdem am Dienstag die ersten Maßnahmen abgeschlossen waren, konnten auch diese Zwölf, eine zehnköpfige Familie und der Fahrer mit Ehefrau, die sichere Weiterreise mit Bus und Zug antreten.']





###############################################################################


text24 = """
"05.01.2015 – 09:56


Polizeipräsidium Heilbronn


Heilbronn (ots)

 Hohenlohekreis 

Pfedelbach: Reh contra Pkw 

Sachschaden in Höhe von rund 1.000 Euro entstand bei einem Wildunfall am Montagmorgen zwischen Gleichen und Heuberg. Gegen 3:35 Uhr rannte plötzlich ein Reh auf die Straße und wurde vom Pkw Peugeot eines 42-Jährigen erfasst. Das Tier lief nach dem Zusammenprall weiter. 

Öhringen: Zwei Auffahrunfälle hintereinander 

Sachschaden in Höhe von rund 2.500 Euro entstand am Sonntagmorgen, gegen 9:45 Uhr, bei einem Auffahrunfall in der Öhringer Hindenburgstraße. Eine 24-jährige Seat-Fahrerin konnte vermutlich infolge nicht angepasster Geschwindigkeit auf der eisglatten Fahrbahn nicht mehr rechtzeitig anhalten und rutschte mit ihrem Pkw auf einen an der Ampel vor ihr stehenden Mercedes-Sprinter. Einer nachfolgenden 35 Jahre alte Opel-Fahrerin gelang es ebenfalls nicht, rechtzeitig anzuhalten. Sie fuhr mit ihrem Pkw deshalb auf den vor ihr zum Stillstand gekommenen Seat auf. Hierdurch entstand nochmals Sachschaden von rund 1.000 Euro. Verletzt wurde keiner der Beteiligten. 

Main-Tauber-Kreis 

Creglingen: Von der Straße abgekommen und gegen Baum geprallt 

Vermutlich wegen nicht angepasster Geschwindigkeit kam eine 31-jährige Pkw-Fahrerin am Sonntagmorgen, gegen 6:30 Uhr, zwischen Tauberzell und Archshofen im Auslauf einer langgezogenen Rechtskurve auf eisglatter Fahrbahn ins Schleudern. Ihr Fahrzeug kam von der Straße ab, prallte mit der linken Fahrzeugseite gegen einen Obstbaum und kam anschließend quer zur Fahrbahn zum Stehen. Die Fahrerin wurde verletzt in ein Krankenhaus eingeliefert. An ihrem Pkw entstand wirtschaftlicher Totalschaden in Höhe von rund 1.500 Euro. 

Niederstetten: Altreifen illegal entsorgt - Zeugen gesucht 

Noch unbekannt ist, wer in den vergangenen Tagen insgesamt dreizehn Altreifen auf dem Parkplatz an der Bundesstraße 290, zwischen Herbsthausen und der Abzweigung Niederstetten illegal entsorgt hat. Sie wurden am Sonntagmittag, gegen 14:15 Uhr, dort entdeckt. Die Polizei in Bad Mergentheim, Telefon 07931 5499-0, sucht Zeugen. 

Tauberbischofsheim: Pkw beschädigt 

Sachschaden in Höhe von rund 500 Euro hinterließ ein unbekannter Vandale an einem Pkw am Samstagabend in der Tauberbischofsheimer Albert-Schweitzer-Straße. Der Suzuki war auf dem Parkplatz des Krankenhauses abgestellt. In der Zeit zwischen 17 und 18 Uhr trat er gegen das linke Teil der Heckschürze, so dass hier eine tiefe Eindellung entstand. Die Polizei Tauberbischofsheim, Telefon 09341 81-0, sucht Zeugen. 

Lauda-Königshofen: Wildschweine auf der Straße 

Für eines von drei Wildschweinen endete die Überquerung der Bundesstraße 290 am Sonntagabend zwischen Lauda und Königshofen tödlich. Es wurde gegen 23:15 Uhr vom Pkw Hyundai eines 23-Jährigen erfasst und getötet. Am Fahrzeug entstand Sachschaden in Höhe von rund 3.000 Euro. 

Wertheim: Vandalen unterwegs - Polizei sucht Zeugen 

Noch unbekannte Vandalen waren in der Zeit zwischen Samstag, 15 Uhr, und Sonntag, 13 Uhr, auf einem Parkplatz in Wertheim, Forrest-E.-Peden-Ring, unterwegs. An einem silbergrauen Fiat Punto beschädigten sie den Heckscheibenwischer. An einem schwarzen VW Tiguan schlugen sie mittels unbekanntem Gegenstand mehrfach gegen Fahrer- und Beifahrertüre. Im Bereich des rechten hinteren Fahrzeughecks hinterließen sie zudem noch einen zirka 20 cm langen Kratzer. Die Polizei in Wertheim, Telefon 09342 9189-0, sucht Zeugen der Vorfälle. 

Neckar-Odenwald-Kreis 

Mudau/Walldürn/Osterburken: Rehe verursachten Unfälle 

Am Sonntagmorgen, gegen 7:40 Uhr, rannte ein Reh zwischen Eberstadt und Bofsheim auf die Fahrbahn. Hierbei wurde es vom Pkw Hyundai eines 30-Jährigen erfasst und getötet. Der Sachschaden am Pkw liegt bei rund 2.000 Euro. Am Sonntagabend wollte ein Reh gegen 19:50 Uhr die Landesstraße 518 zwischen Hettingen und Walldürn überqueren. Ein 36-Jähriger erfasste es dabei mit seinem Pkw Peugeot. Das verletzte Tier schleppte sich noch in ein angrenzendes Gebüsch und wurde dort vom Jagdausübungsberechtigten von seinen Qualen erlöst. Auch hier liegt der Sachschaden am Pkw bei etwa 2.000 Euro. Gegen 23:30 Uhr wechselte ein Reh zwischen Schloßau und Seitzebuche über die Landesstraße 585. Eine 23-Jährige erfasste das Tier mit ihrem Pkw Opel und verletzte es tödlich. Der Schaden am Corsa beträgt rund 600 Euro. 

Mosbach: Audi frontal gegen Baum 

Sachschaden in Höhe von rund 10.000 Euro entstand bei einem Unfall am  Sonntagmorgen in Mosbach. Ein 48 Jahre alter Audi-Fahrer kam gegen 7 Uhr auf der Solbergallee, kurz nach dem Bahnübergang, aus noch unbekannter Ursache nach rechts von der Fahrbahn ab und prallte frontal gegen einen Baum. Der Mann blieb glücklicherweise unverletzt. 

Rainer Ott 

Für Rückfragen stehen wir Ihnen unter der Telefonnummer 07131 104-1010 gerne zur Verfügung. 

 

Rückfragen bitte an:

Polizeipräsidium Heilbronn
Telefon: 07131 104-9
E-Mail: heilbronn.pp@polizei.bwl.de
http://www.polizei-bw.de/

Original-Content von: Polizeipräsidium Heilbronn, übermittelt durch news aktuell"

"""


split24 = [
 '2015 – 09:56 Polizeipräsidium Heilbronn Heilbronn (ots) Hohenlohekreis  Pfedelbach: Reh contra Pkw Sachschaden in Höhe von rund 1.000 Euro entstand bei einem Wildunfall am Montagmorgen zwischen Gleichen und Heuberg. Gegen 3:35 Uhr rannte plötzlich ein Reh auf die Straße und wurde vom Pkw Peugeot eines 42-Jährigen erfasst. Das Tier lief nach dem Zusammenprall weiter.',
 'Öhringen: Zwei Auffahrunfälle hintereinander Sachschaden in Höhe von rund 2.500 Euro entstand am Sonntagmorgen, gegen 9:45 Uhr, bei einem Auffahrunfall in der Öhringer Hindenburgstraße. Eine 24-jährige Seat-Fahrerin konnte vermutlich infolge nicht angepasster Geschwindigkeit auf der eisglatten Fahrbahn nicht mehr rechtzeitig anhalten und rutschte mit ihrem Pkw auf einen an der Ampel vor ihr stehenden Mercedes-Sprinter. Einer nachfolgenden 35 Jahre alte Opel-Fahrerin gelang es ebenfalls nicht, rechtzeitig anzuhalten. Sie fuhr mit ihrem Pkw deshalb auf den vor ihr zum Stillstand gekommenen Seat auf. Hierdurch entstand nochmals Sachschaden von rund 1.000 Euro. Verletzt wurde keiner der Beteiligten.',
 'Main-Tauber-Kreis  Creglingen: Von der Straße abgekommen und gegen Baum geprallt Vermutlich wegen nicht angepasster Geschwindigkeit kam eine 31-jährige Pkw-Fahrerin am Sonntagmorgen, gegen 6:30 Uhr, zwischen Tauberzell und Archshofen im Auslauf einer langgezogenen Rechtskurve auf eisglatter Fahrbahn ins Schleudern. Ihr Fahrzeug kam von der Straße ab, prallte mit der linken Fahrzeugseite gegen einen Obstbaum und kam anschließend quer zur Fahrbahn zum Stehen. Die Fahrerin wurde verletzt in ein Krankenhaus eingeliefert. An ihrem Pkw entstand wirtschaftlicher Totalschaden in Höhe von rund 1.500 Euro.',
 'Niederstetten: Altreifen illegal entsorgt - Zeugen gesucht Noch unbekannt ist, wer in den vergangenen Tagen insgesamt dreizehn Altreifen auf dem Parkplatz an der Bundesstraße 290, zwischen Herbsthausen und der Abzweigung Niederstetten illegal entsorgt hat. Sie wurden am Sonntagmittag, gegen 14:15 Uhr, dort entdeckt. Die Polizei in Bad Mergentheim, Telefon 07931 5499-0, sucht Zeugen.',
 'Tauberbischofsheim: Pkw beschädigt Sachschaden in Höhe von rund 500 Euro hinterließ ein unbekannter Vandale an einem Pkw am Samstagabend in der Tauberbischofsheimer Albert-Schweitzer-Straße. Der Suzuki war auf dem Parkplatz des Krankenhauses abgestellt. In der Zeit zwischen 17 und 18 Uhr trat er gegen das linke Teil der Heckschürze, so dass hier eine tiefe Eindellung entstand. Die Polizei Tauberbischofsheim, Telefon 09341 81-0, sucht Zeugen.',
 'Lauda-Königshofen: Wildschweine auf der Straße Für eines von drei Wildschweinen endete die Überquerung der Bundesstraße 290 am Sonntagabend zwischen Lauda und Königshofen tödlich. Es wurde gegen 23:15 Uhr vom Pkw Hyundai eines 23-Jährigen erfasst und getötet. Am Fahrzeug entstand Sachschaden in Höhe von rund 3.000 Euro.',
 'Wertheim: Vandalen unterwegs - Polizei sucht Zeugen Noch unbekannte Vandalen waren in der Zeit zwischen Samstag, 15 Uhr, und Sonntag, 13 Uhr, auf einem Parkplatz in Wertheim, Forrest-E.-Peden-Ring, unterwegs. An einem silbergrauen Fiat Punto beschädigten sie den Heckscheibenwischer. An einem schwarzen VW Tiguan schlugen sie mittels unbekanntem Gegenstand mehrfach gegen Fahrer- und Beifahrertüre. Im Bereich des rechten hinteren Fahrzeughecks hinterließen sie zudem noch einen zirka 20 cm langen Kratzer. Die Polizei in Wertheim, Telefon 09342 9189-0, sucht Zeugen der Vorfälle.',
 'Neckar-Odenwald-Kreis  Mudau/Walldürn/Osterburken: Rehe verursachten Unfälle Am Sonntagmorgen, gegen 7:40 Uhr, rannte ein Reh zwischen Eberstadt und Bofsheim auf die Fahrbahn. Hierbei wurde es vom Pkw Hyundai eines 30-Jährigen erfasst und getötet. Der Sachschaden am Pkw liegt bei rund 2.000 Euro. Am Sonntagabend wollte ein Reh gegen 19:50 Uhr die Landesstraße 518 zwischen Hettingen und Walldürn überqueren. Ein 36-Jähriger erfasste es dabei mit seinem Pkw Peugeot. Das verletzte Tier schleppte sich noch in ein angrenzendes Gebüsch und wurde dort vom Jagdausübungsberechtigten von seinen Qualen erlöst. Auch hier liegt der Sachschaden am Pkw bei etwa 2.000 Euro. Gegen 23:30 Uhr wechselte ein Reh zwischen Schloßau und Seitzebuche über die Landesstraße 585. Eine 23-Jährige erfasste das Tier mit ihrem Pkw Opel und verletzte es tödlich. Der Schaden am Corsa beträgt rund 600 Euro.',
 'Mosbach: Audi frontal gegen Baum Sachschaden in Höhe von rund 10.000 Euro entstand bei einem Unfall am Sonntagmorgen in Mosbach. Ein 48 Jahre alter Audi-Fahrer kam gegen 7 Uhr auf der Solbergallee, kurz nach dem Bahnübergang, aus noch unbekannter Ursache nach rechts von der Fahrbahn ab und prallte frontal gegen einen Baum. Der Mann blieb glücklicherweise unverletzt.',
 ]


###############################################################################

# "Spiel" wird als Ort erkannt. Ist aber ein Ort in NRW. evtl. Ortsliste auf BW beschränken?

text99 = """
27.07.2015 – 15:57


Polizeipräsidium Aalen


Rems-Murr-Kreis: (ots)

 Schorndorf: Lkw -Kontrolle - zahlreiche Verstöße führten zu enormen Bußgeldern 

Vorausgegangen war ein lapidarer Handy-Verstoß eines 39-jährigen Lkw-Fahrers am 20. Juli auf der B 29 in Richtung Waiblingen. Beamte des Verkehrspolizeikommissariats Backnang hielten den Lkw im Bereich der Anschlussstelle Schorndorf zur Kontrolle an. Wie sich hierbei herausstellte, hatte der 39-Jährige eine falsche Fahrerkarte im Kontrollgerät gesteckt. Zudem bestand gegen ihn einen Vollstreckungshaftbefehl, den er gegen Bezahlung von über 700 Euro abwenden konnte. Die weiteren Ermittlungen der Polizei ergaben, dass die gesteckte Fahrerkarte eines mazedonischen Mannes mehrmals widerrechtlich zum Einsatz gekommen war. Auf dem Betriebsgelände des Arbeitgebers konnte zudem ein scheinbar betriebsunsicherer Lkw Iveco festgestellt werden, der kurz zuvor mit einer Lieferung aus Mazedonien eingetroffen war. Auch hier wieder dasselbe Spiel: Der verantwortliche Lkw-Fahrer hatte die Fahrerkarte des 40-jährigen Firmenchefs und Fahrzeughalter im Kontrollgerät verwendet. Der mazedonische Lkw-Fahrer musste deshalb eine Sicherheitsleistung in Höhe von ca. 550 Euro hinterlegen. Wegen des betriebsunsicheren Lkw wurde ein Sachverständiger hinzugezogen, der erhebliche Mängel am Fahrwerk sowie an der Lenk- und Bremseinrichtung feststellte. Der Lkw-Fahrer musste deshalb nochmals 525 Euro Sicherheitsleistung hinterlegen. Auch der 40-Jährige Firmenchef und Fahrzeughalter wurde für den betriebsunsicheren Zustand des Fahrzeug verantwortlich gemacht, weshalb er ein Bußgeld samt Gebühren von ca. 2200 Euro entrichten musste. 

Murrhardt: Taufstein in Kapelle beschädigt 

Unbekannte verschoben bereits letzte Woche am Mittwoch oder Donnerstag in der Waltrichskapelle im Klosterhof einen schweren Taufstein. Hierbei brachen am Stein Anbauteile ab. Der Schaden beläuft sich auf ca. 2000 Euro. Außerdem wurde in diesem Zusammenhang festgestellt, dass Bargeld aus dem Opferstock entwendet wurde. Die Polizei Murrhardt hat hierzu die Ermittlungen aufgenommen und bittet unter Tel. 07192/5313 um Zeugenhinweise. 

Fellbach: Parkunfall 

2000 Euro ist die Schadenssumme, als am Montag gegen 8 Uhr ein 34-jähriger Opel-Fahrer in der Luthersstraße beim Einparken gegen einen am Fahrbahnrand geparkten BMW stieß. 

Fellbach: Auto überschlagen 

Ein 21-jähriger Mercedes-Fahrer befuhr am Montagmorgen gegen 6.45 Uhr die B 14 in Richtung Waiblingen. Ca. 500 Meter vor dem Kappelbergtunnel kam der junge Fahrer aus bislang unbekannten Gründen nach rechts von der Fahrbahn ab. Der Wagen überschlug sich abseits der Fahrbahn und kam auf den Rädern im Grünbereich wieder zum Stehen. Der 21-Jährige wurde beim Unfall leicht verletzt und wurde deshalb in ein nahegelegenes Krankenhaus verbracht. Der total beschädigte Unfallwagen, an dem ein Sachschaden in Höhe von ca. 5000 Euro zu verzeichnen ist, musste durch ein Abschleppunternehmen geborgen werden. 

Winnenden: Radfahrerin übersehen 

Ein 35-jähriger Lkw-Fahrer fuhr am Montag gegen 10 Uhr rückwärts aus einem Parkplatz in die Bachstraße ein und übersah dabei eine 67-jährige Fahrradfahrerin, die in Richtung Waiblingen gefahren ist. Die Bikerin versuchte nach links auszuweichen, wurde jedoch noch mit dem Heck des Lkw angestoßen. Die Zweiradfahrerin stürzte und verletzte sich dabei leicht. 

Korb: Lkw aufgebrochen 

Über das vergangene Wochenende schlugen Diebe das Fenster eines Lkw-Kastenwagens ein und einwendeten aus dem Fahrzeug zwei medizinische Prüfgeräte im Wert von mehreren tausend Euro. Sollten Passanten im Bereich der Winnender Straße diesbezüglich verdächtige Beobachtungen getätigt haben, werden diese gebeten sich mit der Polizei Remshalden unter Tel. 07151/72463 in Verbindung zu setzen. 

 

Rückfragen bitte an:

Polizeipräsidium Aalen
Öffentlichkeitsarbeit
Telefon: 07361 580-105
E-Mail: aalen.pp.stab.oe@polizei.bwl.de
http://www.polizei-bw.de/

Original-Content von: Polizeipräsidium Aalen, übermittelt durch news aktuell
"""



###############################################################################


text25 = """
12.05.2015 – 14:34


Polizeipräsidium Aalen


Aalen (ots)

 Ellwangen: Brand in Erdgeschosswohnung verläuft glimpflich 

Der fahrlässige Umgang mit einer noch nicht ganz erloschenen Zigarettenkippe war am Dienstagvormittag die Ursache für einen kleineren Brand in einer Hochparterrewohnung eines Mehrfamilienhauses in der Stettiner Straße. Glücklicherweise wurden im Haus befindliche Handwerker durch einen Feuermelder auf die starke Rauchentwicklung aufmerksam und verständigten gegen 10.10 Uhr die Feuerwehr.  Lediglich ein Teil der 21im Haus gemeldeten Anwohner befanden sich zur Brandausbruchszeit in ihren Wohnungen und konnten diese rechtzeitig und unverletzt verlassen. Der 60 Jahre alte Bewohner der betroffenen Wohnung hatte diese gegen 10 Uhr verlassen und zuvor die genannte Zigarettenkippe in einem im Hausflur befindlichen Abfalleimer entsorgt. Das darin befindliche Papier und auch Abfall fingen hauptsächlich stark zu kokeln und zu rauchen an. Ein größeres Feuer entstand nicht. Die Männer der Ellwanger Wehr begaben sich mit vier Fahrzeugen und 22 Mann vor Ort. Nachdem sie die Wohnungstüre eingetreten hatten, löschten sie den Abfalleimer rasch ab, sodass zügig Entwarnung gegeben werden konnte und die Bewohner nach entsprechender Lüftung durch die Wehr in ihre Wohnungen zurückkehren konnten. In der Wohnung entstand hauptsächlich Schaden durch den Rußniederschlag, welcher auf etwa 1000 Euro beziffert wird. 

Bopfingen-Oberdorf: Rotdornbäume beschädigt 

Ein Unbekannter beschädigte vermutlich durch den Einsatz eines Pflanzenvernichtungsmittels elf Rotdornbäume, die dadurch abstarben. Die Bäume wurden im Mai 2014 im Auftrag der Stadt Bopfingen entlang des Egerweges gepflanzt. Dieser Tage musste festgestellt werden, dass die Bäume gänzlich abgestorben sind. Da einige weitere Bäume unbeschädigt blieben, geht die Polizei von einer vorsätzlichen Beschädigung aus. Der Schaden wird auf über 1300 Euro geschätzt. Der Tatzeitraum dürfte sich auf die Zeit seit Anfang Oktober bis jetzt erstrecken. Hinweise auf den Verursacher liegen bislang nicht vor. Der Polizeiposten Bopfingen bittet unter Telefon 07362/96020 um Hinweise. 

Lauchheim: Fehler beim Rangieren 

Beim Rangieren In den Kreuzäckern stieß am Dienstagvormittag, gegen 10.10 Uhr ein 28 Jahre alter Lkw-Lenker gegen einen parkenden VW. An diesem entstand Sachschaden von 1.000 Euro. 

Aalen: 20-Jähriger bei Arbeitsunfall verletzt 

Ein 20 Jahre alter Arbeiter erlitt am Dienstagvormittag einen Arbeitsunfall und musste mit Verletzungen in ein Krankenhaus eingeliefert werden. Der junge Mann war gegen 11.20 Uhr bei einer Firma in der Industriestraße zusammen mit einer weiteren Person mit Verladearbeiten von Stahlträgern beschäftigt. Dabei wurde er von einem Stahlträger beim Aufladen nach hinten gedrückt, sodass er ins Stolpern kam und rückwärts stürzte. Der Verletzte wurde durch einen Notarzt sowie Sanitätern versorgt und anschließend  mit einem Rettungswagen in ein Krankenhaus eingeliefert. 

 

Rückfragen bitte an:

Polizeipräsidium Aalen
Öffentlichkeitsarbeit
Telefon: 07361 580-106
E-Mail: aalen.pp.stab.oe@polizei.bwl.de
http://www.polizei-bw.de/

Original-Content von: Polizeipräsidium Aalen, übermittelt durch news aktuell
"""

split25 = [
 '2015 – 14:34 Polizeipräsidium Aalen Aalen (ots)  Ellwangen: Brand in Erdgeschosswohnung verläuft glimpflich Der fahrlässige Umgang mit einer noch nicht ganz erloschenen Zigarettenkippe war am Dienstagvormittag die Ursache für einen kleineren Brand in einer Hochparterrewohnung eines Mehrfamilienhauses in der Stettiner Straße. Glücklicherweise wurden im Haus befindliche Handwerker durch einen Feuermelder auf die starke Rauchentwicklung aufmerksam und verständigten gegen 10.10 Uhr die Feuerwehr. Lediglich ein Teil der 21im Haus gemeldeten Anwohner befanden sich zur Brandausbruchszeit in ihren Wohnungen und konnten diese rechtzeitig und unverletzt verlassen. Der 60 Jahre alte Bewohner der betroffenen Wohnung hatte diese gegen 10 Uhr verlassen und zuvor die genannte Zigarettenkippe in einem im Hausflur befindlichen Abfalleimer entsorgt. Das darin befindliche Papier und auch Abfall fingen hauptsächlich stark zu kokeln und zu rauchen an. Ein größeres Feuer entstand nicht. Die Männer der Ellwanger Wehr begaben sich mit vier Fahrzeugen und 22 Mann vor Ort. Nachdem sie die Wohnungstüre eingetreten hatten, löschten sie den Abfalleimer rasch ab, sodass zügig Entwarnung gegeben werden konnte und die Bewohner nach entsprechender Lüftung durch die Wehr in ihre Wohnungen zurückkehren konnten. In der Wohnung entstand hauptsächlich Schaden durch den Rußniederschlag, welcher auf etwa 1000 Euro beziffert wird.',
 'Bopfingen-Oberdorf: Rotdornbäume beschädigt Ein Unbekannter beschädigte vermutlich durch den Einsatz eines Pflanzenvernichtungsmittels elf Rotdornbäume, die dadurch abstarben. Die Bäume wurden im Mai 2014 im Auftrag der Stadt Bopfingen entlang des Egerweges gepflanzt. Dieser Tage musste festgestellt werden, dass die Bäume gänzlich abgestorben sind. Da einige weitere Bäume unbeschädigt blieben, geht die Polizei von einer vorsätzlichen Beschädigung aus. Der Schaden wird auf über 1300 Euro geschätzt. Der Tatzeitraum dürfte sich auf die Zeit seit Anfang Oktober bis jetzt erstrecken. Hinweise auf den Verursacher liegen bislang nicht vor. Der Polizeiposten Bopfingen bittet unter Telefon 07362/96020 um Hinweise.',
 'Lauchheim: Fehler beim Rangieren Beim Rangieren In den Kreuzäckern stieß am Dienstagvormittag, gegen 10.10 Uhr ein 28 Jahre alter Lkw-Lenker gegen einen parkenden VW. An diesem entstand Sachschaden von 1.000 Euro.',
 'Aalen: 20-Jähriger bei Arbeitsunfall verletzt Ein 20 Jahre alter Arbeiter erlitt am Dienstagvormittag einen Arbeitsunfall und musste mit Verletzungen in ein Krankenhaus eingeliefert werden. Der junge Mann war gegen 11.20 Uhr bei einer Firma in der Industriestraße zusammen mit einer weiteren Person mit Verladearbeiten von Stahlträgern beschäftigt. Dabei wurde er von einem Stahlträger beim Aufladen nach hinten gedrückt, sodass er ins Stolpern kam und rückwärts stürzte. Der Verletzte wurde durch einen Notarzt sowie Sanitätern versorgt und anschließend mit einem Rettungswagen in ein Krankenhaus eingeliefert.',
 ]


###############################################################################

text26 = """
13.05.2015 – 12:13


Polizeipräsidium Stuttgart


Stuttgart-Bad Cannstatt (ots)

 Unbekannte sind in der Nacht von Montag (11.05.2015) auf Dienstag (12.05.2015) in ein Geschäft an der Marktstraße eingebrochen und haben Bargeld gestohlen. Beschäftigte stellten den Einbruch am Dienstagmorgen zu Geschäftsbeginn fest und alarmierten die Polizei. Die Unbekannten hatten auf der Gebäuderückseite ein Fenster zu einem Lagerraum aufgehebelt und waren so in die Verkaufsräume eingedrungen. Dort durchsuchten sie Schränke und Schubladen und nahmen aus einer Geldkassette mehrere Hundert Euro Bargeld mit. Ob aus einem aufgebrochenen Tresor etwas mitgenommen wurde, muss noch eine Inventur des Ladenbesitzers ergeben. Zeugenhinweise nehmen die Beamtinnen und Beamten des Polizeirevier 6 Martin-Luther-Straße unter der Rufnummer 8990-3600 entgegen. 

 

Rückfragen bitte an:

Polizeipräsidium Stuttgart
Telefon: 0711 8990-1111
E-Mail: stuttgart.pressestelle@polizei.bwl.de
Außerhalb der Bürozeiten (Montag bis Freitag 06.30 Uhr bis 18.00 
Uhr):
Telefon: 0711 8990-3333
E-Mail: stuttgart.pp@polizei.bwl.de

http://www.polizei-bw.de/

Original-Content von: Polizeipräsidium Stuttgart, übermittelt durch news aktuell
"""

split26 = ['2015 – 12:13 Polizeipräsidium Stuttgart Stuttgart-Bad Cannstatt (ots) Unbekannte sind in der Nacht von Montag (11.05.2015) auf Dienstag (12.05.2015) in ein Geschäft an der Marktstraße eingebrochen und haben Bargeld gestohlen. Beschäftigte stellten den Einbruch am Dienstagmorgen zu Geschäftsbeginn fest und alarmierten die Polizei. Die Unbekannten hatten auf der Gebäuderückseite ein Fenster zu einem Lagerraum aufgehebelt und waren so in die Verkaufsräume eingedrungen. Dort durchsuchten sie Schränke und Schubladen und nahmen aus einer Geldkassette mehrere Hundert Euro Bargeld mit. Ob aus einem aufgebrochenen Tresor etwas mitgenommen wurde, muss noch eine Inventur des Ladenbesitzers ergeben. Zeugenhinweise nehmen die Beamtinnen und Beamten des Polizeirevier 6 Martin-Luther-Straße unter der Rufnummer 8990-3600 entgegen.']




###############################################################################


text27 = """
07.09.2015 – 09:12


Polizeipräsidium Aalen


Schwäbisch Hall (ots)

 Frankenhardt: Wildunfall 

Auf der Landesstraße 1064 lief am Montagmorgen ein Reh vor einen Opel. Das Tier flüchtete nach dem Anprall gegen 5.50 Uhr zwischen Gründelhardt und Spaichbühl verletzt ins benachbarte Feld. Am Opel entstand Sachschaden von etwa 500 Euro. 

Crailsheim: Vorderrad verloren, leicht verletzt 

Ein 16-jähriger Jugendlicher verletzte sich bei einem Sturz vom Fahrrad am Sonntagabend. Er war auf der Worthingtonstraße unterwegs und wollte gegen 201.10 Uhr vor dem Stadthotel auf den Gehweg fahren. Hierbei löste sich das Vorderrad, weshalb der Radfahrer zu Boden stürzte. Der Radlenker wurde hierbei  verletzt und anschließend vorsorglich ambulant im Klinikum Crailsheim behandelt. 

Crailsheim: Führerscheinneuling unter Drogen 

Bei einer Verkehrskontrolle in der Karl-Schlecht-Straße entstand bei den kontrollierenden Polizeibeamten der Eindruck, dass der 18-jährige Pkw-Fahrer unter dem Einfluss von Betäubungsmittel stehen würde. Ein an Ort und Stelle durchgeführter Test verlief positiv. Der Fahranfänger räumte daraufhin einen vor kurzem erfolgten Marihuanakonsum ein. Bei ihm wurde anschließend eine Blutentnahme durchgeführt, sein Führerschein wurde einbehalten. Beim 19-jähirgen Beifahrer fand die Polizei anschließend zwei Verbrauchseinheiten Marihuana. 

Crailsheim: Vorfahrtsunfall 

Wegen eines Vorfahrtsverstoßes ereignete sich am Sonntagmorgen ein Verkehrsunfall, bei dem an den Unfallfahrzeugen ein Schaden von rund 10000 Euro entstand. Der 50-jährige Unfallverursacher war auf der Worthingtonstraße, von der Stadtmitte kommend, in Richtung Stadtteil "Türkei" unterwegs. An der Kreuzung mit der  Goethestraße hielt er die Wartepflicht nicht ein und stieß gegen 6.30 Uhr mit einem vorfahrtsberechtigten Pkw Opel zusammen. 

Crailsheim: Illegale Sofametamorphose 

Weil sie umziehen wollte, stellte eine 31-jährige Hausbewohnerin am Freitagabend  ihr Ledersofa in den gemeinsamen Hausflur eines Mehrfamilienhauses in der Innenstadt. Als sie am Samstagnachmittag ihren Umzug fortsetzen wollte hatte ihr Ledersofa eine erstaunliche Metamorphose durchgemacht und war um Jahre gealtert. Da die 31-jährige Frau sich eine gemeinsame Zukunft mit dem verlebten Diwan nicht vorstellen konnte, rief sie die Polizei um Hilfe. Die konnte ihr rund 1000 Euro teures Sitzmöbel bei einem Nachbarn feststellen, der den Tausch auch einräumte. Der Nachbar sitzt nun nicht nur wieder unbequemer, sondern sicher auch unruhiger, denn die Polizei ermittelt nun gegen ihn wegen Diebstahls. 

Satteldorf: Sattelzug mit Auflieger beschädigt über hundert Meter Leitplanken 

Auf der BAB6 kam am Montagmorgen ein 66-jähriger Sattelzugfahrer zwischen der Landesgrenze und der Anschlussstelle Crailsheim nach links von der Fahrbahn ab. Dort beschädigte er kurz nach fünf Uhr mehr als 30 doppelte Mittelleitplanken. Dabei entstand an Fahrzeug und Verkehrseinrichtung ein Schaden, der auf rund 20000 Euro geschätzt wurde. 

Mainhardt: Wildunfall 

Mit einem Dachs pralle am Sonntagabend ein 51-jähriger Audi-Fahrer zusammen. Er war auf der Bundesstraße 39, zwischen Hohenstraßen und Ammertsweiler unterwegs, als er gegen 23.30 Uhr auf das Tier traf. Der Dachs flüchtete nach dem Unfall, am Pkw war Schaden von ca. 1000 Euro entstanden. 

Gaildorf: Motorrad-Fahrer leicht verletzt 

Beim Ausfahren am Sonntagvormittag aus dem verkehrsberuhigten Bereich der Grabenstraße in die weiterführende Grabenstraße missachtete ein 63-jähriger Seat--Fahrer gegen 11 Uhr den Vorrang eines 18-jährigen Motorrad-Fahrers. Der Zweirad-Fahrer kam aus Richtung Schlossstraße und wurde durch den Zusammenstoß leicht verletzt. Der Sachschaden wurde auf ca. 2500 Euro geschätzt. 

 

Rückfragen bitte an:

Polizeipräsidium Aalen
Öffentlichkeitsarbeit
Telefon: 07361 580-107
E-Mail: aalen.pp.stab.oe@polizei.bwl.de
http://www.polizei-bw.de/

Original-Content von: Polizeipräsidium Aalen, übermittelt durch news aktuell
"""




split27 = [
 '2015 – 09:12 Polizeipräsidium Aalen Schwäbisch Hall (ots)  Frankenhardt: Wildunfall Auf der Landesstraße 1064 lief am Montagmorgen ein Reh vor einen Opel. Das Tier flüchtete nach dem Anprall gegen 5.50 Uhr zwischen Gründelhardt und Spaichbühl verletzt ins benachbarte Feld. Am Opel entstand Sachschaden von etwa 500 Euro.',
 'Crailsheim: Vorderrad verloren, leicht verletzt Ein 16-jähriger Jugendlicher verletzte sich bei einem Sturz vom Fahrrad am Sonntagabend. Er war auf der Worthingtonstraße unterwegs und wollte gegen 201.10 Uhr vor dem Stadthotel auf den Gehweg fahren. Hierbei löste sich das Vorderrad, weshalb der Radfahrer zu Boden stürzte. Der Radlenker wurde hierbei verletzt und anschließend vorsorglich ambulant im Klinikum Crailsheim behandelt.',
 'Crailsheim: Führerscheinneuling unter Drogen Bei einer Verkehrskontrolle in der Karl-Schlecht-Straße entstand bei den kontrollierenden Polizeibeamten der Eindruck, dass der 18-jährige Pkw-Fahrer unter dem Einfluss von Betäubungsmittel stehen würde. Ein an Ort und Stelle durchgeführter Test verlief positiv. Der Fahranfänger räumte daraufhin einen vor kurzem erfolgten Marihuanakonsum ein. Bei ihm wurde anschließend eine Blutentnahme durchgeführt, sein Führerschein wurde einbehalten. Beim 19-jähirgen Beifahrer fand die Polizei anschließend zwei Verbrauchseinheiten Marihuana.',
 'Crailsheim: Vorfahrtsunfall Wegen eines Vorfahrtsverstoßes ereignete sich am Sonntagmorgen ein Verkehrsunfall, bei dem an den Unfallfahrzeugen ein Schaden von rund 10000 Euro entstand. Der 50-jährige Unfallverursacher war auf der Worthingtonstraße, von der Stadtmitte kommend, in Richtung Stadtteil "Türkei" unterwegs. An der Kreuzung mit der Goethestraße hielt er die Wartepflicht nicht ein und stieß gegen 6.30 Uhr mit einem vorfahrtsberechtigten Pkw Opel zusammen.',
 'Crailsheim: Illegale Sofametamorphose Weil sie umziehen wollte, stellte eine 31-jährige Hausbewohnerin am Freitagabend ihr Ledersofa in den gemeinsamen Hausflur eines Mehrfamilienhauses in der Innenstadt. Als sie am Samstagnachmittag ihren Umzug fortsetzen wollte hatte ihr Ledersofa eine erstaunliche Metamorphose durchgemacht und war um Jahre gealtert. Da die 31-jährige Frau sich eine gemeinsame Zukunft mit dem verlebten Diwan nicht vorstellen konnte, rief sie die Polizei um Hilfe. Die konnte ihr rund 1000 Euro teures Sitzmöbel bei einem Nachbarn feststellen, der den Tausch auch einräumte. Der Nachbar sitzt nun nicht nur wieder unbequemer, sondern sicher auch unruhiger, denn die Polizei ermittelt nun gegen ihn wegen Diebstahls.',
 'Satteldorf: Sattelzug mit Auflieger beschädigt über hundert Meter Leitplanken Auf der BAB6 kam am Montagmorgen ein 66-jähriger Sattelzugfahrer zwischen der Landesgrenze und der Anschlussstelle Crailsheim nach links von der Fahrbahn ab. Dort beschädigte er kurz nach fünf Uhr mehr als 30 doppelte Mittelleitplanken. Dabei entstand an Fahrzeug und Verkehrseinrichtung ein Schaden, der auf rund 20000 Euro geschätzt wurde.',
 'Mainhardt: Wildunfall Mit einem Dachs pralle am Sonntagabend ein 51-jähriger Audi-Fahrer zusammen. Er war auf der Bundesstraße 39, zwischen Hohenstraßen und Ammertsweiler unterwegs, als er gegen 23.30 Uhr auf das Tier traf. Der Dachs flüchtete nach dem Unfall, am Pkw war Schaden von ca. 1000 Euro entstanden.',
 'Gaildorf: Motorrad-Fahrer leicht verletzt Beim Ausfahren am Sonntagvormittag aus dem verkehrsberuhigten Bereich der Grabenstraße in die weiterführende Grabenstraße missachtete ein 63-jähriger Seat--Fahrer gegen 11 Uhr den Vorrang eines 18-jährigen Motorrad-Fahrers. Der Zweirad-Fahrer kam aus Richtung Schlossstraße und wurde durch den Zusammenstoß leicht verletzt. Der Sachschaden wurde auf ca. 2500 Euro geschätzt.',
 ]

###############################################################################

text28 = """
20.03.2015 – 10:43


Polizeipräsidium Heilbronn


Heilbronn (ots)

 Neckar-Odenwald-Kreis 

Buchen: Verkehrsunfall 

Auf rund 1.500 Euro beläuft sich der Sachschaden, der am Donnerstag, gegen 10.00 Uhr, bei einem Verkehrsunfall im Bereich Buchen entstand. Ein 21-Jähriger hatte mit seinem 3,5-Tonner-Lkw die Bundesstraße 27 von Waldhausen kommend in Richtung Buchen befahren. Vermutlich wegen Unachtsamkeit geriet er zunächst nach rechts auf den Grünstreifen, beschädigte einen Leitpfosten, schleuderte danach quer über die Fahrbahn, prallte mit der rechten Seite gegen die Böschung und kam schließlich nach weiteren 50 Metern Fahrt im Graben zum Liegen. Bei der Unfallaufnahme stellten die Beamten fest, dass das Profil der beiden Vorderreifen des 3,5-Tonners vollständig abgefahren war. Verletzt wurde niemand. 

Mosbach: Verfolgungsfahrt 

Bei einem Einsatz in Mosbach am Donnerstag, kurz vor 19.00 Uhr, wurde ein Beamter des Mosbacher Polizeireviers verletzt. Zunächst stellte eine Streife fest, dass in der Mosbacher Kistnerstraße ein Rollerfahrer samt Sozius unterwegs war, ohne einen Schutzhelm zu tragen. Auch war an dem Zweirad kein Versicherungskennzeichen angebracht. Als die beiden die Polizeistreife als solche erkannten, gab der 28-Jährige Gas und bog in die Odenwaldstraße ab. Anhalteaufforderungen, auch unter zu Hilfenahme des Blaulichtes und des Martinshorns, wurden ignoriert. Nach mehreren Wendemanövern auf der Fahrbahn bogen die Flüchtenden bei rot zeigender Ampel  in die Eisenbahnstraße ab. Die Verfolgungsfahrt ging weiter über die Bleichstraße/Am Henschelberg in Richtung Nüstenbach. Mehrfach mussten andere Autofahrer abbremsen und ausweichen. Weitere Anhalteaufforderungen schlugen fehl. Nach der Fahrt durch Nüstenbach ging es über einen Verbindungsweg nach Lohrbach und durch ein Waldgebiet in Richtung Waldstadt. Eine weitere Streifenwagenbesatzung stellte ihren Streifenwagen quer und blockierte den Waldweg, während eine Polizeibeamtin auf dem Weg deutliche Haltezeichen gab. Der Rollerfahrer fuhr jedoch unvermittelt weiter, direkt auf die Beamtin zu, sodass diese nur durch einen Sprung zur Seite einen Zusammenprall verhindern konnte. In diesem Moment gelang es, den kurz zum Stehen gekommenen Rollerfahrer zu ergreifen und von seinem Fahrzeug zu ziehen. Sowohl Fahrer als auch Beifahrer leisteten gegen die Festnahme heftigen Widerstand. Ein Beamter erlitt hierbei Verletzungen und wird die nächste Zeit nicht dienstfähig sein. Dem 28-Jährigen und seinem 21-jährigen Sozius wurde eine Blutprobe entnommen. Die Männer standen vermutlich unter Alkohol- und Drogeneinfluss. Der Roller wurde sichergestellt. Nach Abschluss der polizeilichen Maßnahmen wurden die Männer auf freien Fuß gesetzt. Sie sehen jetzt Anzeigen wegen Widerstand gegen Polizeibeamte, Gefährlichen Eingriff in den Straßenverkehr, Fahren ohne Fahrerlaubnis, Körperverletzung und anderen Delikten entgegen. Da es während ihrer Fahrt mit großer Wahrscheinlichkeit zu Gefahrensituationen gegenüber anderer Verkehrsteilnehmer kam, werden Zeugen bzw. Personen, die gefährdet wurden gebeten, sich unter der Tel.Nr.: 06261 809-0 mit der Polizei Mosbach in Verbindung zu setzen. 

Elztal-Dallau: Verkehrsunfall 

Auf rund 19.000 Euro dürfte sich der Sachschaden belaufen, welcher am Donnerstag, gegen 12.00 Uhr, bei einem Verkehrsunfall in Elztal-Dallau entstand. Eine 43-Jährige wollte mit seinem Pkw Nissan auf der Kirchstraße vom Fahrbahnrand aus losfahren, während gleichzeitig ein 69-Jähriger mit seinem Fiat auf der Straße in Richtung Ortsmitte fuhr. In der Folge prallte der Fiat-Panda gegen die linke Seite des Nissans, wurde dadurch um 90 Grad gedreht und überschlug sich ein Mal. Das Auto der 43-Jährigen wurde durch den Aufprall nach rechts abgewiesen und kollidierte mit einem geparkten Fiat. Der 69-Jährige wurde bei dem Unfall leicht verletzt und vorsorglich in ein Krankenhaus gebracht. 

Mosbach: Fahren ohne Fahrerlaubnis 

Es fällt ein Stück weit schwer, das von ergreifender Schlichtheit geprägte Verhalten eines 18-Jährigen zu kommentieren, der am Donnerstag, gegen 13.25 Uhr in Mosbach von einer Polizeistreife kontrolliert wurde. Der junge Autofahrer erklärte bei seiner Kontrolle, dass er keinen Führerschein habe, da er diesen "vorhin" bei der Staatsanwaltschaft Mosbach abgegeben hätte. Natürlich bedurfte diese Aussage einer weiteren Abklärung und der 18-Jährige musste die Beamten noch dorthin begleiten. Hier wurde tatsächlich offenkundig, dass gegen den Fahranfänger bereits seit Mitte Februar ein rechtskräftiges Fahrverbot von einem Monat vorlag. Da er sich direkt nach Abgabe seines Führerscheines trotzdem in sein Auto setzte und kurz danach erwischt wurde, zieht dies neben einer Anzeige wegen Fahrens ohne Fahrerlaubnis auch einen Bericht an die Führerscheinstelle nach sich. 

Künzelsau: Nachtrag zu Container-Brand 

Wie bereits berichtet, brannte am Mittwoch, gegen 19.45 Uhr, ein im Künzelsauer Hermersberger Weg aufgestellter Altkleidercontainer. Es besteht die Möglichkeit, dass das Feuer absichtlich gelegt wurde. Im Zuge der Ermittlungen richtet sich der Fokus auf eine Person, welche sich  zwischen 19.15 Uhr und 19.50 Uhr im Bereich der Schule, also in der Nähe des Containers aufgehalten hatte. Diese war mit einer rotfarbenen Jacke bekleidet. Auffällig war der schwankende Gang des Unbekannten. Ob dies einem etwaigen Alkoholkonsum geschuldet war, lässt sich nicht sagen. Während der betreffenden Tatzeit müssten sich mehrere Fußgänger im näheren Bereich aufgehalten haben. Hinweise zur Identität des Unbekannten nimmt die Polizei Künzelsau unter der Tel.Nr.: 07940 940-0 entgegen. 

Für Rückfragen stehen wir Ihnen unter der Telefonnummer 07131 104-1010 gerne zur Verfügung. 

 

Rückfragen bitte an:

Polizeipräsidium Heilbronn
Telefon: 07131 104-9
E-Mail: heilbronn.pp@polizei.bwl.de
http://www.polizei-bw.de/

Original-Content von: Polizeipräsidium Heilbronn, übermittelt durch news aktuell
"""

split28 = [
 '2015 – 10:43 Polizeipräsidium Heilbronn Heilbronn (ots) Neckar-Odenwald-Kreis  Buchen: Verkehrsunfall Auf rund 1.500 Euro beläuft sich der Sachschaden, der am Donnerstag, gegen 10.00 Uhr, bei einem Verkehrsunfall im Bereich Buchen entstand. Ein 21-Jähriger hatte mit seinem 3,5-Tonner-Lkw die Bundesstraße 27 von Waldhausen kommend in Richtung Buchen befahren. Vermutlich wegen Unachtsamkeit geriet er zunächst nach rechts auf den Grünstreifen, beschädigte einen Leitpfosten, schleuderte danach quer über die Fahrbahn, prallte mit der rechten Seite gegen die Böschung und kam schließlich nach weiteren 50 Metern Fahrt im Graben zum Liegen. Bei der Unfallaufnahme stellten die Beamten fest, dass das Profil der beiden Vorderreifen des 3,5-Tonners vollständig abgefahren war. Verletzt wurde niemand.',
 'Mosbach: Verfolgungsfahrt Bei einem Einsatz in Mosbach am Donnerstag, kurz vor 19.00 Uhr, wurde ein Beamter des Mosbacher Polizeireviers verletzt. Zunächst stellte eine Streife fest, dass in der Mosbacher Kistnerstraße ein Rollerfahrer samt Sozius unterwegs war, ohne einen Schutzhelm zu tragen. Auch war an dem Zweirad kein Versicherungskennzeichen angebracht. Als die beiden die Polizeistreife als solche erkannten, gab der 28-Jährige Gas und bog in die Odenwaldstraße ab. Anhalteaufforderungen, auch unter zu Hilfenahme des Blaulichtes und des Martinshorns, wurden ignoriert. Nach mehreren Wendemanövern auf der Fahrbahn bogen die Flüchtenden bei rot zeigender Ampel in die Eisenbahnstraße ab. Die Verfolgungsfahrt ging weiter über die Bleichstraße/Am Henschelberg in Richtung Nüstenbach. Mehrfach mussten andere Autofahrer abbremsen und ausweichen. Weitere Anhalteaufforderungen schlugen fehl. Nach der Fahrt durch Nüstenbach ging es über einen Verbindungsweg nach Lohrbach und durch ein Waldgebiet in Richtung Waldstadt. Eine weitere Streifenwagenbesatzung stellte ihren Streifenwagen quer und blockierte den Waldweg, während eine Polizeibeamtin auf dem Weg deutliche Haltezeichen gab. Der Rollerfahrer fuhr jedoch unvermittelt weiter, direkt auf die Beamtin zu, sodass diese nur durch einen Sprung zur Seite einen Zusammenprall verhindern konnte. In diesem Moment gelang es, den kurz zum Stehen gekommenen Rollerfahrer zu ergreifen und von seinem Fahrzeug zu ziehen. Sowohl Fahrer als auch Beifahrer leisteten gegen die Festnahme heftigen Widerstand. Ein Beamter erlitt hierbei Verletzungen und wird die nächste Zeit nicht dienstfähig sein. Dem 28-Jährigen und seinem 21-jährigen Sozius wurde eine Blutprobe entnommen. Die Männer standen vermutlich unter Alkohol- und Drogeneinfluss. Der Roller wurde sichergestellt. Nach Abschluss der polizeilichen Maßnahmen wurden die Männer auf freien Fuß gesetzt. Sie sehen jetzt Anzeigen wegen Widerstand gegen Polizeibeamte, Gefährlichen Eingriff in den Straßenverkehr, Fahren ohne Fahrerlaubnis, Körperverletzung und anderen Delikten entgegen. Da es während ihrer Fahrt mit großer Wahrscheinlichkeit zu Gefahrensituationen gegenüber anderer Verkehrsteilnehmer kam, werden Zeugen bzw. Personen, die gefährdet wurden gebeten, sich unter der Tel.Nr.: 06261 809-0 mit der Polizei Mosbach in Verbindung zu setzen.',
 'Elztal-Dallau: Verkehrsunfall Auf rund 19.000 Euro dürfte sich der Sachschaden belaufen, welcher am Donnerstag, gegen 12.00 Uhr, bei einem Verkehrsunfall in Elztal-Dallau entstand. Eine 43-Jährige wollte mit seinem Pkw Nissan auf der Kirchstraße vom Fahrbahnrand aus losfahren, während gleichzeitig ein 69-Jähriger mit seinem Fiat auf der Straße in Richtung Ortsmitte fuhr. In der Folge prallte der Fiat-Panda gegen die linke Seite des Nissans, wurde dadurch um 90 Grad gedreht und überschlug sich ein Mal. Das Auto der 43-Jährigen wurde durch den Aufprall nach rechts abgewiesen und kollidierte mit einem geparkten Fiat. Der 69-Jährige wurde bei dem Unfall leicht verletzt und vorsorglich in ein Krankenhaus gebracht.',
 'Mosbach: Fahren ohne Fahrerlaubnis Es fällt ein Stück weit schwer, das von ergreifender Schlichtheit geprägte Verhalten eines 18-Jährigen zu kommentieren, der am Donnerstag, gegen 13.25 Uhr in Mosbach von einer Polizeistreife kontrolliert wurde. Der junge Autofahrer erklärte bei seiner Kontrolle, dass er keinen Führerschein habe, da er diesen "vorhin" bei der Staatsanwaltschaft Mosbach abgegeben hätte. Natürlich bedurfte diese Aussage einer weiteren Abklärung und der 18-Jährige musste die Beamten noch dorthin begleiten. Hier wurde tatsächlich offenkundig, dass gegen den Fahranfänger bereits seit Mitte Februar ein rechtskräftiges Fahrverbot von einem Monat vorlag. Da er sich direkt nach Abgabe seines Führerscheines trotzdem in sein Auto setzte und kurz danach erwischt wurde, zieht dies neben einer Anzeige wegen Fahrens ohne Fahrerlaubnis auch einen Bericht an die Führerscheinstelle nach sich.',
 'Künzelsau: Nachtrag zu Container-Brand Wie bereits berichtet, brannte am Mittwoch, gegen 19.45 Uhr, ein im Künzelsauer Hermersberger Weg aufgestellter Altkleidercontainer. Es besteht die Möglichkeit, dass das Feuer absichtlich gelegt wurde. Im Zuge der Ermittlungen richtet sich der Fokus auf eine Person, welche sich zwischen 19.15 Uhr und 19.50 Uhr im Bereich der Schule, also in der Nähe des Containers aufgehalten hatte. Diese war mit einer rotfarbenen Jacke bekleidet. Auffällig war der schwankende Gang des Unbekannten. Ob dies einem etwaigen Alkoholkonsum geschuldet war, lässt sich nicht sagen. Während der betreffenden Tatzeit müssten sich mehrere Fußgänger im näheren Bereich aufgehalten haben. Hinweise zur Identität des Unbekannten nimmt die Polizei Künzelsau unter der Tel.Nr.: 07940 940-0 entgegen. Für Rückfragen stehen wir Ihnen unter der Telefonnummer 07131 104-1010 gerne zur Verfügung.',
 ]


###############################################################################


text29 = """
02.11.2015 – 10:37


Polizeipräsidium Freiburg


Freiburg (ots)

 Waldshut-Tiengen/Tiengen: Autofahrer unter Drogeneinfluss 

Die Polizei kontrollierte am Samstagnachmittag in der Wutachstraße einen VW. Bei dem 22 Jahre alten Fahrer wurde Symptome für eine aktuelle Drogenbeeinflussung festgestellt, ein Drogenvortest zeigte Spuren des Cannabiswirkstoffs THC im Urin des Mannes an. Er musste sein Fahrzeug stehen lassen, eine Blutuntersuchung wurde veranlasst. 

Waldshut-Tiengen/Waldshut: Unfallbeteiligter fährt weiter 

Zu einem Verkehrsunfall mit Sachschaden kam es am Samstagabend gegen 17.45 Uhr in der Robert-Gerwig-Straße. Ein 29 Jahre alter Mann wollte mit seinem Honda Civic vom Parkplatz des Burger-King auf die Straße einfahren und stieß hierbei mit einem dort in Richtung Kreisverkehr fahrenden Pkw zusammen. An beiden Fahrzeugen entstand Sachschaden, am Honda wurde die Motorhaube beschädigt, am anderen Fahrzeug sind Schäden an der rechten Fahrzeugseite entstanden. Der Fahrer des zweiten Fahrzeugs hielt kurz an, fuhr dann aber in Richtung Kreisverkehr davon. Bei dem flüchtigen Fahrzeug handelt es sich um einen dunkelblauen Kleinwagen. Die Polizei bittet Zeugen, die den Unfall gesehen haben oder die Hinweise zu dem anderen Fahrzeug geben können, sich beim Polizeirevier Waldshut (Tel. 07751 83160) zu melden. 

 

Rückfragen bitte an:

Polizeipräsidium Freiburg
Stabsstelle Öffentlichkeitsarbeit
Paul Wißler
Telefon: 07741 8316-201
E-Mail: freiburg.pp@polizei.bwl.de
http://www.polizei-bw.de/

Original-Content von: Polizeipräsidium Freiburg, übermittelt durch news aktuell
"""

split29 = [
 '2015 – 10:37 Polizeipräsidium Freiburg Freiburg (ots)  Waldshut-Tiengen/Tiengen: Autofahrer unter Drogeneinfluss Die Polizei kontrollierte am Samstagnachmittag in der Wutachstraße einen VW. Bei dem 22 Jahre alten Fahrer wurde Symptome für eine aktuelle Drogenbeeinflussung festgestellt, ein Drogenvortest zeigte Spuren des Cannabiswirkstoffs THC im Urin des Mannes an. Er musste sein Fahrzeug stehen lassen, eine Blutuntersuchung wurde veranlasst.',
 'Waldshut-Tiengen/Waldshut: Unfallbeteiligter fährt weiter Zu einem Verkehrsunfall mit Sachschaden kam es am Samstagabend gegen 17.45 Uhr in der Robert-Gerwig-Straße. Ein 29 Jahre alter Mann wollte mit seinem Honda Civic vom Parkplatz des Burger-King auf die Straße einfahren und stieß hierbei mit einem dort in Richtung Kreisverkehr fahrenden Pkw zusammen. An beiden Fahrzeugen entstand Sachschaden, am Honda wurde die Motorhaube beschädigt, am anderen Fahrzeug sind Schäden an der rechten Fahrzeugseite entstanden. Der Fahrer des zweiten Fahrzeugs hielt kurz an, fuhr dann aber in Richtung Kreisverkehr davon. Bei dem flüchtigen Fahrzeug handelt es sich um einen dunkelblauen Kleinwagen. Die Polizei bittet Zeugen, die den Unfall gesehen haben oder die Hinweise zu dem anderen Fahrzeug geben können, sich beim Polizeirevier Waldshut (Tel. 07751 83160) zu melden.',
 ]


###############################################################################

text30 = """
04.07.2015 – 10:00


Polizeipräsidium Ludwigsburg


Ludwigsburg (ots)

 Remseck am Neckar: Zusammenstoß mit Stadtbahn 

Am Freitagnachmittag um kurz vor 15.00 Uhr ereignete sich auf der Kreuzung L1100 / Am Holzbach in Remseck am Neckar ein Verkehrsunfall zwischen einem LKW und einer Stadtbahn der Linie U14. Als der 57-jährige LKW Fahrer von der Landstraße nach links in die Straße Am Holzbach einbiegen wollte, übersah der die von hinten kommende, vorfahrtberechtigte Stadtbahn. Der Stadtbahnführer führte vergeblich eine Vollbremsung durch und stieß schließlich mit dem Anhänger des LKW zusammen. Verletzt wurde dabei niemand. Der Sachschaden beträgt mindestens 13.000 Euro. Der dortige Schienenverkehr musste für ca. 45 Minuten unterbrochen werden. 

Möglingen: LKW gerät beim Fahren in Brand 

Am Freitagnachmittag um kurz nach 17.00 Uhr befuhr ein 42-jähriger LKW-Fahrer die Straße im Bornrain in Möglingen. Aus unbekannter Ursache geriet während der Fahrt die Ladung, bestehend aus Folien, in Brand. Der Fahrer konnte anhalten, ehe der Innenraum seines LKW ausbrannte. Verletzt wurde niemand. Der Sachschaden beträgt ungefähr 8000 Euro. Die Feuerwehr war mit drei Fahrzeugen und 20 Einsatzkräften vor Ort. 

Kornwestheim: Flächenbrand von Acker 

Aus bislang unbekannter Ursache geriet am Freitagnachmittag gegen 18.00 Uhr ein frisch gemähter Acker im Bereich zwischen Kornwestheim und Ludwigsburg in Brand. Der Brand erstreckte sich über eine Fläche von 400 m². Die Höhe des entstandenen Schadens kann nicht beziffert werden, liegt aber bei höchstens 200 Euro. Die Feuerwehr war mit drei Fahrzeugen und 27 Feuerwehrleuten im Einsatz. 

 

Rückfragen bitte an:

Polizeipräsidium Ludwigsburg
Telefon: 07141 18-9
E-Mail: ludwigsburg.pp@polizei.bwl.de
http://www.polizei-bw.de/

Original-Content von: Polizeipräsidium Ludwigsburg, übermittelt durch news aktuell
"""


split30 = [
 '2015 – 10:00 Polizeipräsidium Ludwigsburg Ludwigsburg (ots) Remseck am Neckar: Zusammenstoß mit Stadtbahn Am Freitagnachmittag um kurz vor 15.00 Uhr ereignete sich auf der Kreuzung L1100 / Am Holzbach in Remseck am Neckar ein Verkehrsunfall zwischen einem LKW und einer Stadtbahn der Linie U14. Als der 57-jährige LKW Fahrer von der Landstraße nach links in die Straße Am Holzbach einbiegen wollte, übersah der die von hinten kommende, vorfahrtberechtigte Stadtbahn. Der Stadtbahnführer führte vergeblich eine Vollbremsung durch und stieß schließlich mit dem Anhänger des LKW zusammen. Verletzt wurde dabei niemand. Der Sachschaden beträgt mindestens 13.000 Euro. Der dortige Schienenverkehr musste für ca. 45 Minuten unterbrochen werden.',
 'Möglingen: LKW gerät beim Fahren in Brand Am Freitagnachmittag um kurz nach 17.00 Uhr befuhr ein 42-jähriger LKW-Fahrer die Straße im Bornrain in Möglingen. Aus unbekannter Ursache geriet während der Fahrt die Ladung, bestehend aus Folien, in Brand. Der Fahrer konnte anhalten, ehe der Innenraum seines LKW ausbrannte. Verletzt wurde niemand. Der Sachschaden beträgt ungefähr 8000 Euro. Die Feuerwehr war mit drei Fahrzeugen und 20 Einsatzkräften vor Ort.',
 'Kornwestheim: Flächenbrand von Acker Aus bislang unbekannter Ursache geriet am Freitagnachmittag gegen 18.00 Uhr ein frisch gemähter Acker im Bereich zwischen Kornwestheim und Ludwigsburg in Brand. Der Brand erstreckte sich über eine Fläche von 400 m². Die Höhe des entstandenen Schadens kann nicht beziffert werden, liegt aber bei höchstens 200 Euro. Die Feuerwehr war mit drei Fahrzeugen und 27 Feuerwehrleuten im Einsatz.',
 ]






###############################################################################


text31 = """
27.11.2015 – 11:30


Polizeipräsidium Ulm


Ulm (ots)

 Die Diebe brachen im Dieselweg in Ehingen ein Fenster auf und kletterten ins Innere. Dort fanden sie eine Kamera und einen  Computer. Mit diesen Sachen machten sich die Unbekannten auf und davon. 

In Rottenacker schlug jemand die Scheibe eines Hauses in der Braigestraße ein. Der Täter konnte das Fenster öffnen und hatte so den Weg frei. Er hatte es auf das Geld in der Firma abgesehen. Dieses fand er in Automaten. Auch eine Flasche Alkohol nahm der Unbekannte mit. 

In beiden Fällen ermittelt jetzt das Polizeirevier Ehingen. Spezialisten sicherten die Spuren der Taten. Mit ihrer Hilfe, aber auch den jetzt folgenden Ermittlungen, wollen die Beamten die Verantwortlichen für die Straftaten finden. 

++++++++++++++++ 2168889 2167618 

Wolfgang Jürgens, Tel. 0731/188-1111, E-Mail: ulm.pp.stab.oe@polizei.bwl.de 

 

Rückfragen bitte an:

Polizeipräsidium Ulm
Telefon: 0731 188-0
E-Mail: ulm.pp@polizei.bwl.de
http://www.polizei-bw.de/

Original-Content von: Polizeipräsidium Ulm, übermittelt durch news aktuell
"""



split31 = ['2015 – 11:30 Polizeipräsidium Ulm Ulm (ots) Die Diebe brachen im Dieselweg in Ehingen ein Fenster auf und kletterten ins Innere. Dort fanden sie eine Kamera und einen Computer. Mit diesen Sachen machten sich die Unbekannten auf und davon. In Rottenacker schlug jemand die Scheibe eines Hauses in der Braigestraße ein. Der Täter konnte das Fenster öffnen und hatte so den Weg frei. Er hatte es auf das Geld in der Firma abgesehen. Dieses fand er in Automaten. Auch eine Flasche Alkohol nahm der Unbekannte mit. In beiden Fällen ermittelt jetzt das Polizeirevier Ehingen. Spezialisten sicherten die Spuren der Taten. Mit ihrer Hilfe, aber auch den jetzt folgenden Ermittlungen, wollen die Beamten die Verantwortlichen für die Straftaten finden.']

###############################################################################


text32 = """
16.02.2015 – 10:58


Polizeipräsidium Mannheim


Leimen/Rhein-Neckar-Kreis (ots)

 Die Kollision zwischen einer Straßenbahn der Linie 23 und einem Auto verlief am Montagvormittag entgegen ersten Meldungen doch glimpflich. 

Kurz nach 9 Uhr war ein 58-jähriger Ford-Fahrer auf der Rohrbacher Straße in Richtung Innenstadt unterwegs, als er nach links in den Fischerweg abbiegen wollte. Dabei übersah er die nachfolgende Straßenbahn, die nicht mehr rechtzeitig anhalten konnte, um den Zusammenstoß zu verhindern. 

Verletzt wurde zum Glück auch in der nur mit wenigen Fahrgästen besetzten Straßenbahn niemand. Der Sachschaden beläuft sich auf rund 8.000.- Euro. Der Schienenverkehr war für rund 45 Minuten gesperrt. 

 

Rückfragen bitte an:

Polizeipräsidium Mannheim
Öffentlichkeitsarbeit
Norbert Schätzle
Telefon: 0621 174-1102
E-Mail: mannheim.pp@polizei.bwl.de
http://www.polizei-bw.de/

Original-Content von: Polizeipräsidium Mannheim, übermittelt durch news aktuell
"""

split32 = ['2015 – 10:58 Polizeipräsidium Mannheim Leimen/Rhein-Neckar-Kreis (ots) Die Kollision zwischen einer Straßenbahn der Linie 23 und einem Auto verlief am Montagvormittag entgegen ersten Meldungen doch glimpflich. Kurz nach 9 Uhr war ein 58-jähriger Ford-Fahrer auf der Rohrbacher Straße in Richtung Innenstadt unterwegs, als er nach links in den Fischerweg abbiegen wollte. Dabei übersah er die nachfolgende Straßenbahn, die nicht mehr rechtzeitig anhalten konnte, um den Zusammenstoß zu verhindern. Verletzt wurde zum Glück auch in der nur mit wenigen Fahrgästen besetzten Straßenbahn niemand. Der Sachschaden beläuft sich auf rund 8.000.- Euro. Der Schienenverkehr war für rund 45 Minuten gesperrt.']



###############################################################################

text33 = """
13.02.2015 – 15:26


Polizeipräsidium Aalen


Rems-Murr-Kreis: (ots)

 Berglen-Hößlinswart: Brandursache weiterhin unklar 

Im Zusammenhang mit dem Brand am frühen Freitagmorgen in der Hirschstraße in Hößlinswart gibt es aktuell noch keine Hinweise auf die Ursache des Brandes. Wie berichtet, brach kurz vor 3.30 Uhr im Dachgeschoss eines Doppelhauses ein Feuer aus. Die Bewohner konnten sich retten. Das Haus ist nicht mehr bewohnbar. Die Bewohner sind allesamt bei Bekannten und Verwandten untergekommen. Eine Besichtigung der näheren Brandstelle ist frühestens am Montag möglich. Die Ortsdurchgangsstraße ist seit kurz nach 13 Uhr wieder befahrbar. 

Fellbach - Auffahrunfall 

An der Kreuzung Eberhardstraße / Bühlstraße wollte am Freitagmorgen gegen 08:00 Uhr eine 48-jährige Opel-Fahrerin rechts abbiegen. Dazu musste sie auf die Rechtsabbiegerspur wechseln und abbremsen. Ein hinter ihr fahrender 48-jähriger Mercedes Benz Fahrer wollte ebenfalls rechts abbiegen und ordnete sich hinter der Opelfahrerin ein. Dabei bemerkte er das Abbremsen seiner Vorderfrau zu spät, und fuhr dieser auf. Dabei entstand Sachschaden in Höhe von 4000EUR. 

Weinstadt - vergeblicher Einbruchsversuch 

In der Nacht von Donnerstag auf Freitag versuchte ein unbekannter Täter in einen Imbiss in der Straße Im Biegel einzubrechen. Dazu versuchte er mittels eines Hebelwerkzeugs die Eingangstüre aufzumachen, was ihm jedoch misslang. Somit blieb es bei einem reinen Sachschaden, der mit ca. 500Eur beziffert wird. 

Winnenden - Einbruch in Imbiss 

Zwischen Mitternacht und den frühen Morgenstunden des heutigen Freitags brachen unbekannte Täter in einen Imbiss in der Alfred-Kärcher-Straße ein. Nach dem Eindringen in die Räumlichkeiten gingen die Täter zielgerichtet auf die Geldspielautomaten zu und brachen diese auf. Wie viel Geld daraus erbeutet werden konnte ist noch nicht bekannt. Durch den Einbruch und das Hebeln an den Automaten entstand ein Sachschaden in Höhe von 2000EUR. 

Schorndorf - 400 Liter Diesel gestohlen 

Unbekannte begaben sich zwischen Donnerstagnachmittag 17:00 Uhr und Freitagmorgen 06:50 Uhr auf eine Baustelle in der Richard-Kapphan-Straße. Dort entnahmen sie den abgestellten Baumaschinen ca. 400 Liter Diesel. 

Fellbach - Fahrradfahrerin und Fußgänger geraten aneinander 

Am vergangenen Montag befuhr ein 12-jähriges Mädchen den Gehweg der Fellbacher Straße. Dort begegnete sie einem Mann, mit dem es zu einem beinah- Zusammenstoß kam. In der Folge dieser Situation beleidigte der Mann das Mädchen, das daraufhin davon fuhr. Der Mann wird als groß und kräftig beschrieben. Er sei Ende 40 / Anfang 50 Jahre alt und habe grauschwarz gelockte Haare. Bekleidet war er mit einer dunkelblaue Jeans, einer dunklen Lederjacke und schwarzen Herrenschuhen. Zeugen des Vorfalls oder Personen, die Hinweise zu dem Mann geben können werden gebeten, sich beim Polizeiposten Schmiden unter 0711 9519130 zu melden. 

Backnang: Bierflasche durch Fenster geworfen 

Am Donnerstag kurz vor Mitternacht betrat eine dreiköpfige Personengruppe das Jungendzentrum in der Mühlstraße. Zwischen den anwesenden Gästen und der alkoholisierten Gruppierung kam es relativ rasch zu einer Diskussion über die jüngsten Pegida-Ereignissen. Da die Situation zu eskalieren begann, wurden die drei Personen aufgefordert, das Jugendzentrum wieder zu verlassen. Sie kamen dieser Aufforderung nach, jedoch wurde beim Weggehen eine Bierflasche gegen ein Fenster geworfen. Hierbei ging auch die Fensterscheibe zu Bruch. Die hinzugerufene Polizei konnte in unmittelbarer Umgebung die mutmaßlichen Verantwortlichen antreffen. Es stellte sich heraus, dass eine 27-Jährige sich vermutlich beim Einschlagen der Fensterscheibe leicht verletzt hatte. Ob die Täter politisch motiviert gehandelt haben, ist derzeit auch Gegenstand der polizeilichen Ermittlungen. 

Schorndorf: Täter nach Raubdelikt in Haft 

Die Schorndorfer Polizei nahmen am Mittwochabend in Winterbach zwei Tatverdächtige einer Raubstraftat fest, die sich bereits am Samstag gegen 2.30 Uhr am Bahnhof ereignete. Dort gerieten ein 24-Jähriger und sein Begleiter mit einer dreiköpfigen Gruppierung aneinander. Die Konfrontation begann zunächst von Seiten der Tätergruppierung mit verbalen Provokationen und setzte sich im Verlauf der Auseinandersetzung mit massiven Drohungen fort. Die Täter forderten Ihre Opfer zur Herausgabe ihrer mitgeführten Geldbörsen auf. Um den Ganzen noch Nachdruck zu verleihen, wurden die Opfer gegen Kopf und Körper geschlagen sowie mit einem Messer bedroht. Das 24-jährige Opfer wurde hierbei verletzt. Die Täter konnten mit dem erbeutetem Bargeld in Höhe von ca. 120 Euro flüchten. 

Eine Polizeistreife erkannte zwei der Tatverdächtigen auf einem P&R Parkplatz beim Bahnhof Winterbach wieder und nahm die beiden 19-jährigen Männer vorläufig fest. Die weiteren Ermittlungen bestätigten den Tatverdacht und führten die Ermittler auf die Spur des dritten Beteiligten. Dieser 21-Jährige konnte bei einer vom Amtsgericht Stuttgart angeordneten Wohnungsdurchsuchung am 12.02.2015 ebenfalls festgenommen werden. Gegen die 19-jährigen Täter erging noch am Donnerstag Haftbefehl, welcher auch sofort vollstreckt wurde. Der 21-Jährige und mutmaßliche Träger der Tatwaffe wurde am Freitag dem Haftrichter vorgeführt, der Haftbefehl erließ. Der junge Mann wurde sodann in eine Justizvollzugsanstalt eingeliefert. 

 

Rückfragen bitte an:

Polizeipräsidium Aalen
Öffentlichkeitsarbeit
Telefon: 07361 580-105 bis 110
E-Mail: aalen.pp.stab.oe@polizei.bwl.de
http://www.polizei-bw.de/

Original-Content von: Polizeipräsidium Aalen, übermittelt durch news aktuell
"""


split33 = [
 '2015 – 15:26 Polizeipräsidium Aalen  Rems-Murr-Kreis: (ots)  Berglen-Hößlinswart: Brandursache weiterhin unklar Im Zusammenhang mit dem Brand am frühen Freitagmorgen in der Hirschstraße in Hößlinswart gibt es aktuell noch keine Hinweise auf die Ursache des Brandes. Wie berichtet, brach kurz vor 3.30 Uhr im Dachgeschoss eines Doppelhauses ein Feuer aus. Die Bewohner konnten sich retten. Das Haus ist nicht mehr bewohnbar. Die Bewohner sind allesamt bei Bekannten und Verwandten untergekommen. Eine Besichtigung der näheren Brandstelle ist frühestens am Montag möglich. Die Ortsdurchgangsstraße ist seit kurz nach 13 Uhr wieder befahrbar.',
 'Fellbach - Auffahrunfall An der Kreuzung Eberhardstraße / Bühlstraße wollte am Freitagmorgen gegen 08:00 Uhr eine 48-jährige Opel-Fahrerin rechts abbiegen. Dazu musste sie auf die Rechtsabbiegerspur wechseln und abbremsen. Ein hinter ihr fahrender 48-jähriger Mercedes Benz Fahrer wollte ebenfalls rechts abbiegen und ordnete sich hinter der Opelfahrerin ein. Dabei bemerkte er das Abbremsen seiner Vorderfrau zu spät, und fuhr dieser auf. Dabei entstand Sachschaden in Höhe von 4000EUR.',
 'Weinstadt - vergeblicher Einbruchsversuch In der Nacht von Donnerstag auf Freitag versuchte ein unbekannter Täter in einen Imbiss in der Straße Im Biegel einzubrechen. Dazu versuchte er mittels eines Hebelwerkzeugs die Eingangstüre aufzumachen, was ihm jedoch misslang. Somit blieb es bei einem reinen Sachschaden, der mit ca. 500Eur beziffert wird.',
 'Winnenden - Einbruch in Imbiss Zwischen Mitternacht und den frühen Morgenstunden des heutigen Freitags brachen unbekannte Täter in einen Imbiss in der Alfred-Kärcher-Straße ein. Nach dem Eindringen in die Räumlichkeiten gingen die Täter zielgerichtet auf die Geldspielautomaten zu und brachen diese auf. Wie viel Geld daraus erbeutet werden konnte ist noch nicht bekannt. Durch den Einbruch und das Hebeln an den Automaten entstand ein Sachschaden in Höhe von 2000EUR.',
 'Schorndorf - 400 Liter Diesel gestohlen Unbekannte begaben sich zwischen Donnerstagnachmittag 17:00 Uhr und Freitagmorgen 06:50 Uhr auf eine Baustelle in der Richard-Kapphan-Straße. Dort entnahmen sie den abgestellten Baumaschinen ca. 400 Liter Diesel.',
 'Fellbach - Fahrradfahrerin und Fußgänger geraten aneinander Am vergangenen Montag befuhr ein 12-jähriges Mädchen den Gehweg der Fellbacher Straße. Dort begegnete sie einem Mann, mit dem es zu einem beinah- Zusammenstoß kam. In der Folge dieser Situation beleidigte der Mann das Mädchen, das daraufhin davon fuhr. Der Mann wird als groß und kräftig beschrieben. Er sei Ende 40 / Anfang 50 Jahre alt und habe grauschwarz gelockte Haare. Bekleidet war er mit einer dunkelblaue Jeans, einer dunklen Lederjacke und schwarzen Herrenschuhen. Zeugen des Vorfalls oder Personen, die Hinweise zu dem Mann geben können werden gebeten, sich beim Polizeiposten Schmiden unter 0711 9519130 zu melden.',
 'Backnang: Bierflasche durch Fenster geworfen Am Donnerstag kurz vor Mitternacht betrat eine dreiköpfige Personengruppe das Jungendzentrum in der Mühlstraße. Zwischen den anwesenden Gästen und der alkoholisierten Gruppierung kam es relativ rasch zu einer Diskussion über die jüngsten Pegida-Ereignissen. Da die Situation zu eskalieren begann, wurden die drei Personen aufgefordert, das Jugendzentrum wieder zu verlassen. Sie kamen dieser Aufforderung nach, jedoch wurde beim Weggehen eine Bierflasche gegen ein Fenster geworfen. Hierbei ging auch die Fensterscheibe zu Bruch. Die hinzugerufene Polizei konnte in unmittelbarer Umgebung die mutmaßlichen Verantwortlichen antreffen. Es stellte sich heraus, dass eine 27-Jährige sich vermutlich beim Einschlagen der Fensterscheibe leicht verletzt hatte. Ob die Täter politisch motiviert gehandelt haben, ist derzeit auch Gegenstand der polizeilichen Ermittlungen.',
 'Schorndorf: Täter nach Raubdelikt in Haft Die Schorndorfer Polizei nahmen am Mittwochabend in Winterbach zwei Tatverdächtige einer Raubstraftat fest, die sich bereits am Samstag gegen 2.30 Uhr am Bahnhof ereignete. Dort gerieten ein 24-Jähriger und sein Begleiter mit einer dreiköpfigen Gruppierung aneinander. Die Konfrontation begann zunächst von Seiten der Tätergruppierung mit verbalen Provokationen und setzte sich im Verlauf der Auseinandersetzung mit massiven Drohungen fort. Die Täter forderten Ihre Opfer zur Herausgabe ihrer mitgeführten Geldbörsen auf. Um den Ganzen noch Nachdruck zu verleihen, wurden die Opfer gegen Kopf und Körper geschlagen sowie mit einem Messer bedroht. Das 24-jährige Opfer wurde hierbei verletzt. Die Täter konnten mit dem erbeutetem Bargeld in Höhe von ca. 120 Euro flüchten. Eine Polizeistreife erkannte zwei der Tatverdächtigen auf einem P&R Parkplatz beim Bahnhof Winterbach wieder und nahm die beiden 19-jährigen Männer vorläufig fest. Die weiteren Ermittlungen bestätigten den Tatverdacht und führten die Ermittler auf die Spur des dritten Beteiligten. Dieser 21-Jährige konnte bei einer vom Amtsgericht Stuttgart angeordneten Wohnungsdurchsuchung am 12.02.2015 ebenfalls festgenommen werden. Gegen die 19-jährigen Täter erging noch am Donnerstag Haftbefehl, welcher auch sofort vollstreckt wurde. Der 21-Jährige und mutmaßliche Träger der Tatwaffe wurde am Freitag dem Haftrichter vorgeführt, der Haftbefehl erließ. Der junge Mann wurde sodann in eine Justizvollzugsanstalt eingeliefert.',
 ]


###############################################################################


text34 = """
15.06.2015 – 15:11


Polizeipräsidium Konstanz


Wangen i. A. (ots)

 Wiederholt hat die Verkehrspolizei Geschwindigkeitsmessungen auf der Autobahn A 96 München - Lindau, auf der Talbrücke Obere Argen, durchgeführt. Die Geschwindigkeit ist dort wegen beschränkter Betriebssicherheit nach einem schweren Verkehrsunfall am 03.03.2015 auf 80 km/h beschränkt. Am Sonntag, 14.06.2015, wurden von 10.45 Uhr bis 16.00 Uhr, mittels eines Laser-Großmessgerätes Geschwindigkeitsmessungen durchgeführt. Insgesamt wurden 6064 Fahrzeuge gemessen. Davon überschritten 2130 Fahrzeuge die zulässige Höchstgeschwindigkeit von 80 km/h. Davon wiederum müssen zirka 500 Autofahrer mit einem Fahrverbot rechnen. Die höchste gemessene Geschwindigkeit betrug 209 km/h. Die Polizei appelliert an alle Fahrzeugführer auch in diesem Bereich die zulässige Höchstgeschwindigkeit nicht zu überschreiten. Insbesondere auch an Autofahrer aus Österreich und der Schweiz. Es ist auch künftig auf der Brücke mit Geschwindigkeitskontrollen zu rechnen. 

Hauke 

 

Rückfragen bitte an:

Polizeipräsidium Konstanz
Telefon: 07531 995-0
E-Mail: konstanz.pp@polizei.bwl.de
http://www.polizei-bw.de/

Original-Content von: Polizeipräsidium Konstanz, übermittelt durch news aktuell
"""


split34 = ['2015 – 15:11 Polizeipräsidium Konstanz Wangen i. A. (ots) Wiederholt hat die Verkehrspolizei Geschwindigkeitsmessungen auf der Autobahn A 96 München - Lindau, auf der Talbrücke Obere Argen, durchgeführt. Die Geschwindigkeit ist dort wegen beschränkter Betriebssicherheit nach einem schweren Verkehrsunfall am 03.03.2015 auf 80 km/h beschränkt. Am Sonntag, 14.06.2015, wurden von 10.45 Uhr bis 16.00 Uhr, mittels eines Laser-Großmessgerätes Geschwindigkeitsmessungen durchgeführt. Insgesamt wurden 6064 Fahrzeuge gemessen. Davon überschritten 2130 Fahrzeuge die zulässige Höchstgeschwindigkeit von 80 km/h. Davon wiederum müssen zirka 500 Autofahrer mit einem Fahrverbot rechnen. Die höchste gemessene Geschwindigkeit betrug 209 km/h. Die Polizei appelliert an alle Fahrzeugführer auch in diesem Bereich die zulässige Höchstgeschwindigkeit nicht zu überschreiten. Insbesondere auch an Autofahrer aus Österreich und der Schweiz. Es ist auch künftig auf der Brücke mit Geschwindigkeitskontrollen zu rechnen.']

###############################################################################

text35 = """
20.06.2015 – 12:27


Polizeipräsidium Reutlingen


Reutlingen (ots)

 Bad Urach (RT): Trickdiebstahl aus Wohnhaus 

Am Freitag um die Mittagszeit klingelte ein unbekannter Mann in der Lange Straße und gab an, dass er den Wasserdruck in der Wasserleitung prüfen müsse. Die 88-jährige Bewohnerin ließ den Unbekannten ins Haus und ging zusammen mit ihm in den Keller. Wahrscheinlich lehnte der Unbekannte die Haustüre nur an, so dass ein Mittäter unbemerkt Zutritt in das Haus bekommen konnte. Nach ca. 20 Minuten klingelte es erneut an der Haustüre und ein zweiter Mann gab sich als Chef des Unbekannten aus. Kurze Zeit später verließ der Unbekannte dann unter einem Vorwand das Haus. Eine Stunde später bemerkte die 88-Jährige, dass bei ihr Schmuck im Wert von mehreren tausend Euro gestohlen wurde. Die beiden Unbekannten werden wir folgt beschrieben. Täter 1: ca. 25 Jahre alt, 165 cm groß, sehr schlank, braune zurück gekämmte Haare, bekleidet mit blauer Arbeitshose und Arbeitsjacke. Der zweite Täter ist ca. 30-35 Jahre alt, ca. 180 cm groß, kräftige dicke Statur, rundes Gesicht, dunkelbraune Haare, bekleidet mit schwarzer Hose und Jacke. Die Polizei Metzingen sucht Zeugen unter 07123/9240. 

Köngen (ES) - Beim Anfahren vom Fahrbahnrand Unfall verursacht 

Ein 61-jähriger Fahrzeuglenker fuhr am Freitagabend gegen 19:30 Uhr in der Christian-Eisele-Straße mit seinem Pkw Ford vom Fahrbahnrand an und übersah hierbei eine 88-jährige Daimler-Lenkerin. Die beiden Fahrzeuge verhakten sich so stark, dass an dem Daimler-Benz der rechte Vorderreifen in seiner Aufhängung brach. Im weiteren Verlauf prallte der Daimler-Benz gegen einen Zaun einer angrenzenden Firma. Die 88-jährige Lenkerin musste durch den Rettungsdienst in ein Klinikum eingeliefert werden. Es entstand ein Sachschaden in Höhe von mehreren tausend Euro. Das Verkehrskommissariat Esslingen hat die Ermittlungen aufgenommen. 

Wendlingen (ES) - Beim Einfahren aus Grundstück Radfahrer übersehen 

Am Freitag, kurz vor 17:30 Uhr, wollte eine 40-Jährige von einer Grundstückausfahrt nach links in die Wertstraße einbiegen. Aufgrund einer Parkreihe am Fahrbahnrand war die Sicht eingeschränkt. Beim Einfahren prallte die 40-jährige Lenkerin mit einem 46-jährigen Radfahrer zusammen. Der Radfahrer schlug mit dem Oberkörper auf die Frontscheibe des Pkw auf. Der 46-jährige Radfahrer wurde verletzt durch den Rettungsdienst in eine Klinik eingeliefert. Der Radfahrer trug zum Unfallzeitpunkt einen Helm. Der Gesamtsachschaden beträgt insgesamt mehrere tausend Euro. 

Esslingen - Unter Alkoholeinwirkung ein Fahrzeug gelenkt und im Anschluss Widerstand geleistet. 

Am Freitag kurz vor Mitternacht wurde von Beamten des Polizeireviers Esslingen ein 26-Jähriger zu einer Verkehrskontrolle angehalten. Hierbei bemerkte die Streifenbesatzung, dass der Fahrzeuglenker unter Alkoholeinwirkung stand. Um eine Blutentnahme durchzuführen, wurde der 26-Jährige zur Dienststelle verbracht. Dort leistete dieser erheblichen Widerstand und verletzte hierbei zwei eingesetzte Beamte leicht. Nach der erfolgten Blutentnahme drohte der 26-Jährige erneut den Beamten. Der Fahrzeuglenker muss sich jetzt noch zusätzlich zu der Trunkenheitsfahrt wegen Widerstand gegen Polizeivollzugsbeamte verantworten. 

Esslingen - Abstand falsch eingeschätzt und Unfall mit über 10 000 Euro Schaden verursacht 

Am Freitagmittag kurz nach 13:00 Uhr, wollte eine 64-jährige VW-Lenkerin in der Krummenackerstraße nach links in die Alexanderstraße einbiegen und kollidierte mit der entgegenkommenden 81-jährigen Lenkerin eines Fiats. Glücklicherweise wurde niemand verletzt. Beide Fahrzeuge mussten durch ein Unternehmen abgeschleppt werden. Der Sachschaden wird auf über 10 000 Euro beziffert. 

Ostfildern(ES) - Streifenfahrzeug der Polizei auf Alarmfahrt verunglückt 

Am Freitagnachmittag, gegen 17:45 Uhr, kam es an der Kreuzung Hindenburgstraße/Rinnenbachstraße zu einem Verkehrsunfall mit einem Streifenfahrzeug des Polizeireviers Filderstadt. Der Streifenwagen befuhr mit eingeschaltetem Sondersignal die Hindenburgstraße in Richtung Ortsmitte Nellingen. An der Kreuzung fuhr der 39-jährige Polizeibeamte bei Rot in den Kreuzungsbereich ein, nachdem bereits eine Autofahrerin auf der Rinnenbachstraße anhielt, um dem Einsatzfahrzeug die Einfahrt in den Kreuzungsbereich zu ermöglichen. Eine weitere 36-jährige Pkw-Lenkerin erkannte diese Situation zu spät, überholte die wartende Autofahrerin und fuhr in den Kreuzungsbereich ein. Im Kreuzungsbereich kollidierte die 36-Jährige mit ihrem Pkw Mazda mit dem Streifenfahrzeug. Der Polizeiwagen geriet ins Schleudern und kam an der Hecke eines angrenzenden Grundstückes zum Stillstand. Verletzt wurde niemand. An beiden Fahrzeugen entstand ein Gesamtsachschaden in Höhe von über 20 000 Euro. Das Einsatzfahrzeug war nicht mehr fahrbereit und musste durch ein Unternehmen geborgen werden. Der anstehende dringliche polizeiliche Einsatz wurde kurzerhand einem anderen Einsatzwagen zugewiesen. 

Neckartailfingen (ES) - Frontalzusammenstoß, 4 Leichtverletzte 

Eine 18-jährige Fahrerin eines VW Polo befuhr am Samstagmorgen gegen 01:20 Uhr die Stuttgarter Straße von Schlaitdorf kommend in Richtung Neckartailfingen. In einer Linkskurve kam diese aus unbekannter Ursache nach links auf den Gegenfahrstreifen und stieß dort mit einem 25-jährigen Fahrer eines VW Golf zusammen. Die Fahrer und 2 Mitfahrer im VW Golf im Alter von 24 und 25 Jahren wurden leicht verletzt und wurden in Krankenhäuser gebracht. Es entstand ein Sachschaden von ca. 4000 Euro. 

Nürtingen (ES) - 6 Personen nach Drogenmissbrauch in Kliniken eingeliefert 

Am Samstag, kurz nach 01:00 Uhr, mussten insgesamt 4 Rettungswagen  nach Nürtingen zur Braikeschule ausrücken. Dort hatten mehrere Personen im Alter zwischen 20 und 30 Jahren eine bislang noch unbekannte Substanz geraucht. Im Anschluss mussten insgesamt 6 Personen durch den Rettungsdienst in verschiedene Kliniken eingeliefert werden. Das Polizeirevier Nürtingen befand sich ebenfalls mit 2 Streifenbesatzungen im Einsatz. 

Tübingen (TÜ) - Unfallflucht: Polizei sucht Zeugen 

Ein Sachschaden von ca. 2000 Euro entstand an einem blauen Ford Fiesta auf dem Parkplatz eines Elektronikmarktes im Schleifmühleweg. Der Geschädigte parkte sein Fahrzeug am Freitag gegen 18:30 Uhr. Als er gegen 19:10 Uhr wieder zu seinem Fahrzeug kam, stellte er auf der linken Fahrzeugseite eine Beschädigung fest. Links neben dem Ford war ein rotes Fahrzeug geparkt. Zeugen werden gebeten sich mit dem Polizeirevier Tübingen unter Tel. 07071/972-8660 in Verbindung zu setzen. 

Ofterdingen (TÜ) - Von der Fahrbahn abgekommen 

Unaufmerksam war eine 51-jährige Lenkerin eines Fiat 500. Diese war am Freitag gegen 15:00 Uhr auf der B 27 von Dußlingen in Richtung Ofterdingen unterwegs. Kurz vor Ortsbeginn Ofterdingen erkannte diese einen Rückstau zu spät. Bei dem Versuch das Fahrzeug abzubremsen, kam sie nach rechts von der Fahrbahn ab, überfuhr hierbei einen Leitpfosten und kam nach ca. 150 Metern, nach Überfahren der dortigen Böschung, zum Stehen. Glücklicherweise wurde die 51-jährige hierbei nicht verletzt. Auch der Pkw wurde hierbei nicht beschädigt. Die B 27 war während der Bergung des Pkw durch einen Kran für ca. 2 Stunden nur einspurig befahrbar. 

 

Rückfragen bitte an:

Peter Buckenmaier, PvD

Polizeipräsidium Reutlingen
Telefon: 07121 942-2224
E-Mail: reutlingen.pp.stabst.oe@polizei.bwl.de
http://www.polizei-bw.de/

Original-Content von: Polizeipräsidium Reutlingen, übermittelt durch news aktuell

"""

###############################################################################

text36 = """
08.10.2019 – 12:15


Polizeipräsidium Heilbronn


Heilbronn (ots)

 Eppingen: Einbruch in Firmengebäude 

Ein Firmengebäude in der Eppinger Lohmühlstraße wurde zwischen Samstag und Montag Ziel von unbekannten Einbrechern. Zunächst wurde versucht ein Fenster aufzuhebeln wodurch die Scheibe zersplitterte. Hierdurch gelang es das Fenster zu öffnen. Anschließend kletterten der oder die Diebe in das Innere und entwendeten einen Laptop und ein Programmiergerät. Der Diebstahlschaden dürfte im mittleren vierstelligen Bereich liegen. Der Schaden am Fenster beziffert sich auf circa 500 Euro. Wie sich herausstellte versuchten die Unbekannten zuvor ein Schloss einer Nebeneingangstür aufzuhebeln, was misslang. Zeugen, die am vergangenen Wochenende im Bereich der Lohmühlstraße verdächtige Wahrnehmungen machen konnten, werden darum gebeten, sich bei der Polizei in Eppingen, Telefon 07262 60950, zu melden. 

Heilbronn-Sontheim: Einbruch in Kindergarten 

Auf eine Stereoanlage hatten es Unbekannte bei ihrem Einbruch in einen Kindergarten in der Sontheimer Güldensteinstraße abgesehen. Wie die Tatverdächtigen zwischen Mittwoch, 2. Oktober und Montagmorgen gelangten, ist derzeit noch nicht klar. Vielleicht wollten die Unbekannten im Schulhof Musik hören, denn dort verblieb die Anlage. Im Abstellraum des Kindergartens sprühten die Unbekannten drei Schriftzüge an die Wand und nahmen aus der Küche noch ein Festnetztelefon mit. Mutmaßlich von der gleichen Täterschaft wurde ein Verkehrsschild in ein Klettergerüst an der Staufenbergschule gesteckt, welches zuvor in der Max-Planck-Straße entwendet worden war. Zeugenhinweise werden an das Polizeirevier in Heilbronn, Telefon 07131 104 2500, erbeten. 

Brackenheim: Mann stürzt sechs Meter in die Tiefe 

Sechs Meter sürzte ein Arbeiter am Montagnachmittag in Brackenheim von einer Maurer in die Tiefe und verletzte sich hierbei schwer. Der Mann versuchte nach bisherigem Ermittlungsstand, gegen 14.30 Uhr, in der Straße "Schloßplatz" ein Schalbrett an einem Gebäude zu lösen und verlor hierbei das Gleichgewicht. Er wurde durch den Rettungsdienst in ein Krankenhaus gebracht. 

Neckarsulm: Fahrradfahrerin verletzt, Pkw-Fahrer flüchtet 

Beim Einfahren in die Neckarsulmer Kochendörfer Straße übersah der Fahrer eines silbernen Fahrzeugs am Montagnachmittag, gegen 12.30 Uhr, eine von rechts kommende Fahrradfahrerin. Das 13-jährige Mädchen konnte einen Zusammenstoß mit dem Auto nicht mehr verhindern und kam hierdurch zu Fall. Ihr linker Fuß geriet hierbei in den Radkasten des Wagens. Der Fahrer stieg zunächst aus, erkundigte sich nach dem Befinden, half dem Mädchen aufzustehen und entfernte sich dann von der Unfallstelle in Richtung eines Einkaufsmarkts und ging dort einkaufen. Die Polizei Neckarsulm sucht Zeugen des Vorfalls. Das Mädchen wurde leichtverletzt. Hinweise werden an das Polizeirevier in Neckarsulm, Telefon 07132 93710, erbeten. 

 

Rückfragen bitte an:

Polizeipräsidium Heilbronn
Telefon: 07131 104-10 17
E-Mail: heilbronn.pp@polizei.bwl.de
http://www.polizei-bw.de/

Original-Content von: Polizeipräsidium Heilbronn, übermittelt durch news aktuell
"""

split36 = [
 '2019 – 12:15 Polizeipräsidium Heilbronn Heilbronn (ots)  Eppingen: Einbruch in Firmengebäude Ein Firmengebäude in der Eppinger Lohmühlstraße wurde zwischen Samstag und Montag Ziel von unbekannten Einbrechern. Zunächst wurde versucht ein Fenster aufzuhebeln wodurch die Scheibe zersplitterte. Hierdurch gelang es das Fenster zu öffnen. Anschließend kletterten der oder die Diebe in das Innere und entwendeten einen Laptop und ein Programmiergerät. Der Diebstahlschaden dürfte im mittleren vierstelligen Bereich liegen. Der Schaden am Fenster beziffert sich auf circa 500 Euro. Wie sich herausstellte versuchten die Unbekannten zuvor ein Schloss einer Nebeneingangstür aufzuhebeln, was misslang. Zeugen, die am vergangenen Wochenende im Bereich der Lohmühlstraße verdächtige Wahrnehmungen machen konnten, werden darum gebeten, sich bei der Polizei in Eppingen, Telefon 07262 60950, zu melden.',
 'Heilbronn-Sontheim: Einbruch in Kindergarten Auf eine Stereoanlage hatten es Unbekannte bei ihrem Einbruch in einen Kindergarten in der Sontheimer Güldensteinstraße abgesehen. Wie die Tatverdächtigen zwischen Mittwoch, 2. Oktober und Montagmorgen gelangten, ist derzeit noch nicht klar. Vielleicht wollten die Unbekannten im Schulhof Musik hören, denn dort verblieb die Anlage. Im Abstellraum des Kindergartens sprühten die Unbekannten drei Schriftzüge an die Wand und nahmen aus der Küche noch ein Festnetztelefon mit. Mutmaßlich von der gleichen Täterschaft wurde ein Verkehrsschild in ein Klettergerüst an der Staufenbergschule gesteckt, welches zuvor in der Max-Planck-Straße entwendet worden war. Zeugenhinweise werden an das Polizeirevier in Heilbronn, Telefon 07131 104 2500, erbeten.',
 'Brackenheim: Mann stürzt sechs Meter in die Tiefe Sechs Meter sürzte ein Arbeiter am Montagnachmittag in Brackenheim von einer Maurer in die Tiefe und verletzte sich hierbei schwer. Der Mann versuchte nach bisherigem Ermittlungsstand, gegen 14.30 Uhr, in der Straße "Schloßplatz" ein Schalbrett an einem Gebäude zu lösen und verlor hierbei das Gleichgewicht. Er wurde durch den Rettungsdienst in ein Krankenhaus gebracht.',
 'Neckarsulm: Fahrradfahrerin verletzt, Pkw-Fahrer flüchtet Beim Einfahren in die Neckarsulmer Kochendörfer Straße übersah der Fahrer eines silbernen Fahrzeugs am Montagnachmittag, gegen 12.30 Uhr, eine von rechts kommende Fahrradfahrerin. Das 13-jährige Mädchen konnte einen Zusammenstoß mit dem Auto nicht mehr verhindern und kam hierdurch zu Fall. Ihr linker Fuß geriet hierbei in den Radkasten des Wagens. Der Fahrer stieg zunächst aus, erkundigte sich nach dem Befinden, half dem Mädchen aufzustehen und entfernte sich dann von der Unfallstelle in Richtung eines Einkaufsmarkts und ging dort einkaufen. Die Polizei Neckarsulm sucht Zeugen des Vorfalls. Das Mädchen wurde leichtverletzt. Hinweise werden an das Polizeirevier in Neckarsulm, Telefon 07132 93710, erbeten.']

###############################################################################

text37 = """
08.12.2016 – 13:19

Polizeipräsidium Karlsruhe

Karlsruhe (ots)
 Erneut waren Karlsruher Firmen in vier bekanntgewordenen Fällen im Visier  von Einbrechern. 
Bargeld in Höhe von mehreren tausend Euro erbeuteten Diebe zwischen Dienstag, 17.30 Uhr, und Mittwoch, 06.15 Uhr, aus einem Firmenanwesen in der Koellestraße im Stadtteil Daxlanden. Dort hatten sie zuvor eine Werkstatttür mit brachialer Gewalt aufgebrochen, um sich mit Werkzeug zu rüsten. Anschließend schlugen die Einbrecher ein Fenster eines Bürogebäudes ein und öffneten mit einem zuvor ergatterten Trennschneider den Firmentresor, worin sich das Bargeld befand. 
Zwei unbekannte Täter versuchten am Mittwoch um 04.45 Uhr gewaltsam in einen Friseursalon in der Riedstraße einzudringen. Dank einer einbruchsgesicherten Eingangstür gelang es den Langfingern jedoch nicht, sich Zutritt zu den Räumlichkeiten zu verschaffen. Ein aufmerksamer Passant konnte die Tat beobachten. Die Diebe waren etwa 20 bis 40 Jahre alt, circa 180 cm groß, dunkel gekleidet und trugen einen Schal oder Tuch zur Maskierung. 
Im Heideweg hebelten Einbrecher zwischen Mittwoch, 13.30 Uhr, und Donnerstag, 04:35 Uhr, die Eingangstür einer Bäckereifiliale auf und stahlen anschließend einem grauen Wandtresor, in welchem sich mehrere hundert Euro Bargeld befand. 
In Mühlburg kam es Donnerstagfrüh gegen 03.45 Uhr in der Rheinstraße zu einem Einbruch in eine Spielothek. Um sich Zutritt in das Innere zu verschafften, durchtrennten die dreisten Diebe zunächst das Kabel der Alarmanlage und hebelten anschließend die Eingangstür auf. Aus der Theke wurde daraufhin eine schwarze Geldkassette mit mehreren hundert Euro Bargeld gestohlen. 
Sachdienliche Hinweise nimmt hierzu das Polizeirevier West unter 0721/939-4611 entgegen. 
Dennis Faber, Pressestelle 
 
Polizeipräsidium Karlsruhe
Telefon: 0721 666-1111
E-Mail: karlsruhe.pp.stab.oe@polizei.bwl.de
http://www.polizei-bw.de/
Original-Content von: Polizeipräsidium Karlsruhe, übermittelt durch news aktuell
"""


split37 = ['2016 – 13:19 Polizeipräsidium Karlsruhe Karlsruhe (ots) Erneut waren Karlsruher Firmen in vier bekanntgewordenen Fällen im Visier von Einbrechern. Bargeld in Höhe von mehreren tausend Euro erbeuteten Diebe zwischen Dienstag, 17.30 Uhr, und Mittwoch, 06.15 Uhr, aus einem Firmenanwesen in der Koellestraße im Stadtteil Daxlanden. Dort hatten sie zuvor eine Werkstatttür mit brachialer Gewalt aufgebrochen, um sich mit Werkzeug zu rüsten. Anschließend schlugen die Einbrecher ein Fenster eines Bürogebäudes ein und öffneten mit einem zuvor ergatterten Trennschneider den Firmentresor, worin sich das Bargeld befand. Zwei unbekannte Täter versuchten am Mittwoch um 04.45 Uhr gewaltsam in einen Friseursalon in der Riedstraße einzudringen. Dank einer einbruchsgesicherten Eingangstür gelang es den Langfingern jedoch nicht, sich Zutritt zu den Räumlichkeiten zu verschaffen. Ein aufmerksamer Passant konnte die Tat beobachten. Die Diebe waren etwa 20 bis 40 Jahre alt, circa 180 cm groß, dunkel gekleidet und trugen einen Schal oder Tuch zur Maskierung. Im Heideweg hebelten Einbrecher zwischen Mittwoch, 13.30 Uhr, und Donnerstag, 04:35 Uhr, die Eingangstür einer Bäckereifiliale auf und stahlen anschließend einem grauen Wandtresor, in welchem sich mehrere hundert Euro Bargeld befand. In Mühlburg kam es Donnerstagfrüh gegen 03.45 Uhr in der Rheinstraße zu einem Einbruch in eine Spielothek. Um sich Zutritt in das Innere zu verschafften, durchtrennten die dreisten Diebe zunächst das Kabel der Alarmanlage und hebelten anschließend die Eingangstür auf. Aus der Theke wurde daraufhin eine schwarze Geldkassette mit mehreren hundert Euro Bargeld gestohlen. Sachdienliche Hinweise nimmt hierzu das Polizeirevier West unter 0721/939-4611 entgegen.']

###############################################################################


def splitter_cases():

    pairs = [
        (text1, split1),
        (text2, split2),
        (text3, split3),
        (text4, split4),
        (text5, split5),
        (text6, split6),
        (text7, split7),
        (text8, split8),
        (text9, split9),
        (text10, split10),
        (text11, split11),
        (text12, split12),
        (text13, split13),
        (text14, split14),
        (text15, split15),
        (text16, split16),
        (text17, split17),
        (text18, split18),
        (text19, split19),
        (text20, split20),
        (text21, split21),
        (text22, split22),
        (text23, split23),
        (text24, split24),
        (text25, split25),
        (text26, split26),
        (text27, split27),
        (text28, split28),
        (text29, split29),
        (text30, split30),
        (text31, split31),
        (text32, split32),
        (text33, split33),
        (text34, split34),
        (text36, split36),
        (text37, split37),
        ]

    for text, split in pairs:
            yield text, split


@pytest.mark.parametrize("text,split", splitter_cases())
def test_splitter(text,split):
    list1 = [text.replace(" ", "") for text in ppSplitter.split_report(text)]
    list2 = [text.replace(" ", "") for text in split]
    assert list1 == list2, (list1, list2)