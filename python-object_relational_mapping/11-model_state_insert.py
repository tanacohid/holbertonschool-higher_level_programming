#!/usr/bin/python3
"""
Script qui ajoute l'objet State "Louisiana" à la base de données hbtn_0e_6_usa.
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Récupération des arguments de la ligne de commande
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Création de l'URL de connexion pour MySQL
    db_url = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        username, password, db_name
    )

    # Initialisation du moteur SQLAlchemy
    engine = create_engine(db_url, pool_pre_ping=True)

    # Création d'une session configurée
    Session = sessionmaker(bind=engine)
    session = Session()

    # Création et ajout du nouvel état "Louisiana"
    new_state = State(name="Louisiana")
    session.add(new_state)
    session.commit()

    # Affichage de l'ID généré pour le nouvel état
    print(new_state.id)

    # Fermeture de la session
    session.close()
