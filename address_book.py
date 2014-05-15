# definisco classe friend //////////////////////////////////////////////////////////////////////////////////
class friend(object):
	address = ''
	email = ''
	phone = ''
	def __init__(self,nome,cognome):
		self.nome = nome
		self.cognome = cognome
	# inserisci dati
	def insert_address(self,address):
		self.address = address
	def insert_email(self,email):
		if self.check_email(email):
			self.email = email
		else:
			return 'not valid email'
	def insert_phone(self,phone): 
		if self.check_phone(phone):
			self.phone = phone
		else:
			return 'not valid phone'
	#leggi dati
	def get_address(self):
		return self.address
	def get_email(self):
		return self.email
	def get_phone(self):
		return self.phone
	# controllo dei dati inseriti
	def check_email(self,email):
		if '@' in email and '.' in email:
			return True
		else:
			return False
	def check_phone(self,phone):
		for i in phone:
			if i.lower() in 'abcdefghijklmnopqrstuwxyz':
				return False
		else:
			return True
	# da in ooutput i dati di un oggetto
	def write_data(self):
		return str(self.nome) + ' ' + str(self.cognome) + ' ' + str(self.address) + ' ' + str(self.email) + ' ' + str(self.phone)
# /////////////////////////////// fine oggetto ////////////////////////////////////////////////////////////
def check_new_element(nome,cognome):
	with open(file_name) as my_file:
		for line in my_file:
			if nome in line and cognome in line:
				print 'questo account esiste gia'
				print line
				return False
	my_file.close()
	return True

# mette tutti i dati del file in una lista temporanea
def modifica_contenuto(oggetto):
	raccogli = [];
	with open(file_name) as my_file:
			for line in my_file:
				if oggetto.nome in line and oggetto.cognome in line:
					raccogli.append(oggetto.write_data())
				else:
					raccogli.append(line)
	my_file.close()
	return raccogli

# legge la lista temporanea e scrive il contenuto in un altro file
def riscrivi(elementi):
	my_file2 = open(file_name2,'w')
	for line in elementi:
			my_file2.write(line)
			my_file2.write('\n')
	my_file2.close()
	return

# inserisce nuovo account
def inserisci_nuovo_account():
	nome = raw_input('inserire nome :')
	cognome = raw_input('inserire cognome _:')
	if check_new_element(nome,cognome):
		indirizzo= raw_input('inserire indirizzo _:')
		email = raw_input('inserire indirizzo email _:')
		telefono = raw_input('inserire numero di telefono _:')
		oggetto = friend(nome,cognome)
		oggetto.insert_address(indirizzo)
		oggetto.insert_email(email)
		oggetto.insert_phone(telefono)
		return oggetto
	else:
		print 'oggetto gia esistente'
		return

# scrive nuovo account nel file
def scrivi_dati(oggetto):
	my_file = open(file_name,'a')
	#se il file contiene dei dati non devi cancellarli
	my_file.write(oggetto.write_data())
	my_file.write('\n')
	my_file.close()
	return

def modifica_oggetto(oggetto):
	indirizzo= raw_input('inserire indirizzo _:')
	email = raw_input('inserire indirizzo email _:')
	telefono = raw_input('inserire numero di telefono _:')
	oggetto.insert_address(indirizzo)
	oggetto.insert_email(email)
	oggetto.insert_phone(telefono)
	return


#inserisci comandi da terminale
s = True
file_name = 'nuovo.txt' #raw_input('inserire nome file da creare o modificare _:')
file_name2 ='nuovo2.txt'
print 'Benvenuto nel programma agenda'
while s == True:
	print '1. crea nuovo account'
	print '2. modifica account esistente'
	print '3. cerca un account'
	print 'q. per  uscire'
	decision = raw_input('selezionare operazione _:')
	if decision == '1':
		scrivi_dati(inserisci_nuovo_account())
	if decision == '2':
		nome = raw_input('inserire_nome _:')
		cognome = raw_input('inserire cognome _:')
		if  not check_new_element(nome,cognome):
			oggetto = friend(nome,cognome)
			modifica_oggetto(oggetto)
			riscrivi(modifica_contenuto(oggetto))
	if decision == '3':
		nome = raw_input('inserire_nome _:')
		cognome = raw_input('inserire cognome _:')
		check_new_element(nome,cognome)
		if not check_new_element(nome,cognome):
			print 'l\' account non esiste'
	if decision =='q':
		print 'hai deciso di chiudere ciaoooooooooo'
		quit()
		


