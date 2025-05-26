
#### Module = eq package ; __init__ permet de prendre un dossier comme un module
#### typage faible = python (le contenant peut changer de contenu a tout moment) ; typage fort ex java
#### interprete python ; java compile
#### mots cle reserve = def, class etcccc
#### tout est objet = on  manipule que des objects caches derriere
#### Comment definir def class et autres

#### Declaration class premiere lettre = Majuscule
#### variable en minuscule
#### Constante tout Majuscule
### Norme pep 8
##### Diff Fonction et methode / Methode appartient a la class / Fonction libre

### methoe start, methode pause
### OBJET = MANIF CASS
class Cours:
    def __init__(self,name,heure):
        self.name = name
        self.heure = heure

    def start(self):
        print("Le cours d'",self.name, "de", self.heure,"finalement demarré")
        
    def pause(self):
        print("Coffee Break")

new_cours = Cours("Espagnol","2h")
new_cours.start()
