(presentation)=

# Présentation du projet

## 1. Objectifs du projet (Problématique)

Le projet consiste en le développement d'une application mobile permettant la planification des devoirs et des examens. L'objectif principal est d'aider les enseignants et les élèves à mieux gérer la charge de travail scolaire.

Actuellement, il est difficile pour les enseignants d'avoir une vue d'ensemble sur les devoirs et les évaluations donnés dans les autres matières, ce qui peut entraîner une surcharge de travail à certaines périodes. De même, les élèves n'ont pas toujours une vision claire du temps à consacrer à chaque devoir ou à la révision des examens.

L'application permettrait donc de :

- répartir plus équitablement les devoirs et les examens
- estimer le temps de travail total quotidien ou hebdomadaire
- fournir des statistiques sur la charge de travail par matière et par période de l'année, ainsi que sur la précision des estimations des enseignants
- faciliter le suivi pour les élèves absents

## 2. Utilisateurs et rôles

Les utilisateurs visés sont les enseignants et les élèves du Collège du Sud. À terme, l'application pourrait être étendue à plusieurs établissements scolaires.

L'application distingue deux rôles principaux : enseignant et élève.

### 2.1 Enseignant

Il peut consulter et ajouter des devoirs et des examens, estimer le temps de travail et consulter des statistiques globales.

### 2.2 Élève

Il peut consulter et ajouter des devoirs et des examens qui le concernent et renseigner le temps réellement consacré au travail. Il peut également consulter des statistiques globales.

## 3. Fonctionnalités principales et pages de l'application

### 3.1 Page d'inscription

Lors de l'inscription, l'utilisateur choisit son rôle : élève ou enseignant.

L'élève renseigne les informations le concernant (nom, prénom, classe, niveau de mathématiques, langue 1, langue 2, langue 3, OS, OC, basic English et bilinguisme).

L'enseignant renseigne également les informations le concernant (nom, prénom, branche(s) enseignée(s), classe(s) pour les branches de base, ainsi que, le cas échéant, OS, OC, basic English et bilinguisme).

Dans tous les cas, l'utilisateur inscrit son adresse email et un mot de passe.

### 3.2 Page de connexion

Les utilisateurs se connectent à leur compte via cette page.

Un bouton « Rester connecté » est envisagé afin de faciliter les connexions ultérieures. En cas d'oubli du mot de passe, l'utilisateur peut le réinitialiser en cliquant sur « Mot de passe oublié ? ». Cette fonctionnalité constitue une extension potentielle du projet.

### 3.3 Page d'accueil

Page de bienvenue présentant le but général de l'application et permettant d'accéder aux différentes fonctionnalités.

Un soin particulier sera apporté à la clarté et à l'aspect visuel de cette page.

### 3.4 Page de calendrier

Cette page affiche les devoirs et les examens sous la forme d'un calendrier.

La charge de travail quotidienne ou hebdomadaire pourra y être indiquée à l'aide d'un indicateur visuel (par exemple une jauge).

### 3.5 Formulaire d'ajout de devoir ou d'examen

Cette page permet aux utilisateurs autorisés d'ajouter un devoir ou un examen à l'aide d'un formulaire adapté au type d'événement sélectionné.

### 3.6 Page de profil

Les utilisateurs peuvent consulter et modifier les informations les concernant. La modification de ces informations constitue une extension du projet.

### 3.7 Page de statistiques (Optionnelle)

Cette page affiche différentes statistiques sous forme de graphiques concernant la charge de travail, les devoirs et les examens.

## 4. Gestion des devoirs

L'application permet aux enseignants ou aux élèves de noter les devoirs à effectuer. Les enseignants peuvent ainsi mieux répartir la charge de travail entre les jours et les matières.

Les enseignants et les élèves pourront y renseigner :

- le titre
- la branche concernée
- la description
- la date de rendu
- une estimation du temps nécessaire, annoncé en classe par l'enseignant ou noté par celui-ci directement dans l'application
- le temps réel consacré, renseigné par l'élève

Les devoirs liés aux options spécifiques (maths renforcées ou standards, langue 3, OS, OC, basic English ou branches en allemand pour les élèves bilingues) ne sont accessibles qu'aux élèves concernés, tous les élèves d'une même classe n'ayant pas nécessairement les mêmes options.

Une jauge de charge indique aux enseignants le niveau d'occupation des élèves, afin d'éviter de dépasser un certain seuil (par exemple trois heures de travail par jour). Le temps de révision des examens est également pris en compte dans ce calcul.

Cette fonctionnalité est aussi utile pour :

- les élèves absents, qui peuvent consulter les devoirs manqués
- la centralisation de la saisie des devoirs (une seule personne les entre, les autres peuvent les consulter)

## 5. Gestion des examens

Si le temps le permet, l'application proposera également la planification des examens dans le même calendrier que les devoirs.

Lors de l'ajout d'un événement, il suffira d'indiquer s'il s'agit d'un devoir ou d'un examen afin d'afficher les champs correspondants.

Les enseignants et les élèves pourront y renseigner :

- le titre
- la branche concernée
- la description
- le temps de révision estimé
- le temps réel consacré aux révisions, renseigné par l'élève

Ils pourront ainsi visualiser les autres examens prévus durant la même période et éviter une concentration excessive d'évaluations. Le temps de révision sera automatiquement réparti sur les jours précédant l'examen et ajouté à la charge de travail quotidienne.

## 6. Statistiques et analyses (Optionnel)

L'application pourra générer différentes statistiques, notamment :

- les périodes les plus chargées en devoirs et en évaluations
- la répartition des devoirs et des examens entre les matières et les semaines

Des statistiques spécifiques seront également disponibles pour chaque enseignant :

- précision des estimations du temps de travail (comparaison entre temps estimé et temps réel renseigné par les élèves)
- volume de devoirs et d'examens donnés par rapport aux autres enseignants
- périodes de l'année où la charge de travail est la plus élevée

## 7. Aspects techniques et organisationnels

Il serait souhaitable de demander au recteur l'accès à la base de données contenant la liste des élèves et des enseignants, afin d'utiliser des données réelles.

Cela permettrait de rendre l'application directement exploitable dans un cadre scolaire, sans devoir créer une base de données fictive.

Il conviendrait également d'estimer :

- le nombre d'utilisateurs
- les moments de la journée où l'application serait la plus utilisée

Une version web (application accessible en ligne) pourrait être envisagée.

Concernant la sécurité et la confidentialité, les données personnelles des utilisateurs seraient stockées de manière sécurisée et ne seraient accessibles qu'aux personnes autorisées, conformément aux usages en milieu scolaire.

## 8. Questions

1. Quel(s) outil(s) utiliser ? → NiceGUI.
2. Les élèves d'une même classe n'ayant pas tous les mêmes options (OS, OC, etc.), certains peuvent avoir une charge de travail plus importante que d'autres. Comment prendre cette différence en compte ?
3. Comment quantifier les données (estimation du temps de travail ou du temps de révision, par exemple) ?

## 9. Extensions possibles

### 9.1 Version moyenne

- modification des informations personnelles
- graphiques générés à partir des statistiques

### 9.2 Version maximale

- réinitialisation du mot de passe
- notifications automatiques (rappels de devoirs ou d'examens proches)

