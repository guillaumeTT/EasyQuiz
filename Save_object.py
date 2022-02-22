import pickle
def save_test(obj, nom_fichier):
	'''Pour sauvegarder un objet précis'''
	with open(f"save/{nom_fichier}.data", "wb") as fic:
		record = pickle.Pickler(fic)
		record.dump(obj)
	

def charger_test(nom_fichier):
	'''Pour charger  un objet précis'''
	with open(f"save/{nom_fichier}.data", "rb") as fic:
		record = pickle.Unpickler(fic)
		pp = record.load()
		return pp