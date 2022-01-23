"""
Sujet:
https://pixees.fr/informatiquelycee/n_site/snt_photo_transImg.html
"""


from PIL import Image

img = Image.open("pomme.jpg")

largeur_image=img.width
hauteur_image=img.height



############Premier exemple:
r,v,b=img.getpixel((100,250))
print("canal rouge : ",r,"canal vert : ",v,"canal bleu : ",b)


############Deuxieme exemple:
for y in range(hauteur_image):
    for x in range(largeur_image):
        r,v,b=img.getpixel((x,y))
        if v<200:
            n_v=255-v
        else :
            n_v=v
        img.putpixel((x,y),(r,n_v,b))
img.show()


###########Exercice 1
##À l'aide du code du premier exemple :
##Modifiez le programme du "Premier exemple" pour qu'il affiche les valeurs du canal rouge,
##du canal vert et du canal bleu du pixel de coordonnées (250,300), notez votre réponse en dessous.
###########

###########Exercice 2
##À l'aide du code du premier exemple et de la méthode putpixel:
##Modifiez le programme du "Premier exemple" afin de colorier le pixel de coordonnées (100,250) en bleu,
##notez votre réponse en dessous.
###########

###########Exercice 3, filtre négatif
##Ecrivez un programme qui donne le négatif d'une image.
##Vous pouvez renprendre les bases du deuxième exemple,
##notez votre réponse en dessous.
##Remarque : La négative d’un pixel de couleur c1=(r,v,b) est le pixel de couleur c2=(255−r,255−v,255−b).
###########

