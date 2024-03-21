def get_match(idmatch):

    c.execute(f"SELECT * FROM match WHERE id_match==idmatch;")

def set_match(idmacth,outcome,nbr,nbcd,nbdf, nbf, classadv):

     c.execute(f"INSERT  INTO match VALUES (idmacth,outcome,nbr,nbcd,nbdf, nbf, classadv;")
    
def set_stats (idmatch, nbvictoire, nbdefaite, iduser):
    c.execute(f"INSERT INTO stats VALUES (idmatch, nbvictoire, nbdefaite, iduser;)")
    
def get_stats (iduser):
    c.execute(f"SELECT * FROM stats WHERE id_user=iduser;")

def set_user (nom, prenom, iduser, password):
    c.execute(f"INSERT INTO user VALUES (nom, prenom, iduser, password);")

def get_user(iduser):
     c.execute(f"SELECT * FROM user WHERE id_user=iduser ;")
    
def remplacer_match (idmacth,outcome,nbr,nbcd,nbdf, nbf, classadv):
    c.execute(f"TRUNCATE TABLE match;")
    c.execute(f"INSERT  INTO match VALUES (idmacth,outcome,nbr,nbcd,nbdf, nbf, classadv;")
    
def remplacer_stats(idmatch, nbvictoire, nbdefaite, iduser):
    c.execute(f"TRUNCATE TABLE stats;")
    c.execute(f"INSERT  INTO stats VALUES (idmatch, nbvictoire, nbdefaite, iduser;")

def remplacer_user(nom, prenom, iduser, password):
    c.execute(f"TRUNCATE TABLE user;")
    c.execute(f"INSERT  INTO user VALUES (nom, prenom, iduser, password;")
