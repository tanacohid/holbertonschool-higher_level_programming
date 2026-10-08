#!/usr/bin/python3
"""
Module pour consommer et traiter des données issues de l'API JSONPlaceholder.
"""
import csv
import requests


def fetch_and_print_posts():
    """
    Récupère tous les articles depuis JSONPlaceholder,
    affiche le code de statut HTTP et le titre de chaque article.
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    print("Status Code: {}".format(response.status_code))

    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post.get("title"))


def fetch_and_save_posts():
    """
    Récupère tous les articles depuis JSONPlaceholder
    et enregistre id, title et body dans un fichier CSV nommé posts.csv.
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    if response.status_code == 200:
        posts = response.json()

        # Structuration des données sous forme de liste de dictionnaires
        data_to_save = [
            {
                "id": post.get("id"),
                "title": post.get("title"),
                "body": post.get("body")
            }
            for post in posts
        ]

        # Nom du fichier de destination et définition des colonnes
        filename = "posts.csv"
        fieldnames = ["id", "title", "body"]

        # Écriture dans le fichier CSV
        with open(filename, mode="w", encoding="utf-8", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data_to_save)
