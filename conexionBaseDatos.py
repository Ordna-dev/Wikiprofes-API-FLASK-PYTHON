import psycopg2

bd = psycopg2.connect(port='5432', host="localhost", dbname="wikiprofes_2.0", user="postgres", password="dantes115")
# bd = psycopg2.connect(port='5433',host="localhost", dbname="wikiprofes_2.0", user="postgres", password="naruto11")
#Carlos, no borres el comentario porfa :'v, se me olvida jajajaj

cursor = bd.cursor()