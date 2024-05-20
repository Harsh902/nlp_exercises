from nltk.book import text1, text3, text5
from nltk.corpus import gutenberg
from nltk.corpus import brown
import matplotlib.pyplot as plt
moby_dick = text1

jane_austin = gutenberg.words('austen-persuasion.txt')

#print(moby_dick.concordance("lightning"))

# for similatiry
#print(moby_dick.similar("very"))

# common contexts
#print(moby_dick.common_contexts(["very", "pretty"]))

# location of word in text
# text1.dispersion_plot(['monstrous', 'very', 'pretty'])
# plt.show()

# generating random text similar to what we input
#print(moby_dick.generate())

# total number of tokens
#print(len(text3))

# number of unique words
#print(sorted(set(text3)))

# number of unique words
# print(len(set(text3)))

# measuring lexical richness
#print(len(set(text3)) / len(text3))

# count specific words
#print(text3.count("thou"))

# percentage of text taken up by a word
#print(100 * (text3.count("thou") / len(text3)))


def lexical_diversity(text):
    return len(set(text)) / len(text)


def percentage(count, total):
    return 100 * count / total


def sum_word_length(text):
    return sum(len(w) for w in text)


def word_freq(word, category):
    return category.count(word)

#print(lexical_diversity(jane_austin))
#print(sum_word_length(moby_dick))
#print(sum_word_length(moby_dick) / len(moby_dick))


#print(word_freq('love', jane_austin))
#print(word_freq('nick', text5))


words = ['Apprize', 'Baptize']


def find_conditional_words(text, endings='ise', contains_letter='z'):
    words_set = set(text)
    words_list = []
    for w in words_set:
        if w.endswith(endings) and contains_letter in w and 'pt' in w and w.istitle():
            words_list.append(w)
    return words_list


webpage = """
Kein Tag ohne Nachrichten über Cyber Crimes. Vom gehackten persönlichen Social-Media-Account bis hin zu groß angelegten militärischen IT-Angriffen, wie zuletzt im Russland-Ukraine-Konflikt vermutet. Und wie in so vielen Lebensbereichen ist auch in der IT der »Faktor Mensch« Risikofaktor Nr. 1. Anderseits aber natürlich auch der größte Erfolgsfaktor. Viele Angriffe starten durch die Anwendung sogenannter »Social Engineering«-Methoden. Das gilt nicht nur für Privatpersonen oder Länder, sondern ebenso für Einrichtungen wie Hochschulen. Auch sie stehen längst im Fokus von IT-Kriminellen. Um uns alle in dieser Hinsicht besser zu schützen, möchten wir euch ein paar Tipps an die Hand geben. Damit jede und jeder von euch eher ein Erfolgs- als ein Risikofaktor ist.

Betriebssystem aktuell halten

Mit das wichtigste ist, stets unterstützte und aktuelle Betriebssystemversionen zu verwenden. Hierbei ist die Installation der Updates essenziell. Diese bieten neben funktionalen Erweiterungen oder Fehlerbehebungen auch die Eliminierung von Schwachstellen an, die zum Teil kritisch sein können. Beim Marktführer in diesem Bereich erfolgt die Bereitstellung der Updates in der Regel am sogenannte »Patch-Tuesday«. Das ist der jeweils zweite Dienstag im Monat. Aber es gibt auch Updates außer der Reihe. Zum Beispiel, wenn eine so schwerwiegende Lücke oder eine erhebliche funktionale Beeinträchtigung, etwa durch ein vorheriges Update, zu verzeichnen ist. Auch für andere Desktop-, Server und mobile Endgerätbetriebssysteme werden regelmäßig System- und Sicherheitsupdates angeboten. Man sollte sie grundsätzlich so schnell wie möglich anwenden. Immer. Die Anwendung der Updates ist zwar keine Garantie, dass das System damit schwachstellenfrei ist, es stellt aber zumindest die Behebung der bekannten Schwachstellen und den vom Hersteller bestmöglichen Stand dar.

Virenschutz zu Hause

IT-Angriffe konzentrieren sich besonders auf die marktführenden Systeme. Aber selbstverständlich ist grundsätzlich keine Plattform davor gefeit. Deshalb zählt ein Anti-Virenschutz seit Jahrzehnten zu den Basics. Auch für mobile Endgeräte. Der erste Computervirus für MS-DOS erschien im Jahre 1986 und hatte den Namen »Brian«. Während damals die Anzahl der Varianten noch überschaubar war, verzeichnen wir 35 Jahre später laut Lagebericht 2021 des Bundesamts für Informationssicherheit (BSI) weltweit tagtäglich bis zu 553.000 neue Schädlinge bzw. schadhafte Programme. Für den privaten Bereich stellt die auf neueren Versionen des marktführenden Betriebssystems bereits vorinstallierte und tief im System verankerte Lösung eine sehr gute Wahl dar. Grund: sie hat in den Tests mittlerweile das Niveau des »Platzhirschen« erreicht. Die Nutzung der integrierten Lösung erscheint jedoch auch noch vor einem anderen Hintergrund sinnvoll. In der Vergangenheit wurden nämlich immer wieder drastische Lücken in einigen sogenannten 3rd-party Anti-Virenschutz Paketen öffentlich. So konnten Angreifer die zusätzlich installierte Schutzanwendung dazu bringen, anstelle des eingeschleusten Schadcodes wichtige System- oder Programmdateien zu löschen. In anderen Fällen konnte man den Schutz „bei Bedarf“ relativ einfach abschalten. Fairerweise muss man aber anmerken, dass sich auch die Software des in Redmond ansässigen Unternehmens immer wieder austricksen lässt. Oder selbst durch offensichtlich nicht optimal getestete, eigens verteilte Updates für negative Schlagzeilen in puncto Schutzwirkung sorgt. Zusammenfassend gesagt bieten viele Hersteller mit ihren bereits vorinstallierten und/oder kostenfrei nutzbaren Pakten für den »Home-Use“ einen guten Schutz.

Mehr Schutz im Businessbereich

In der Geschäftswelt stehen die Zeichen etwas anders. Hier ist der Einsatz einer sogenannten Next-Generation Anti-Virenlösung/Endpoint Detection & Response anzuraten. Diese arbeitet nicht nur rein signaturbasiert, sondern vielmehr verhaltensbasiert. Heißt, alles was über die Signaturen als bösartig bekannt ist, wird auch so erkannt und blockiert. Die laufenden Prozesse (Taskmanager), Veränderungen am System (unter anderem Dateisystem und Registry), die Netzwerkkommunikation, Downloads, Systemanmeldungen werden auf Anomalien und Auffälligkeiten untersucht und je nach Einstellung entweder nur identifiziert oder sogar autonom unterbunden. Zudem besitzen solche Tools Mechanismen, um ein infiziertes System schnell und effektiv vom Netzwerk zu isolieren. Größere Schäden sind so abzuwenden.

Anwendungsprogramme richtig konfigurieren und aktuell halten

Logischerweise müssen auch die 3rd party-Anwendungen richtig konfiguriert und aktuell gehalten werden, da diese auch nicht immer »out-of-the-box« sicher konzipiert (security-by-design) respektive voreingestellt (security-by-default) sind. Nachdem die Entwickler stets auf neu entdeckte Schwachstellen mit einer Systemanpassung reagieren müssen, ist auch hier eine regelmäßige manuelle oder toolbasierte Überprüfung und Anwendung der Updates unabdingbar. Untermauern lässt sich dieser Ratschlag mit 1.000 neu aufkommenden CVEs (Common Vulnerabilities and Exposures) im Monat. Im Vergleich zu den Jahren 1999 bis 2021 wird man in diesem Jahr den bisherigen Höchstwert aus 2020 mit 18.325 Einträgen auf cvedetails.com erneut übertreffen. Greifbarer wird das, wenn man sich ein Beispiel ansieht. Im Unternehmensumfeld offenbart die von den meisten Einrichtungen genutzte zentrale E-Mail-Kommunikationsplattform schwere Sicherheitslücken. Während auf der cloud-gehosteten Variante stets zeitnah vom Hersteller die dafür vorgesehenen Softwareupdates als Software-as-a-Service gemacht wurden, blieben die selbstverwalteten On-Premise Installationen oft länger verwundbar. Etwa mangels zeitlicher oder personeller Ressourcen von Seiten der Systembetreuer vor Ort. Daher sahen wir in der jüngeren Vergangenheit schon viele Hackergruppen die ihre Angriffe gezielt auf diese Gegebenheit ausrichteten und am Ende die Systeme der betroffenen Unternehmen mit Ransomware lahmlegen konnten. BSI und BKA warnten zuletzt vor einem erhöhten Risiko von Cyberangriffen rund um Weihnachten. Gut möglich, dass dabei auch die rund 13.000 verwundbaren und extern erreichbaren Server in Deutschland mit auf der Charta standen. Ein weiteres Beispiel ist die aktuell vorherrschende Schwachstelle in log4j Version 2 – der Bibliothek zum Loggen von Anwendungsmeldungen in Java. Zwischen Bekanntwerden und krimineller Ausnutzung liegen meist nur Stunden bis wenige Tage. So hat es bereits einen Angriff auf die Webseite des Bundesfinanzhofs gegeben, welche aber erfolgreich abgewehrt werden konnte.

Das Passwort Dilemma

Ein noch immer weit verbreitetes Problem stellen die Benutzerkonten dar, weil sie zumeist noch immer nur mit einem Passwort geschützt sind. Diese sind zu simpel (zum Beispiel Zeichenreihen von der Tastatur, Wörter aus dem Wörterbuch, Name des Haustiers, etc.) und werden oftmals für mehrere Dienste gleichzeitig verwendet. Ganz zur Freude der Hacker. Sinnbildlich für dieses Dilemma ist der Blick auf das am meisten verwendete Passwort in Deutschland aus dem Jahr 2021: »123456«. Die Plätze 2 und 3 gehen an: »passwort« und »12345«. Naja. Der Worst-Case ist dann erreicht, wenn das Passwort des E-Mail Kontos öffentlich wurde. Durch Sichtung der E-Mails oder Analyse der „most commonly used services“, wie Online-Shopping oder Soziale Netzwerke, können die Passwörter zurückgesetzt und die Accounts missbräuchlich genutzt werden. Wie kann man dieses Problem also lösen? Ganz einfach. Durch Wahl eines kryptischen Passworts, dass lang ist (12 Stellen und mehr) und sich aus möglichst vielen verschiedenen Zeichen (Groß-, Kleinbuchstaben, Ziffern, Sonderzeichen) zusammensetzt. Aber auch klar: Man muss es sich merken können und keinesfalls öffentlich zugänglich notieren. Spätestens dann, wenn man dem bereits oben angerissenen Grundsatz folgt und für jeden Dienst ein neues, voneinander komplett unabhängiges „starkes“ Passwort verwendet, wird Missbrauch schwierig.

Passwortmanager

Für Unterstützung bei den Passworten gibt es sogenannte Passwortmanager. Gute Produkte sind oft kostenlos verfügbar, wie zum Beispiel KeePassXC. Der Passwortmanager dient zur sicheren Aufbewahrung von Konten und enthält meist auch die Option sich ein zufälliges Passwort generieren zu lassen. Hierzu erstellt man einmalig einen sogenannten »Tresor«, eine verschlüsselte Datei, vergibt dafür ein Masterpasswort, welches bei jedem Aufruf einzugeben und somit auch zu merken ist und legt darin alle Konten (Benutzername & Passwort) ordnungsgemäß an. Am Ende des Tages muss man sich nur noch sehr wenige Passwörter merken. Für alle anderen kann man auf die Datenbank zurückgreifen. Ein sehr nützliches Tutorial dazu bietet der Cyber Security Experte Aron Molnar an: https://www.youtube.com/watch?v=uQUtBooXJ54 und https://www.youtube.com/watch?v=o6Bk0HLPLzo.

2/MFA

Alternativ oder sogar darüber hinaus sollte man wo immer möglich die Authentifizierung über einen »zweiten Faktor« aktivieren (2/MFA). So, wie man es vom Online-Banking kennt. Die sichersten Varianten hierbei liegen in der Verwendung eines Hardware- (meist USB-Stick) oder Softwaretoken (Authenticator-App am Smartphone). Damit ist es Hackern nur durch Kenntnis des Benutzername und des Passwort-Tupels nicht möglich, auf das Konto zuzugreifen.

Nicht mit Administratorrechten arbeiten

Ein weiter bekannter Grundsatz ist es, nicht mit lokalen Administratorrechten zu arbeiten. Auch wenn die Nutzung dessen oftmals als bequem und einfach erscheint, birgt es doch enorme Risiken. Sollte man sich zum Beispiel durch Öffnen eines verseuchten E-Mail-Anhangs oder Klick auf einen Link, der einem auf eine präparierte Seite führt, unwissentlich einen Schädling auf den PC laden und diesen damit infizieren, so ist der Malware mit privilegierten Admin-Rechten logischerweise mehr möglich als unter normalen Benutzerrechten. Recht deutlich wurde das auch bei einem Cyberangriff auf die Heise-Gruppe.

Software und Daten aus sicheren Quellen nutzen

Egal, ob auf Desktop-/Server- oder mobilen Betriebssystemen gilt es Anwendungen und Apps nur aus vertrauenswürdigen Quellen zu beziehen. Also etwa den offiziellen Herstellerseiten oder App-Stores. Bei dubiosem, nicht geprüftem oder vertrauenserweckendem Ursprung besteht immer ein erhöhtes Risiko, dass man sich ein Stück unerwünschte Software auf den Endpunkt installiert, da neben der Kernfunktionalität z.B. auch sensible Daten ausgelesen und an eine nicht weiter bekannte Adresse transferiert werden. Aber auch in den offiziellen Stores sollte man Vorsicht walten lassen, da auch hierin immer wieder schadhafte Apps entdeckt und entfernt werden müssen.

Rechner/Geräte vor unberechtigtem Zugriff schützen

Ein Automatismus wie das Hände waschen sollte das Sperren des (End-)Geräts sein, wenn man es verlässt oder unbeaufsichtigt lässt. Eine Sperrung erfolgt über die Shortcuts (Windows: Windows-Taste + L; Linux: Strg + Alt + L; MacOS: Ctrl-Befehlstaste-Q). Selbiges gilt natürlich auch für mobile Endgeräte. Hier empfiehlt es sich, klassisch via 6-stelliger PIN oder Passwort zu sperren. Grundsätzlich sind alternativ auch biometrische Merkmale wie Fingerabdruck oder Gesichtsscan denkbar. Dabei muss man jedoch gegenüber den Herstellern ein gutes Stück Vertrauen mitbringen, da auch dort immer das Risiko besteht, dass sensible Daten in falsche Hände gelangen könnten.

Keine zweifelhaften E-Mails bearbeiten oder beantworten

Wie bekannt, sollte man im Umgang mit E-Mail immer vorsichtig agieren, um hier keine Fehler zu begehen. Es gilt immer genau dieselben Merkmale zu prüfen. Entspricht die Absendeadresse (nicht Anzeigename) dem Standard der Organisation von der ich eine E-Mail erwarte? Wohin führen Links tatsächlich? (wie zu erwarten: https://www.xyz.th-deg.de - oder doch z.B.: xyz.abc.hu?)? Und drittens die Form: Entspricht die E-Mail den gängigen Richtlinien? (Anrede, Inhalt, Signatur).

Sensible Informationen nicht leichtfertig preisgeben

Wie bekannt zurückhaltend im Umgang mit sensiblen Informationen sein. Dies ist im geschäftlichen Bereich ebenso gültig wie im Privaten.

Nichtbenötigte Dienste deaktivieren

Auch hier ist bekannt, dass man nicht benötige Anwendungen oder Dienste deinstallieren oder deaktivieren sollte. Hintergrund ist der, dass - sowohl das eine als auch das andere – stets sicher konfiguriert und auf dem aktuellsten Stand gehalten werden muss. Damit reduziert man Angriffsfläche und Supportaufwand.

Daten/System sichern

Gemäß dem Leitsatz „Kein Backup – kein Mitleid“ empfiehlt es sich als letzter und wichtigster Punkt regelmäßige Backups anzufertigen. Diese sollten offline sein, also nur für den Sicherungsprozess am Gerät bzw. am Netzwerk angeschlossen werden, um im Falle einer Infektion des Endgeräts nicht für den Schädling erreichbar zu sein. Bei einer Ransomware-Infektion werden frühzeitig lokale angefertigte Schattenkopien bzw. Wiederherstellungspunkte gelöscht und im Netzwerk nach Backup-Geräten gesucht, um die darauf befindlichen Daten ebenfalls unbrauchbar zu machen.

Abschließend der Tipp, all diese Regeln bestmöglich zu beachten. Es ist keine Frage des »ob« man Opfer eines Cyberattacke wird, sondern des »wann«. Und in diesem Falle hilft meist nur die Wiederherstellung eines Backups, um nicht Lösegeld bezahlen zu müssen. Was man aus Expertensicht selbstverständlich NIEMALS machen sollte. Nicht zuletzt, weil man so dieses kriminelle Geschäftsmodell unterstützt. Abschließend wünsche ich euch allen: „Stay Safe & Secure!“

Martin Oberberger

Martin Oberberger, M. Sc. ist seit Nov. 2018 an der Technischen Hochschule Deggendorf tätig. Dort ist er für den (neu gegründet & erstmals besetzten) Bereich der Informationssicherheit zuständig & unterstützt dabei Prof. Dr. Liebelt in Ihrer Rolle als Informationssicherheitsbeauftrage auf strategisch & operativer Ebene.
26.01.2022| Martin Oberberger
"""


#print(find_conditional_words(words))

print(lexical_diversity(webpage))
print(sum_word_length(webpage.split(' ')) / len(webpage.split(' ')))
print(word_freq('der', webpage))

