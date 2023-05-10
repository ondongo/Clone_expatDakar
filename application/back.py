import dbm
from .front import app

from flask import render_template, request, redirect, url_for, flash,session
from application.models.EnumEtatArticle import *
from application.models.EnumCategorie import *
from application.models.SousCategorie import *
from .front import app
from sqlalchemy import desc
from flask_login import login_required
from flask_paginate import Pagination, get_page_parameter
#Hash password
import hashlib
from flask_login import LoginManager,  login_user, logout_user, login_required, current_user
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

from application.models.model import(
    Annonce,
    Favorite,
    Restaurant,
    ajouter_favori,
    findAnnonceById,
    saveAnnonce,
    getAllAnnoncePublier,
    getAllAnnonceBrouillon,
    getAllAnnonceDel,
    un_delete,
    un_published,
    editAnnonceModel,
    
    User,
    saveUser,
    addResto
    
)



listcategories=list(EnumCategorie)

listEtats=list(EnumEtatArticle)
# =====================================================================
# =============================Publier Annonce===========================
# =====================================================================

  
 

@app.route('/admin/add/<categorie>', methods=['GET', 'POST'],defaults={"id_annonce":0,"categorie":None})
@app.route('/admin/add/<categorie>', methods=['GET', 'POST'],defaults={"id_annonce":0})
@login_required
def publierAnnonce(id_annonce, categorie):
    
    
        annonce = findAnnonceById(id_annonce)
        sous_categories = []
        recupcategories = categorie
        if request.method == 'GET':
            # ============01
            if categorie == 'Vehicules':
                sous_categories = SousCategorieVehicule.__members__.values()
            # ===========02
            elif categorie == 'Sport_Loisirs_Voyages':
                sous_categories = SousCategorieSport_Loisirs_Voyages.__members__.values()
            # =============03 
            elif categorie == 'Services':
                sous_categories = SousCategorieService.__members__.values()
            # =============04
            elif categorie == 'Offres_Emploi':
                sous_categories = SousCategorieOffreEmploi.__members__.values()
            # =============05   
            elif categorie == 'Multimedia':
                sous_categories = SousCategorieMultimedia.__members__.values()
            # =============06   
            elif categorie == 'Mode_Beaute':
                sous_categories = SousCategorieMode.__members__.values()
            # =============07   
            elif categorie == 'Equipements':
                sous_categories = SousCategorieMateriaux.__members__.values()
            # =============08   
            elif categorie == 'Maison':
                sous_categories = SousCategorieMaison.__members__.values()
            # =============09
            elif categorie == 'Immobilier':
                sous_categories = SousCategorieImmobilier.__members__.values()
            # =============10   
            elif categorie == 'Demande_Emploi':
                sous_categories = SousCategorieDemande.__members__.values()
            # =============11
            elif categorie == 'Animaux':
                sous_categories = SousCategorieAnimaux.__members__.values()
            # =============12
            elif categorie == 'AgroAlimentaire':
                sous_categories = SousCategorieAgroalimentaire.__members__.values()
    
        return render_template("/back/formAdd.html",annonce=annonce,listcategories=listcategories,listEtats=listEtats,sous_categories=sous_categories,recupcategories=recupcategories)








@app.route('/admin/edit/<int:id_annonce>', methods=['GET', 'POST'])
@login_required
def editAnnonce(id_annonce):
    annonce = Annonce.query.get(id_annonce)
    return render_template("/back/editArticle.html", annonce=annonce, listcategories=listcategories, listEtats=listEtats)

@app.route("/edit", methods=["POST"])
def edit():
    id_annonce = request.form.get("id_annonce")
    annonce = Annonce.query.get(id_annonce)
    if annonce:
        annonce.title = request.form.get("title")
        annonce.categorie = request.form.get("categorie")
        annonce.sousCategorie = request.form.get("sous_categorie")
        annonce.description = request.form.get("description")
        annonce.prix = request.form.get("prix")
        annonce.published = False if not request.form.get("publish") else True
        annonce.img_url = request.form.get("img_url")
        annonce.img_title = request.form.get("img_title")
        annonce.etat = request.form.get("etat")
        annonce.lieuPub = request.form.get("lieu")
        editAnnonceModel(annonce)
    return redirect(url_for("gestionAnnonce"))


#************************************Save ***********************************
@app.route("/save", methods=["POST"])
def save():
  
   
    id_annonce = request.form.get("id_annonce")
    title_form = request.form.get("title")
    categorie_form = request.form.get("categorie")
    sous_categorie_form = request.form.get("sous_categorie")
    description_form = request.form.get("description")
    prix_form = request.form.get("prix")
    publish_form = request.form.get("publish")
    img_url_form = request.form.get("img_url")
    img_title_form = request.form.get("img_title")
    etat_form= request.form.get("etat")
    lieuPub_form=request.form.get("lieu")

    # if not publish_form:
    #     publish_form = False
    # else:
    #     publish_form = True

    publish_form = False if not publish_form else True

    # Creer un objet de type Annonce
    new_annonce = Annonce(
        title=title_form,
        description=description_form ,
        prix=prix_form,
        published=publish_form,
        img_url=img_url_form,
        img_title=img_title_form,
        categorie=categorie_form,
        etat=etat_form,
        lieuPub=lieuPub_form,
        user_id=current_user.id,
        sousCategorie=sous_categorie_form
        # datePub=datetim
    )
    
    saveAnnonce(new_annonce)
    return redirect(url_for("publierAnnonce"))
    


# =====================================================================
# =============================Gerer Annonce Admin
# -===========================
# =====================================================================   
@app.route('/admin/listings')
@login_required
def gestionAnnonce():
   
        annonces =(
        Annonce.query.filter(Annonce.published == 1, Annonce.deleted == 0,Annonce.user_id==current_user.id).order_by((Annonce.datePub)).all())
        count_publier=len(annonces)
        return render_template("/back/gestionAnnonce.html",annonces=annonces,listcategories=listcategories,listEtats=listEtats,count_publier=count_publier)
 


#************************************ListCorbeille***********************************
@app.route('/admin/listings/Corbeille')
@login_required
def gestionAnnonce_Corbeille():
        annonces =getAllAnnonceDel()
        count_corbeille =len(annonces)
        return render_template("/back/gestionAnnonce.html",annonces=annonces,listcategories=listcategories,listEtats=listEtats,count_corbeille=count_corbeille)
    

#************************************Brouillon ***********************************
@app.route('/admin/listings/Brouillon')
@login_required
def gestionAnnonce_Brouillon():
        annonces =getAllAnnonceBrouillon()
        count_brouillon =len(annonces)
        return render_template("/back/gestionAnnonce.html",annonces=annonces,listcategories=listcategories,listEtats=listEtats,count_brouillon=count_brouillon)





#************************************Delete ***********************************
@app.route("/admin/annonce/<int:id_annonce>/delete")
def un_deleteAnnonce(id_annonce):
    un_delete(id_annonce)
    return redirect(url_for("gestionAnnonce"))


#************************************Publish ***********************************
@app.route("/admin/annonce/<int:id_annonce>/publish")
def un_publishAnnonce(id_annonce):
    un_published(id_annonce)
    return redirect(url_for("gestionAnnonce"))




# =====================================================================
# =============================Gestion de la connexion===========================
# =====================================================================

@app.route("/compte/creation", methods=["POST","GET"])
def creation_compte():
    if request.method == "POST":
        nom = request.form.get("nom")
        prenom = request.form.get("prenom")
        tel_recup = request.form.get("tel")
        login_recup = request.form.get("login")
        password = request.form.get("pass")
        password_confirmation = request.form.get("PassConfirmation")

        if password != password_confirmation:
            flash("Les mots de passe ne correspondent pas. Veuillez réessayer.", "danger")
            return redirect(url_for("creation_compte"))

        # Hasher le mot de passe dans la base de données
        hashed_password = hashlib.md5(password.encode('utf-8')).hexdigest()

        # Créez un nouvel utilisateur et enregistrez-le dans la base de données
        nouvel_utilisateur = User(nom=nom, prenom=prenom, tel=tel_recup, login=login_recup, password=hashed_password)
        
        test_existance = User.query.filter_by(tel=tel_recup, login=login_recup).first()
        if test_existance:
            flash("Ce login ou tel déjà utilisé. Veuillez en choisir un autre.")
            return redirect(url_for('creation_compte'))
        else:
            saveUser(nouvel_utilisateur)

            flash("Votre compte a été créé avec succès! Veuillez vous connecter.", "success")
            return redirect(url_for("login"))

    
    return render_template("/back/creation_compte.html")




@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route("/login", methods = ["GET","POST"])
def login():
    if request.method == 'POST':
        login = request.form['login']
        password = request.form['pass']
        tel=request.form['tel']
        user = User.query.filter_by(login= login, tel=tel).first()
        if user is None or not user.check_password(password):
            flash('Login ou mot de passe incorrect')
            return render_template('/back/login.html')
        else:
            # Log the user in
            login_user(user)

            return redirect(url_for('index'))
    else:
        return render_template("/back/login.html")

# Deconnexion
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))






# ===================================================================
# =============================404 Error=========================================
# =====================================================================


@app.errorhandler(404)
def page404(error):
    return render_template("errors/404.html")


@app.route('/recherche-annonceAvancee')
def recherche_annonAvancee():
    query = request.args.get('searchAvance')
    annonces=(Annonce.query.filter( Annonce.user_id==current_user.id,
                                   Annonce.title.ilike(f"%{query}%"))
        .order_by(desc(Annonce.datePub))
        .all())
    count =len(annonces)
    return render_template("/back/gestionAnnonce.html",annonces=annonces,count=count)



@app.route('/favoris')
@login_required
def articles_favoris():
    user = User.query.get(current_user.id)
    annonces_favoris = user.favorites
    list_favoris = []
    for annonce in annonces_favoris:
        list_favoris.append(annonce.id)
    # Retrieve the information of the articles in the ids_articles_favoris list
    annonce_favoris_info = Annonce.query.filter(Annonce.id.in_(list_favoris)).all()
    count_fav=len(annonce_favoris_info)
    # Render the template with the list of articles in favoris
    return render_template('/back/favori.html', annonces_favoris=annonce_favoris_info,count_fav=count_fav)



@app.route('/ajouter_favoriBack/<int:id_annonce>', methods=['GET','POST'])
@login_required
def ajouter_favoriBack(id_annonce):
    annonce = Annonce.query.get(id_annonce)
    user = User.query.get(current_user.id)
    if annonce not in user.favorites:
        favorite = Favorite(annonce_id=annonce.id, user_id=current_user.id)
        ajouter_favori(favorite)
        flash("L'annonce a été ajoutée à vos favoris avec succès", 'success')
        return redirect(url_for('articles_favoris'))
    else:
        flash('Impossible Deja en favori')


@app.route('/retirer_favoriBack/<int:id_annonce>', methods=['GET','POST'])
@login_required
def retirer_favoriBack(id_annonce):
    return redirect(url_for('articles_favoris'))














#************************************SaveRestaurant ***********************************

@app.route('/admin/addResto', methods=['GET', 'POST'])
@login_required
def publierResto():
    return render_template("back/CreerRestaurant.html")
    
    
@app.route("/saveRestaurant", methods=["POST"])
def saveRestaurant():
   
    #id_annonce = request.form.get("id_annonce")
    nom_form = request.form.get("title")
    cat_form = request.form.get("cat")
   
    description_form = request.form.get("description")
    lieu_form = request.form.get("lieu")
    img_url_form = request.form.get("img_url")
    img_title_form = request.form.get("img_title")
    ouverture_form= request.form.get("ouverture")
    fermeture_form=request.form.get("fermeture")
    publish_form=request.form.get("publish")

    # if not publish_form:
    #     publish_form = False
    # else:
    #     publish_form = True

    publish_form = False if not publish_form else True

    # Creer un objet de type Annonce
    
    new_restaurant = Restaurant(
        Categorie_Restaurant=cat_form,
        Nom_Restaurant=nom_form,
        description_Restaurant=description_form ,
       
        published=publish_form,
        img_url=img_url_form,
        img_title=img_title_form,
       Opening_hours=ouverture_form,
       Fermeture_hours=fermeture_form,
        adresse= lieu_form ,
        user_id=current_user.id,
     
        # datePub=datetim
    )
    
    addResto(new_restaurant)
    return redirect(url_for("publierResto"))
    