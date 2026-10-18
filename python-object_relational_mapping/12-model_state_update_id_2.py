#!/usr/init/python3
#!/usr/bin/env python3
"""
Script qui change le nom de l'état dont l'id est 2
en "New Mexico" dans la base de données hbtn_0e_6_usa.
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

    # Construction de l'URL de connexion pour SQLAlchemy
    db_url = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        username, password, db_name
    )

    # Initialisation du moteur SQLAlchemy
    engine = create_engine(db_url, pool_pre_ping=True)

    # Création d'une session configurée
    Session = sessionmaker(bind=engine)
    session = Session()

    # Recherche de l'état dont l'id est 2
    state_to_update = session.query(State).filter_by(id=2).first()

    if state_to_update:
        state_to_update.name = "New Mexico"
        session.commit()

    # Fermeture de la session
    session.close()
