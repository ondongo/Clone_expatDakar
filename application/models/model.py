import hashlib
from flask_sqlalchemy import SQLAlchemy
from application.front import app
import datetime
import logging as log 

from sqlalchemy import desc
from flask_login import UserMixin, current_user

db = SQLAlchemy(app)



class Favorite(db.Model):
    __tablename__ = "favorite" 
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    annonce_id = db.Column(db.Integer, db.ForeignKey('annonces.id'))
  
# Creation des Models
class Annonce(db.Model):
    __tablename__ = "annonces" 
    # Au cas ou on change le nom de la table
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False, unique=True)
    description = db.Column(db.Text)
    prix=db.Column(db.Float(1000),nullable=True)
    categorie = db.Column(db.String(200))
    sousCategorie = db.Column(db.String(200))
    etat = db.Column(db.String(200),nullable=True)
    img_url = db.Column(db.String(255),nullable=True)
    img_title = db.Column(db.String(100))
    datePub = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    lieuPub=db.Column(db.String(200))
    published = db.Column(db.Boolean, default=True)
    deleted = db.Column(db.Boolean, default=False)
    nbreVues = db.Column(db.Integer, default=0)
    favorites = db.relationship('Favorite', backref='annonces', lazy='dynamic')
    #clé étrangère qui lie l'annonce à l'utilisateur qui l'a publié.
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    #ratings = db.relationship('Ratings', backref='annonces', lazy='dynamic')



    


# Creation du model User
class User(db.Model,UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(200), nullable=False)
    prenom  = db.Column(db.String(200), nullable=False)
    tel  = db.Column(db.String(200), nullable=False,unique=True)
    login = db.Column(db.String(200), nullable=False, unique=True)
    password = db.Column(db.String(5000), nullable=False)
    active = db.Column(db.Boolean, default=True)
    #==============-------Chaque fois que l'utilisateur publie ça compte si ça arrive à 100 passe le Vip
    NbreAnnoncePub=db.Column(db.Integer, default=0)
    favorites = db.relationship('Favorite', backref='users', lazy='dynamic')
    annonces = db.relationship('Annonce', backref='users', lazy=True)
    boutiques = db.relationship('Boutique', backref='users', lazy=True)
    restaurant = db.relationship('Restaurant', backref='users', lazy=True)
    
    #======= Pour faire le systeme d etoiles
   # ratings = db.relationship('Ratings', backref='users', lazy='dynamic')



    
    
    
    
    def __repr__(self):
        return f"<User : {self.login}>"
    
    def check_password(self, password):
        return hashlib.md5(password.encode('utf-8')).hexdigest() == self.password
    

 #constructeur
    # def __init__(self, nom, prenom, tel, email, password) :
    #     self.nom = nom
    #     self.prenom = prenom
    #     self.tel = tel
    #     self.email = email
    #     self.password = password

class Boutique(db.Model):
    __tablename__ = "boutique" 
    id = db.Column(db.Integer, primary_key=True)
    title_entreprise = db.Column(db.String(200), nullable=False, unique=True)
    description_Entreprise = db.Column(db.Text)
    prix=db.Column(db.Float(1000))
    type_boutique = db.Column(db.String(200))
    img_url = db.Column(db.String(255))
    img_title = db.Column(db.String(100))
    Directions=db.Column(db.String(200))
    adresse_postale=db.Column(db.String(200))
    Instagram_name=db.Column(db.String(200))
    Opening_hours=db.Column(db.String(200))
    published = db.Column(db.Boolean, default=True)
    deleted = db.Column(db.Boolean, default=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

class Restaurant(db.Model):
    __tablename__ = "restaurant" 
    id = db.Column(db.Integer, primary_key=True)
    Categorie_Restaurant = db.Column(db.String(200), nullable=False)
    Nom_Restaurant = db.Column(db.String(200), nullable=False, unique=True)
    description_Restaurant = db.Column(db.Text)
    img_url = db.Column(db.String(255))
    img_title = db.Column(db.String(100))
    Opening_hours=db.Column(db.String(200))
    Fermeture_hours=db.Column(db.String(200))
    
    adresse=db.Column(db.String(200))
    published = db.Column(db.Boolean, default=True)
    deleted = db.Column(db.Boolean, default=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

# class Ratings(db.Model):
#     __tablename__ = "ratings" 
#     id = db.Column(db.Integer, primary_key=True)
#     user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
#     annonce_id = db.Column(db.Integer, db.ForeignKey('annonces.id'))
  
# ----------Pas besoin
# class Commande(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
   
# class Payement(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
  


# =====================================================================
# =============================Fin Classe ==============
# =====================================================================




# =====================================================================
# =============================Requetes complexes dans back.py et front.py ==============
# =====================================================================







# ****************************************************************************
# =*****************************Debut Requetes Query Simples***********************************
# **********************************************************************


#************************************Annonces ***********************************
# ========-----Afficher tous les articles
def getAllAnnonce():
    return Annonce.query.all()

def getAllAnnonceRecent():
    return Annonce.query.order_by(desc(Annonce.datePub)).all()

#========-------Publish
#Visit
def getAllAnnoncePublier():
    return (
        Annonce.query.filter(Annonce.published == 1, Annonce.deleted == 0)
        .order_by(desc(Annonce.datePub))
        .all()
    )




#=====-----RequeteCorbeille
def getAllAnnonceDel():
    return  (
        Annonce.query.filter(Annonce.deleted == 1,Annonce.user_id==current_user.id)
        .order_by(desc(Annonce.datePub))
        .all()
    )


#========== Non---------Publish
def getAllAnnonceBrouillon():
    return (
        
        Annonce.query.filter(Annonce.published == 0, Annonce.deleted == 0,Annonce.user_id==current_user.id)
        .order_by(desc(Annonce.datePub))
        .all()
    )


#=======-------------Afficher l'article qui a cet id
def findAnnonceById(id_annonce):
    annonce = Annonce.query.get(id_annonce)
    if annonce is not None:
        annonce.nbreVues += 1
        db.session.commit()
    return annonce

# def solution(id_annonce):
#     return Annonce.query.get(id_annonce)


def getAllAnnonceA_La_Une():
    return (
            Annonce.query.order_by(desc(Annonce.nbreVues)).limit(5).all()
        )

# =====================================================================
# =====================Publier/Modifier/Supprimer==============


# def getAnnoncesByDate(date):
#     date_obj = date.strftime("%d-%m-%Y à %H:%M%:%S")
#     return Annonce.query.filter(Annonce.datePub == date_obj).all()




#============Save objet de type article====================
def saveAnnonce(annonce: Annonce):
    db.session.add(annonce)
    db.session.commit()
    
    
#============Save objet de type article====================
def addResto(resto: Restaurant):
    db.session.add(resto)
    db.session.commit()


#==============================---------Modifier Annonce

def editAnnonceModel(annonce:Annonce):
    old_annonce = Annonce.query.get(annonce.id)
    #
    old_annonce.title = annonce.title
    old_annonce.description = annonce.description
    old_annonce.published = annonce.published
    old_annonce.img_title = annonce.img_title
    old_annonce.img_url = annonce.img_url
    old_annonce.prix = annonce.prix
    old_annonce.categorie = annonce.categorie
    old_annonce.lieuPub = annonce.lieuPub
    old_annonce.etat = annonce.etat
    db.session.commit()

#==========---------Faire passer à publier

def un_published(id_annonce):
    annonce = Annonce.query.get(id_annonce)

    # Tester si c'est une publication:
    if not annonce.published:
        annonce.datePub = datetime.datetime.utcnow()

    annonce.published = not annonce.published
    db.session.commit()



#=======---------Mettre à la Corbeille=======CoteModel
def un_delete(id_annonce):
    annonce = Annonce.query.get(id_annonce)

    annonce.deleted = not annonce.deleted
    db.session.commit()

#========---------Mettre Favori
# def ajouter_favori(user_id, annonce_id):
#     favori = Favorite(user_id=user_id, annonce_id=annonce_id)
#     db.session.add(favori)
#     db.session.commit()





#************************************ USER REQUETES ***********************************

def saveUser(user: User):
    db.session.add(user)
    db.session.commit()


def ajouter_favori(favorite: Favorite):
    db.session.add(favorite)
    db.session.commit()


# =====================================================================
# ============Création de commande(Excution au lancement)==============
# ========================decorators init==============================
@app.cli.command('EldyDb')
def init_db():
    with app.app_context():
        db.drop_all()
        db.create_all()
        
        log.warning("Base de donnees actualisee")

# ==================Test---------------

#01 ========== insert 
@app.cli.command('insert-user')
def insert_user():
    user=User()
    user.nom = 'ONDONGO'
    user.prenom = 'PrinceDeGloire'
    user.tel = '771592145'
    user.login = 'gloireondongo1205@gmail.com'
    user.password = '1234'
    
# ============save
    
    
    user3 = User(
        nom="Eldy",
        prenom="ODG",
        tel="78555555",
        login="Eldy@yahoo.com",
        password="171295"
    )
    # db.session.add(user3)
    db.session.add_all([user,user3])
    db.session.commit()
    log.warning(f"{user} est bien inséré")
    log.warning(f"{user3} est bien inséré")


#02 ========== select =======
@app.cli.command('select-all-user')
def selectAll_user():
    users=User.query.all()
    print(users)
    
#03 ========== select-where =======
@app.cli.command('selectby-user')
def selectwhere_user():
    userby=User.query.filter(login="gloireondongo1205@gmail.com").all()
    
    print(userby)
    
#03 ========== select-like =======
@app.cli.command('selectlike-user')
def selectLike_user():
    userbyLike=User.query.filter(User.login.like('%g%')).all()
    
    print(userbyLike)
    






        
























