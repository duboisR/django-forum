# django-forum

Un mini-projet pour apprendre les bases en Django.

Plugins:
- [django](https://www.djangoproject.com/)
- [django-webpack-loader](https://github.com/django-webpack/django-webpack-loader)


## Développement Pipenv

Pour lancer le projet localement sur votre machine de développement:

```sh
$ pipenv shell
$ ./manage.py runserver
```

Vérifier que le projet se lance bien sur [http://localhost:8000/](http://localhost:8000/)


### Environnement avec pipenv

Pour installer pipenv, il vous suffit de suivre la [documentation](https://pypi.org/project/pipenv/). Ou bien simplement de lancer la commande suivante
```sh
pip install --user pipenv
```

Il faut ensuite se mettre dans le dossier qui contient le fichier `Pipfile` (dans notre cas le dossier `app`)

Installer l'environnement :
```sh
$ pipenv install
```

Installer les packages utiles au debug :
```sh
$ pipenv install --dev
```

Lorsqu'on veut installer un nouveau paquet, ne pas utiliser `pip install` mais `pipenv install`, cela l'ajoutera automatiquement au fichier `Pipfile`.

Utiliser l'environnement :

```sh
$ pipenv shell
```

Maintenant on peut lancer toutes les commandes `migrate.py`


### Première utilisation

Lors de la première utilisation, ne pas oublier de lancer la première migration.

```sh
$ ./manage.py migrate
```

Il faudra ensuite lancer le build du thème afin de pouvoir accéder à la plateforme.
En cas de problèmes, vous pouvez vous référer à la section **Modification du thème/ReactJs**.

```sh
$ cd app/assets
$ npm install
$ npm run build
```

### Création d'un compte super-utilisateur

Pour créer un compte super-utilisateur:

```sh
$ ./manage.py createsuperuser
```


## Développement Docker

Pour lancer le projet localement sur votre machine de développement:

```sh
$ docker-compose up -d --build
```

Vérifier que le projet se lance bien sur [http://localhost:8000/](http://localhost:8000/)


### Environnement avec pipenv

Pour installer docker, il vous suffit de suivre la [documentation](https://docs.docker.com/engine/install/ubuntu/).
Pour installer docker-compose, il vous suffit de suivre la [documentation](https://docs.docker.com/compose/install/).


### Première utilisation

Lors de la première utilisation, ne pas oublier de lancer la première migration.

```sh
$ docker-compose exec web ./manage.py migrate
```

Il faudra ensuite lancer le build du thème afin de pouvoir accéder à la plateforme.
En cas de problèmes, vous pouvez vous référer à la section **Modification du thème/ReactJs**.

```sh
$ cd app/assets
$ npm run build
```


### Création d'un compte super utilisateur

Pour créer un compte super utilisateur:

```sh
$ docker-compose exec web ./manage.py createsuperuser
```

Il vous suffit ensuite de vous connecter à la [page d'administration Django](http://localhost:8000/admin/) avec les identifiants que vous avez renseigné.



## Modification du thème/ReactJs

Nous utilisons Webpack pour concaténer/minifier/bunble nos fichiers JS + SCSS.

Version NVM / NPM
```
$ nvm list
    [...]
->      v15.3.0
default -> node (-> v15.3.0)
node -> stable (-> v15.3.0) (default)
stable -> 15.3 (-> v15.3.0) (default)
[...]

$ npm --version
7.0.14
```

Pour lancer le watcher de webpack
```sh
$ cd app/assets
$ npm install
$ npm run watch
```

Pour faire un build pour la mise en prod
```sh
$ cd app/assets
$ npm run build
```


## Mail

Pour le developpement, nous redirigons tous nos emails sur une boïte mail [mailinator](https://www.mailinator.com/v3/index.jsp?zone=public&query=readmeastory#/#inboxpane)
Pour ce faire, vous pouvez suivre l'article Medium [Django et E-mail](https://medium.com/@duboisr/django-et-e-mail-eb9d9ac4503e)



## Projet

Ce mini-projet a été mis en place pour vous permettre de découvrir/apprendre/perfectionner les bases en Django.
Le design des pages se basera sur un thème Bootstrap trouver sur [bootdey](https://www.bootdey.com/snippets/view/bs4-forum).
On utilise aussi un bout de code fourni sur [stackoverflow](https://stackoverflow.com/a/41406599) pour l'avatar de la page profile.

Pour aller plus vite, l'ensemble des templates sera déjà disponible dans l'app Django `main`.

Pour ce projet, je vais vous demander de créer un forum qui sera composé:
- D'une partie "compte utilisateur"
    - L'app Django `user`, le modèle et l'admin sont déja fournis.
    - Une page de login. Vous retrouverez le design de la page [ici](http://localhost:8000/main/login) en vous inspirant de cet [article](https://learndjango.com/tutorials/django-login-and-logout-tutorial)
    - Une page de création de compte. Vous retrouverez le design de la page [ici](http://localhost:8000/main/register) en vous inspirant de cet [article](https://learndjango.com/tutorials/django-signup-tutorial)
    - Des pages destinées au reset de mdp (avec envoi d'un mail). Vous retrouverez le design des pages en vous inspirant de cet [article](https://learndjango.com/tutorials/django-password-reset-tutorial):
        - [reset_pwd_form](http://localhost:8000/main/reset_pwd_form/)
        - [reset_pwd_done](http://localhost:8000/main/reset_pwd_done/)
        - [reset_pwd_confirm](http://localhost:8000/main/reset_pwd_confirm/)
        - [reset_pwd_complete](http://localhost:8000/main/reset_pwd_complete/)
    - D'un page profile pour mettre à jour les données du compte utilisateur. Vous retrouverez le design de la page [ici](http://localhost:8000/main/profil/)
- D'une partie "forum"
    - Une page listant tous les sujets (Topics) créés. Ces derniers pourront être filtrés sur leur titre, leur statut et s'ils ont déjà eu des réponses. Vous retrouverez le design de la page [ici](http://localhost:8000/main/topics)
    - Une page pour permettre la création d'un nouveau sujet. Attention, seuls les utilisateurs ayant un compte peuvent créer un nouveau sujet. Vous retrouverez le design de la page [ici](http://localhost:8000/main/topics/new)
    - Une page pour répondre au sujet sélectionné. Attention, seuls les utilisateurs ayant un compte peuvent répondre, les autres ont un accès en lecture seul. De plus, si l'utilisateur connecté est le créateur du sujet, il doit y avoir un bouton permettre de clôturer le sujet. Vous retrouverez le design de la page [ici](http://localhost:8000/main/topics/topic_pk/)
Toutes ces pages sont disponibles sur la [homepage](http://localhost:8000/) du projet.

Ce projet est commun à tous les sujets ci-dessous.


### Sujet 1: Créer un forum en Django (sans utiliser les classBasedViews)
Pour ce sujet, il suffit simplement de créer le forum sans utiliser les [classBasedViews](https://docs.djangoproject.com/fr/3.1/topics/class-based-views/).


### Sujet 2: Créer un forum en Django (avec les classBasedViews)
Pour ce sujet, il suffit simplement de recréer le forum en utilisant les [classBasedViews](https://docs.djangoproject.com/fr/3.1/topics/class-based-views/).
Vous pouvez consulter l'article suivant pour vous aider:
- [Django Doc](https://ccbv.co.uk/)

### Sujet 3: Créer un forum en Django Rest API + ReactJs
Pour ce sujet, il faut créer une simple page app en ReactJs ainsi que de mettre en place un API REST pour communiquer avec la BDD. Pour cela, il faut utiliser le [Django REST framework](https://www.django-rest-framework.org/). Concernant la réalisation de l'application ReactJs, cette dernière se fera dans le dossier `app/assets/src/forum/`. L'ensemble des outils permettant l'intégration de l'app ReactJS dans un projet Django aura déjà été configuré.
Vous retrouverez un exemple d'integration d'un composant ReactJs dans une view Django [ici](http://localhost:8000/main/react/).
Vous pouvez consulter les articles suivants pour vous aider:
- [ReactJs](https://openclassrooms.com/fr/courses/7008001-debutez-avec-react)
- [Django REST](https://www.django-rest-framework.org/tutorial/quickstart/)
- [Django REST Doc](https://www.cdrf.co/3.12/rest_framework.generics/RetrieveAPIView.html#get_object)

### Sujet 4: Créer un forum en Django Rest API + Flutter
Pour ce sujet, il faut créer une application mobile en Flutter ainsi que de mettre en place un API REST pour communiquer avec la BDD. Pour cela, il faut utiliser le [Django REST framework](https://www.django-rest-framework.org/). Concernant la réalisation de l'application ReactJs, cette dernière se fera dans le dossier `mobile/`.

Pour lancer l'application mobile, il vous suffit de faire la commande `flutter run` dans le dossier `mobile/` après avoir lancé un émulateur Android/Ios.
