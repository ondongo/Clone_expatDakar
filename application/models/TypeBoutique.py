# if request.method == 'POST':
#         # Vérifiez si le fichier est présent dans la requête
#         if 'file' not in request.files:
#             return 'Aucun fichier n\'a été téléchargé.'
#         file = request.files['file']
#         # Si l'utilisateur n'a pas sélectionné de fichier, le champ de fichier sera vide
#         if file.filename == '':
#             return 'Aucun fichier n\'a été sélectionné.'
#         # Vérifiez si le fichier téléchargé est une image
#         if not file.content_type.startswith('image/'):
#             return 'Le fichier téléchargé doit être une image.'
#         # Enregistrez le fichier dans le dossier d'upload
#         filename = file.filename
#         filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
#         file.save(filepath)
#         # Ouvrir l'image avec PIL et la traiter
#         with Image.open(filepath) as image:
#             image = image.convert('RGB')
#             image = image.resize((500, 500))
#             # Enregistrer l'image traitée dans un nouveau fichier
#             processed_filepath = os.path.join(app.config['UPLOAD_FOLDER'], 'processed_' + filename)
#             image.save(processed_filepath)
#         # Enregistrez le chemin d'accès à l'image dans votre base de données
#         image_path = 'uploads/processed_' + filename