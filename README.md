# Blog Personnel

Ce projet est un blog personnel développé avec Django. Il permet de publier des articles, de les catégoriser et de gérer les commentaires des utilisateurs.

## Fonctionnalités

- **Publication d'articles** : Ajoutez, modifiez et supprimez des articles.
- **Catégorisation** : Associez des catégories aux articles pour une meilleure organisation.
- **Commentaires** : Les utilisateurs peuvent laisser des commentaires sur les articles.
- **Interface utilisateur** : Une interface simple et intuitive pour naviguer entre les articles et les catégories.

## Prérequis

- Python 3.x
- Django 3.x ou supérieur
- virtualenv (recommandé)

## Installation

1. **Cloner le dépôt** :
   ```bash
   git clone https://github.com/votre_utilisateur/blog-personnel.git
   cd blog-personnel
   ```

2. **Creer l'environnement virtuel**
   ```bash
   virtualenv blog_env
   ```
   
3. **Activer l'environnement virtuel**
    Sur Windows :
   ```cmd
   env\Scripts\activate
   ```

   Sur macOS et Linux :
   ```bash
   source env/bin/activate
   ```

4. **Installer les dépendances**
   ```bash
   pip install -r requirements.txt
   ```

5. **Appliquer les migrations**
    ```bash
    python manage.py migrate
    ```
6. **Créer un superutilisateur**
    ```bash
    python manage.py createsuperuser
    ```
   
7. **Lancer le serveur de développement**
    ```bash
    python manage.py runserver
    ```
   
8. **Accéder au blog**

Ouvrez votre navigateur et allez à l'adresse `http://127.0.0.1:8000/`.

## Utilisation
* Admin Django : Accédez à l'interface d'administration à l'adresse `http://127.0.0.1:8000/admin/` pour gérer les articles, les catégories et les commentaires.
* Ajouter un article : Connectez-vous à l'interface d'administration et ajoutez un nouvel article via le menu "Articles".
* Ajouter une catégorie : Ajoutez une nouvelle catégorie via le menu "Catégories".
* Ajouter un commentaire : Les utilisateurs peuvent ajouter des commentaires directement sur la page de chaque article.

## Structure du projet

```tee
blog-personnel/
    manage.py
    blog/
        __init__.py
        settings.py
        urls.py
        asgi.py
        wsgi.py
    articles/
        __init__.py
        admin.py
        apps.py
        migrations/
            __init__.py
        models.py
        tests.py
        views.py
        templates/
            articles/
                liste_articles.html
                detail_article.html
        urls.py
    templates/
        base.html
    static/
    requirements.txt
    README.md
```

## Contribution
Les contributions sont les bienvenues ! Pour contribuer :
* Fork le dépôt.
* Créez une branche pour votre fonctionnalité (`git checkout -b feature/nouvelle-fonctionnalite`). 
* Commit vos modifications (`git commit -am 'Ajout d'une nouvelle fonctionnalité'`).
* Push la branche (`git push origin feature/nouvelle-fonctionnalite`). 
* Ouvrez une Pull Request.

## Licence

Ce projet est sous licence MIT. Voir le fichier LICENSE pour plus de détails.