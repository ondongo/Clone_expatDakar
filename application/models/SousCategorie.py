from enum import Enum



class SousCategorieAgroalimentaire(Enum):
    Alimentation=1
    Agriculture=2
    
    
class SousCategorieMaison(Enum):
    Mobilier=1
    Electromenager=2
    Décoration_linge_maison=3
    Vaisselle=4
    Jardinage_bricolage=5 


class SousCategorieVehicule(Enum):
    Moto_Scooters=1
    Location_Voitures=2
    Equipements_Pieces=3
    Vans=4
    Engins=5
    Bateaux=6
    Camions=7
    
class SousCategorieImmobilier(Enum):
    Appartements_à_louer=1
    Appartements_meublés=2
    Terrains_à_vendre=3
    Maisons_à_vendre=4
    Maisons_à_louer=5
    Appartements_à_vendre=6
    Propriétés_commerciales_louer=7
    Chambres_louer=8
    Propriétés_commerciales_vendre=9
    

class SousCategorieMultimedia(Enum):
    Ordinateurs=1
    Téléphones=2
    Accessoires_multimédia=3
    TV_home_cinéma=4
    Jeux_vidéos_consoles=5
    Tablettes=6
    Equipement_vidéo_audio=7
    Imprimantes_scanners=8
    Appareils_photos=9 
 
 
    
class SousCategorieOffreEmploi(Enum):
    Emploi_vente_commercial=1
    Emploi_marketing_communication=2
    Emploi_services_personne=3
    Emploi_transport_logistique=4
    Emploi_informatique=5
    Emploi_construction_architecture=6
    Emploi_médical_santé=7
    Emploi_social=8
    Emploi_restauration=9
    Emploi_enseignement_formation=10
    Emploi_management_business_development=11
    Emploi_administratif=12
    Emploi_hôtellerie_tourisme_loisirs=13
    Emploi_comptabilité_finance_audit=14
    Emploi_service_client_support_technique=15
    Emploi_graphisme_design=16
    Emploi_hygiène_sécurité=17
    Emploi_ressources_humaines=18
    Emploi_gestion_projet_produit=19
    Emploi_immobilier=20
    Emploi_conseil_stratégie=21
    Emploi_ingénierie=22
    Emploi_achat=23
    Emploi_agricole=24
    Emploi_juridique=25
    Emploi_sécurité=26
    
class SousCategorieSport_Loisirs_Voyages(Enum):   
    Matériel_de_sport=1
    Vélos=2
    Instruments_musique=3
    CDs_DVDs_livres=4
    Tourisme_activités=5
    Art_artisanat=6
    Hôtels=7
    
class SousCategorieService(Enum):
    Prestations_de_service=1
    Coursparticuliers=2
    Formations=3
    Objets_perdus_retrouvé=4
    
class SousCategorieDemande(Enum):
    Autres_demandes_emploi=1
    Nettoyage_personnel=2
    Chauffeur_conducteur=3
    Restauration=4
    Demande_stages=5
    Nounous_garde_enfants=6
    
class SousCategorieAnimaux(Enum):
    Accessoires_animaux=1
    Chiens_chiots=2
    Autres_animaux=3
    Pigeons=4
    Moutons=5
    Lapins=6
    Chats_chatons=7 

  
class SousCategorieMode(Enum):
    Enfant_bébé=1
    Parfums_produits_cosmetiques=2
    Vetements_homme=3
    Vêtements_femme=4
    Montres_bijoux=5
    Chaussure_homme=6
    Accessoires_de_mode=7
    Valises_sacs=8
    Cheveux_coiffure=9
    Chaussures_femme=10
    Lingerie =11
    
class SousCategorieMateriaux(Enum):
    Matériel_pro=1
    Matériel_construction=2
    Caméras_surveillance=3
    Energie_groupes_électrogènes=4
    Equipement_médical=5
    Equipement_restauration =6