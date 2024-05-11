import os
#Nombres: Gael Humberto Borchardt Castellanos Daniel Ivan Estrada Neri
class Config():
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'clave_secretinha'