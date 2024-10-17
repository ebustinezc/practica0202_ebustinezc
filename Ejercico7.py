# Escribir un programa que pregunte el correo electrónico del usuario en la consola y muestre por pantalla otro correo electrónico 
# con el mismo nombre (la parte delantera de la arroba @) pero con dominio ceu.es.
correo_electronico=input('Escribe tu correo electronico:')
print(correo_electronico[:correo_electronico.find('@')],'@ceu.es.')