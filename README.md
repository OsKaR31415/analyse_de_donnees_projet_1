


# Structure du projet

Pour générer le fichier html contenant le rapport, lancer `quarto render report.qmd` ou simplement `make report`

 - `report.qmd` contient le texte du rapport et sa structure
 - `report.ipynb` est un notebook contenant le code du projet
     - **Attention :** ne pas modifier le fichier `report.py`, qui est auto-généré (et donc écrasé) à chaque render
 - `_quarto.yml` est un fichier de configuration (pour le rendu et l'affichage du rapport)
 - En relation avec le code :
     - le dossier `DATA/` contient les données (au format CSV) utilisées dans le projet
     - `requirements.txt` contient la liste des modules python nécessaires pour exécuter le projet
 - Fichiers de rendu (non synchronisés par git) (générés automatiquement)
     - `report.html` contient le rapport
     - `report.out.ipynb` contient le résultat de l'exécution de `report.ipynb`
     - `report-preview.html` est une page affichant le notebook `report.ipynb` (ou plutôt, sa version exécutée)
     - `report_files/` contient des fichiers servant à l'affichage du rapport (librairies, frameworks...)


En résumé :
 - pour éditer le rapport : `report.qmd`
 - pour éditer le code : `report.ipynb`
 - les données sont dans le dossier `DATA/`
 - `_quarto.yml` pour la configuration
 - `requirements.txt` pour les modules python
 - le résultat est dans `report.html`
