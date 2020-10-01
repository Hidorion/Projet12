import pygame 
import pytmx


tm = pytmx.load_pygame("Foret.tmx", pixelalpha=True)
# defini la largeur de la map, le nombre de tuile, et la taille des tuiles
width = tm.width * tm.tilewidth
# pareil pour la haute, nombre et taille des tuiles
height = tm.height * tm.tileheight
tmxdata = tm
#sauvegarder la commande
save_command = tmxdata.get_tile_image_by_gid
# parcourir les couche de la map
# Pour chaque calque visible
for layer in tmxdata.visible_layers :
    
    # Vérifier si le layer contient que des tuiles et pas des objets
    if isinstance(layer, pytmx.TiledTileLayer): 
        # pour chaque x, y et id de chaque image
        for x, y, gid, in layer :
            print(gid)
            # Recherche si le l'id correspond a une surface
            tile = save_command(gid)
            if tile :
                pass