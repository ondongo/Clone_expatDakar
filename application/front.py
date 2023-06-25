
from flask import Flask, render_template,redirect,url_for,request
from sqlalchemy import desc
from application.models.EnumEtatArticle import *
from application.models.EnumCategorie import *
from application.models.SousCategorie import *



#from .routes import main 
# from . import fakes_data
# from .fakes_data import getAllArticles, findArticleById


from flask_paginate import Pagination, get_page_parameter

#----------Fichier Principal-------------
app =Flask(__name__)

# Montrer a flask la ou se trouve notre fichier de config Flask
# app.config.from_object("config"))
# Pagination des pages
# pagination = Pagination(app)


# CREATION DE FILTER <<============================================>>

# --------------Creation Route--------------------
# Une fonction et Route en meme temps

app.config.from_object("config")
socketio = SocketIO(
    app,
   
    mode='r',
   
)


from application.models.model import (
     Message, User, findAnnonceById,Annonce,getAllAnnoncePublier,getAllAnnonceA_La_Une,Restaurant)

listcategories=list(EnumCategorie)
listEtats=list(EnumEtatArticle)
sous_categories=[]
listesVehicules =list(SousCategorieVehicule)
icons = {
        'restauration': 'fas fa-utensils',
        'Vehicules': 'fas fa-car',
        'Multimedia': 'fas fa-computer',
        'Immobilier': 'fas fa-house-chimney-window',
        'Sport_Loisirs_Voyages':'fas fa-basketball',
        'Services':'fas fa-users-gear',
        'Offres_Emploi':'fas fa-briefcase',
        'Mode_Beaute':'fas fa-glasses',
        'Equipements':'fa-solid fa-screwdriver-wrench',
        'Maison':'fas fa-house',
        'Demande_Emploi':'fas fa-handshake',
        'Animaux':'fas fa-paw',
        'AgroAlimentaire':'fas fa-truck-pickup'
        
    } 

rEnum=EnumCategorie

@app.template_filter("full_date")
def dslfsdlfjlsd(date):
    return date.strftime("%d/%m/%Y à %H:%M:%S")



# ===================================================================
# =============================Test Api de Google Pour la gestion des lieux  =========================================
# =====================================================================

# remplacer 'API_KEY' par votre clé API Google Maps
# api_key = 'API_KEY'

# # remplacer les coordonnées ci-dessous par celles de votre lieu de publication
# lat = 48.8534
# lng = 2.3488

# url = f'https://maps.googleapis.com/maps/api/geocode/json?latlng={lat},{lng}&key={api_key}'
# response = requests.get(url)

# if response.status_code == 200:
#     result = response.json()
#     if result['status'] == 'OK':
#         place_name = result['results'][0]['formatted_address']
#         print(place_name)
#     else:
#         print(result['status'])
# else:
#     print('Error:', response.status_code)




@app.route("/")
def index():
    # app.config['APP_NAME']="gloire"
    # print(app.config)
    return redirect(url_for(" test15"))

# def recuperationTel(id_annonce):
#      # Récupérer l'annonce correspondante à l'id_annonce fourni
#     annonce = Annonce.query.filter(Annonce.id==id_annonce).first()
#     # annonce = Annonce.query.get(id_annonce)

#     # Récupérer l'utilisateur correspondant à l'annonce
#     user = User.query.get(annonce.user_id).first()
#     return user.tel

    
@app.route("/Annonce50")
def test15():
     return render_template("/pages/indexEldy.html"),
     


@app.route("/Annonce")
def annonceAll():
    annonces = getAllAnnoncePublier()
    count = len(annonces)
    page = request.args.get(get_page_parameter(), type=int, default=1)
    NbreElementParPage = 2
    offset = (page - 1) * NbreElementParPage
    pagination = Pagination(page=page, per_page=NbreElementParPage, total=count)
    annonces = annonces[offset: offset + NbreElementParPage]
    
    # liste pour stocker les numéros de téléphone
    # stocker les numéros de téléphone par utilisateur
    

    # Boucle sur chaque annonce pour récupérer le numéro de téléphone de son auteur    
    #Bof Mon many to one m a gere ca   
            
    return render_template("/pages/index.html",
                           annonces=annonces,
                           listcategories=listcategories,
                           icons=icons,
                           count=count,
                           pagination=pagination,
                           sous_categories=sous_categories)






@app.route("/Annonce_A_La_Une")
def annonceA_la_une():
    annonces = getAllAnnonceA_La_Une()
   
    count =len(annonces)
    page = request.args.get(get_page_parameter(), type=int, default=1)
    NbreElementParPage = 2
    offset = (page - 1) * NbreElementParPage
    pagination = Pagination(page=page, per_page=NbreElementParPage, total=len(annonces))
    annonces = annonces[offset: offset + NbreElementParPage]
    
    return render_template("/pages/accueil.html",annonces=annonces,listcategories=listcategories,icons=icons,count=count,pagination=pagination)






# =====================================================================
# =============================Lien Nav Bleu===========================
# =====================================================================

#==============01
@app.route('/Annonce/Immobilier')
def Immobilier_articles():
    annonces = Annonce.query.filter_by(categorie=EnumCategorie.Immobilier.name).all()
    count =len(annonces)
    page = request.args.get(get_page_parameter(), type=int, default=1)
    NbreElementParPage = 2
    offset = (page - 1) * NbreElementParPage
    pagination = Pagination(page=page, per_page=NbreElementParPage, total=len(annonces))
    annonces = annonces[offset: offset + NbreElementParPage]
    sous_categories = SousCategorieImmobilier.__members__.values()
    return render_template("/pages/index.html",annonces=annonces,listcategories=listcategories,icons=icons,count=count,rEnum=rEnum.Immobilier.name,pagination=pagination,sous_categories=sous_categories)

#==============02
@app.route('/Annonce/Equipements')
def Equipements_articles():
    annonces = Annonce.query.filter_by(categorie=EnumCategorie.Equipements.name).all()
    count =len(annonces)
    page = request.args.get(get_page_parameter(), type=int, default=1)
    NbreElementParPage = 2
    offset = (page - 1) * NbreElementParPage
    pagination = Pagination(page=page, per_page=NbreElementParPage, total=len(annonces))
    annonces = annonces[offset: offset + NbreElementParPage]
    sous_categories = SousCategorieMateriaux.__members__.values()
    return render_template("/pages/index.html",annonces=annonces,listcategories=listcategories,icons=icons,count=count,rEnum=rEnum.Equipements.name,pagination=pagination,sous_categories=sous_categories)
#==============03

@app.route('/Annonce/Vehicules')
def Vehicules_articles():
    sous_categories = SousCategorieVehicule.__members__.values()
    return render_template("/pages/vehicules.html",sous_categories=sous_categories)

#==============04
@app.route('/Annonce/Maison')
def Maison_articles():
    annonces = Annonce.query.filter_by(categorie=EnumCategorie.Maison.name).all()
    count =len(annonces)
    page = request.args.get(get_page_parameter(), type=int, default=1)
    NbreElementParPage = 2
    offset = (page - 1) * NbreElementParPage
    pagination = Pagination(page=page, per_page=NbreElementParPage, total=len(annonces))
    annonces = annonces[offset: offset + NbreElementParPage]
    sous_categories = SousCategorieMaison.__members__.values()
    return render_template("/pages/index.html",annonces=annonces,listcategories=listcategories,icons=icons,count=count,rEnum=rEnum.Maison.name,pagination=pagination,sous_categories=sous_categories)

#==============05
@app.route('/Annonce/Multimédia')
def Multimédia_articles():
    annonces = Annonce.query.filter_by(categorie=EnumCategorie.Multimedia.name).all()
    count =len(annonces)
    page = request.args.get(get_page_parameter(), type=int, default=1)
    NbreElementParPage = 2
    offset = (page - 1) * NbreElementParPage
    pagination = Pagination(page=page, per_page=NbreElementParPage, total=len(annonces))
    annonces = annonces[offset: offset + NbreElementParPage]
    
    sous_categories = SousCategorieMultimedia.__members__.values()
    
    return render_template("/pages/index.html",annonces=annonces,listcategories=listcategories,icons=icons,count=count,rEnum=rEnum.Multimedia.name,pagination=pagination,sous_categories=sous_categories)

#==============06
@app.route('/Annonce/OffresEmploi')
def Demande_Emploi_articles():
    annonces = Annonce.query.filter_by(categorie=EnumCategorie.Demande_Emploi.name).all()
    count =len(annonces)
    
    page = request.args.get(get_page_parameter(), type=int, default=1)
    NbreElementParPage = 2
    offset = (page - 1) * NbreElementParPage
    pagination = Pagination(page=page, per_page=NbreElementParPage, total=len(annonces))
    annonces = annonces[offset: offset + NbreElementParPage]
    sous_categories = SousCategorieOffreEmploi.__members__.values()
    return render_template("/pages/index.html",annonces=annonces,listcategories=listcategories,icons=icons,count=count,rEnum=rEnum.Offres_Emploi.name,pagination=pagination,sous_categories=sous_categories)

#==============07

#==============08


# =============================Fin Lien Nav Bleu===========================



# =====================================================================
# ============--------------Recherche Annonces-----------==============
# =====================================================================

# =====================Search-----Categorie
@app.route('/Ann')
def articles_par_categorie():
    categorie = request.args.get('categorie')
    
    if categorie is None:
        # Si la catégorie n'est pas spécifiée, afficher toutes les annonces
        annonces = Annonce.query.all()
        count =len(annonces)
    else:
        # Si la catégorie est spécifiée, filtrer par catégorie
        annonces = Annonce.query.filter_by(categorie=categorie).all()
        # count =Annonce.query.filter_by(categorie=categorie).count()
        count=len(annonces) 
    page = request.args.get(get_page_parameter(), type=int, default=1)
    NbreElementParPage = 2
    offset = (page - 1) * NbreElementParPage
    pagination = Pagination(page=page, per_page=NbreElementParPage, total=len(annonces))
    annonces = annonces[offset: offset + NbreElementParPage]
        
    
  
    return render_template("/pages/index.html",annonces=annonces,listcategories=listcategories,icons=icons,count=count,rEnum=categorie,pagination=pagination)




@app.route('/AnnSousCategorie')
def articles_par_sous_categorie():
    categor = request.args.get('categor')
    souscategor = request.args.get('souscategor')
    
    if categor is None:
        # =====================Si la catégorie n'est pas spécifiée, afficher toutes les annonces
        annonces = Annonce.query.all()
        count =len(annonces)
    else:
        # =================Si la catégorie est spécifiée, filtrer par catégorie
        annonces = Annonce.query.filter_by(categorie=categor,sousCategorie=souscategor).all()
        # count =Annonce.query.filter_by(categorie=categorie).count()
        count=len(annonces) 
    page = request.args.get(get_page_parameter(), type=int, default=1)
    NbreElementParPage = 2
    offset = (page - 1) * NbreElementParPage
    pagination = Pagination(page=page, per_page=NbreElementParPage, total=len(annonces))
    annonces = annonces[offset: offset + NbreElementParPage]
        
    
    return render_template("/pages/index.html",annonces=annonces,listcategories=listcategories,icons=icons,count=count,pagination=pagination)



# =====================Search-----Lieu
@app.route('/Ann_lieu')
def articles_par_lieu():
    lieu = request.args.get('lieu')
    
    if lieu is None:
        # Si la catégorie n'est pas spécifiée, afficher toutes les annonces
        annonces = Annonce.query.all()
        count =len(annonces)
    else:
        # Si la catégorie est spécifiée, filtrer par catégorie
        annonces = Annonce.query.filter_by(lieuPub=lieu).all()
        count_lieu =Annonce.query.filter_by(lieuPub=lieu).count()
    page = request.args.get(get_page_parameter(), type=int, default=1)
    NbreElementParPage = 2
    offset = (page - 1) * NbreElementParPage
    pagination = Pagination(page=page, per_page=NbreElementParPage, total=len(annonces))
    annonces = annonces[offset: offset + NbreElementParPage]
        
    
    return render_template("/pages/index.html",annonces=annonces,listcategories=listcategories,icons=icons,count_lieu=count_lieu,pagination=pagination)


# =====================Search-----Lieu
@app.route('/Ann_Prix')
def annonces_par_Prix():
    prixmaxRecup=request.args.get('max-priceIndex')
    prixminRecup=request.args.get('min-priceIndex')

    if prixmaxRecup is not None and prixminRecup is not None:
        annonces=Annonce.query.filter(Annonce.prix.between(prixminRecup,prixmaxRecup)).all()

    else:
        # Si la catégorie est spécifiée, filtrer par catégorie
        annonces = Annonce.query.all()
    page = request.args.get(get_page_parameter(), type=int, default=1)
    NbreElementParPage = 2
    offset = (page - 1) * NbreElementParPage
    pagination = Pagination(page=page, per_page=NbreElementParPage, total=len(annonces))
    annonces = annonces[offset: offset + NbreElementParPage]
        
    
    return render_template("/pages/index.html",annonces=annonces,listcategories=listcategories,icons=icons,pagination=pagination)


# ==================================Search-----Input

@app.route('/recherche-annonce')
def recherche_annon():
    query = request.args.get('querygloire')
    annonces = Annonce.query.filter(Annonce.title.ilike(f"%{query}%")).all()
    
    count =len(annonces)
    page = request.args.get(get_page_parameter(), type=int, default=1)
    NbreElementParPage = 2
    offset = (page - 1) * NbreElementParPage
    pagination = Pagination(page=page, per_page=NbreElementParPage, total=len(annonces))
    annonces = annonces[offset: offset + NbreElementParPage]
    return render_template("/pages/index.html",annonces=annonces,listcategories=listcategories,icons=icons,count=count,pagination=pagination)

# afficher les annonces filtrées
@app.route('/annoncesTri', methods=['GET', 'POST'])
def afficher_annoncesTri():
    if request.method == 'POST':
        tri = request.form['tri']
        if tri == 'croissant':
            annonces = Annonce.query.order_by(Annonce.prix.asc()).all()
        elif tri == 'decroissant':
            annonces = Annonce.query.order_by(Annonce.prix.desc()).all()
        elif tri == 'recents':
            annonces = Annonce.query.order_by(Annonce.datePub.desc()).all()
        else:
            return 'Tri invalide'
    else:
        annonces = Annonce.query.all()

    count =len(annonces)
    page = request.args.get(get_page_parameter(), type=int, default=1)
    NbreElementParPage = 2
    offset = (page - 1) * NbreElementParPage
    pagination = Pagination(page=page, per_page=NbreElementParPage, total=len(annonces))
    annonces = annonces[offset: offset + NbreElementParPage]
    return render_template("/pages/index.html",annonces=annonces,listcategories=listcategories,icons=icons,count=count,pagination=pagination)

# =====================================================================
# =============================Details Annonces===========================
# =====================================================================
# Test
@app.route("/Annonce/<int:id_annonce>")
def annonce_Id(id_annonce):
    annonce = findAnnonceById(id_annonce)
    
    
    # nbreEtoiles = Annonce.query(func.avg(Ratings.rating)).filter_by(annonce_id=id_annonce).scalar()

   
    if not annonce:
        return redirect(url_for("/"))
    return render_template("/pages/detailsAnnonce.html",annonce=annonce)


# =====================================================================
# =============================Details Annonces===========================
# =====================================================================
# Test


# =====================================================================
# =============================Voiture===========================
# =====================================================================
@app.route('/Filtre_desNeuf_Voitures')
def Filtre_desNeuf_Voitures():
    recolte = request.args.get('recolteMarque')
    annonces = Annonce.query.filter(Annonce.description.ilike(f"%{recolte}%")).all()
    
    count =len(annonces)
    page = request.args.get(get_page_parameter(), type=int, default=1)
    NbreElementParPage = 2
    offset = (page - 1) * NbreElementParPage
    pagination = Pagination(page=page, per_page=NbreElementParPage, total=len(annonces))
    annonces = annonces[offset: offset + NbreElementParPage]
    return render_template("/pages/index.html",annonces=annonces,listcategories=listcategories,icons=icons,count=count,pagination=pagination)


@app.route('/Filtre_Voitures_Neuves')
def Filtre_Voitures_Neuves():
    
    annonces = Annonce.query.filter(Annonce.etat==EnumEtatArticle.Neuf.name,Annonce.categorie==EnumCategorie.Vehicules.name).all()
    count =len(annonces)
    page = request.args.get(get_page_parameter(), type=int, default=1)
    NbreElementParPage = 2
    offset = (page - 1) * NbreElementParPage
    pagination = Pagination(page=page, per_page=NbreElementParPage, total=len(annonces))
    annonces = annonces[offset: offset + NbreElementParPage]
    return render_template("/pages/index.html",annonces=annonces,listcategories=listcategories,icons=icons,count=count,pagination=pagination)

@app.route('/Filtre_Location_Voitures')
def Filtre_Location_Voitures():
    
    annonces = Annonce.query.filter(Annonce.sousCategorie==SousCategorieVehicule.Location_Voitures.name,Annonce.categorie==EnumCategorie.Vehicules.name).all()
    count =len(annonces)
    page = request.args.get(get_page_parameter(), type=int, default=1)
    NbreElementParPage = 2
    offset = (page - 1) * NbreElementParPage
    pagination = Pagination(page=page, per_page=NbreElementParPage, total=len(annonces))
    annonces = annonces[offset: offset + NbreElementParPage]
    return render_template("/pages/index.html",annonces=annonces,listcategories=listcategories,icons=icons,count=count,pagination=pagination)


@app.route('/Filtre_All')
def Filtre_Voitures_All():
    
    annonces = (Annonce.query.filter(Annonce.published == 1, Annonce.deleted == 0,Annonce.categorie==EnumCategorie.Vehicules.name)
        .order_by(desc(Annonce.datePub))
        .all())
    count =len(annonces)
    page = request.args.get(get_page_parameter(), type=int, default=1)
    NbreElementParPage = 2
    offset = (page - 1) * NbreElementParPage
    pagination = Pagination(page=page, per_page=NbreElementParPage, total=len(annonces))
    annonces = annonces[offset: offset + NbreElementParPage]
    return render_template("/pages/index.html",annonces=annonces,listcategories=listcategories,icons=icons,count=count,pagination=pagination)


@app.route("/Vehicules")
def RouteVehicules():
    return render_template("/pages/vehicules.html",listesVehicules=listesVehicules)


@app.route("/FiltreVehicules")
def vehicules():
    #sousCategorieRecup=request.args.get('sousCategorie')
    CategoryRecup=request.args.get('Categories')
    #lieuxRecup=request.args.get('region')
    prixmaxRecup=request.args.get('max-price')
    prixminRecup=request.args.get('min-price')
    sousCategorieRecup=request.args.get('sousCategorie')
    if prixmaxRecup is not None and prixminRecup is not None and sousCategorieRecup is None :
        annonces=Annonce.query.filter(Annonce.prix.between(prixminRecup,prixmaxRecup)).all()
        
        
    if sousCategorieRecup is not None and prixmaxRecup is None and prixminRecup is None:
        annonces=Annonce.query.filter(Annonce.sousCategorie==sousCategorieRecup).all()
    annonces=Annonce.query.filter(Annonce.prix.between(prixminRecup,prixmaxRecup),Annonce.categorie==CategoryRecup).all()
    count =len(annonces)
    
    
    page = request.args.get(get_page_parameter(), type=int, default=1)
    NbreElementParPage = 2
    offset = (page - 1) * NbreElementParPage
    pagination = Pagination(page=page, per_page=NbreElementParPage, total=len(annonces))
    annonces = annonces[offset: offset + NbreElementParPage]
    
    return render_template("/pages/index.html",annonces=annonces,listcategories=listcategories,icons=icons,count=count,pagination=pagination)




# ===================================================================
# =============================Chat Envoye Recevoir Avec Socketio  =========================================
# =====================================================================

#====================je vais dans mon fichier special.py

# messages = []  # Liste pour stocker les messages

# @app.route('/chat/<int:article_id>')
# def chat(article_id):
#     annonce = Annonce.query.get(article_id)
#     if annonce:
#         article_author = annonce.users.nom
#         return render_template("/pages/chat.html", article_author=article_author)
#     else:
#         return "Article not found"

# @socketio.on('connect')
# def handle_connect():
#     print('Client connected!')

# @socketio.on('user_join')
# def handle_user_join(username):
#     print(f'User {username} joined!')

# @socketio.on('new_message')
# def handle_new_message(data):
#     message = data['message']
#     recipient = data['recipient']
#     sender = None

#     for sid, user in socketio.server.manager.rooms[''].items():
#         if user == request.sid:
#             sender = sid
#             break

#     if recipient == article_author:
#         emit('chat', {'message': message, 'sender': sender, 'recipient': recipient}, room=recipient)
#     else:
#         emit('chat', {'message': message, 'sender': sender}, broadcast=True)

#         # Ajouter le message à la liste
#         messages.append({'sender': sender, 'message': message})



# @app.route('/Annonce/Recent', methods=['POST'])
# def process_form():
#     selected_value = request.form['select_field']
#     annonces = getAnnoncesByDate('2023-03-28 03:37:35.970126')
#     # Do something with the selected value
#     return render_template("/pages/index.html",annonces=annonces,listcategories=listcategories,icons=icons)
    








# @app.route('/')
# def index():
#     # Accessing Enum members:
#     my_etat =EnumEtatArticle.Reconditione.name

#     # return 'my_etat is {}'.format(my_etat.value)
#     return 'my_etat is {}'.format(my_etat)



@app.route('/Restauration')
def Restauration_Categorie():  
    restos = Restaurant.query.all()
    count = len(restos)
    restoCat = Restaurant.query.all()
    page = request.args.get(get_page_parameter(), type=int, default=1)
    NbreElementParPage = 2
    offset = (page - 1) * NbreElementParPage
    pagination = Pagination(page=page, per_page=NbreElementParPage, total=count)
    restos = restos[offset: offset + NbreElementParPage]
    return render_template("/pages/restauration.html",restos=restos,pagination=pagination,restoCat=restoCat)


# =====================Search-----RestaurantParCategorie
@app.route('/CatResto')
def restaurant_par_categorie():
    categorieResto = request.args.get('categorieResto')
    
    if categorieResto is None:
        # Si la catégorie n'est pas spécifiée, afficher toutes les annonces
        restos = Restaurant.query.all()
        restoCat = Restaurant.query.all()
        count =len(restos)
    else:
        # Si la catégorie est spécifiée, filtrer par catégorie
        restos = Restaurant.query.filter_by(Categorie_Restaurant=categorieResto).all()
        restoCat = Restaurant.query.all()
        # count =Annonce.query.filter_by(categorie=categorie).count()
        count=len(restos) 
    page = request.args.get(get_page_parameter(), type=int, default=1)
    NbreElementParPage = 2
    offset = (page - 1) * NbreElementParPage
    pagination = Pagination(page=page, per_page=NbreElementParPage, total=count)
    restos = restos[offset: offset + NbreElementParPage]
        
    
  
    return render_template("/pages/restauration.html",restos=restos,pagination=pagination,restoCat=restoCat)


# articles = Article.query.order_by(Article.prix.asc()).all()
# articles = Article.query.order_by(Article.prix.desc()).all()
# # récupère les 10 articles les plus récents
# articles = Article.query.order_by(Article.date.desc()).limit(10).all()


