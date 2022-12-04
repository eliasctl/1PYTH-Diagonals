#!/opt/homebrew/bin/python3 python3
# Script by Elias MOUSSA OSMAN SupInfo B.Eng.1 2022-2023
# Le but de ce mini-projet est de programmer en Python un petit jeu de stratégie combinatoire abstrait nommé Diagonals.

# Entreé des données permetant de jouer
n = int(input("Entrez la taille du tableau dans lequel vous souhaitez jouer : "))

#Une fonction "newBoard(n)" qui retourne une liste à deux dimensions représentant l’état initial d’un plateau de jeu de n cases sur n cases.
board = []
def newBoard(n):
	for i in range(n):
		temp = []
		for k in range(n):
			temp.append(0)
		board.append(temp)
	print(board)

#Une procédure "displayBoard(board, n)" qui réalise l’affichage du plateau sur la console. On représentera une case vide par un ‘.’, un pion blanc par un ‘x’ et un pion noir par un ‘o’. On numérotera les lignes et les colonnes (à partir de 1) pour que les joueurs puissent repérer facilement les coordonnées d'une case.
def displayBoard(board, n):
	for k in range(n):
		print("\n",k," | ", end="")
		for l in range(n):
			if board[k][l] == 0:
				print(" . ", end="")
			# Joueur 1
			elif board[k][l] == 1:
				print(" o ", end="")
			# Joueur 2
			elif board[k][l] == 2:
				print(" x ", end="")
	
	print("\n    |",end="")
	for m in range(n):
		print("―――",end="")
	print("\n     ",end="")
	for o in range(n):
		print(" ",o,end="")
	print("\n")

#Une procédure "displayScore(score)" qui réalise l'affichage du score sur la console.
def displayScore(score):
	print("Scores : Le Joueur 1 à ", score[0]," points, le joueur 2 à ", score[1], " points .")

#Une fonction "possibleSquare(board, n, i, j)" qui retourne True si i et j sont les coordonnées d’une case où le joueur courant peut poser un pion, et False sinon
def possibleSquare(board, n, i, j):
	temp = board[i]
	if temp[j]!=0:
		return False
	else:
		return True

#Une fonction "selectSquare(board, n)" qui fait saisir au joueur player les coordonnées d’une case où il peut poser un pion. On supposera qu’il existe une telle case, on ne testera pas ce fait ici. Tant que ces coordonnées ne seront pas valides en regard des règles du jeu (et des dimensions du plateau), on lui demandera de nouveau de les saisir. Finalement, la fonction retournera ces coordonnées.

def selectSquare(board, n):
	i = int(input("Entrez l'ordonné de la case choisie : "))
	j = int(input("Entrez l'abscice de la case choisie : "))
	while possibleSquare(board, n, i, j)!=True:
		print("La case entrée n'est pas valide ! ")
		i = int(input("Entrez l'ordonné de la case choisie : "))
		j = int(input("Entrez l'abscice de la case choisie : "))
	return i, j

	

#Une procédure "updateBoard(board, player, i, j)" où l’on suppose ici que i et j sont les coordonnées d’une case où le joueur player peut poser un pion. Cette procédure réalise cette pose.
def updateBoard(board, player, i, j):
	if player == 1:
		board[i][j]=1
	else:
		board[i][j]=2


#Une procédure "updateScore(board, n, player, score, i, j)" où l’on suppose ici que i et j sont les coordonnées d’une case où le joueur player vient de poser un pion. Cette procédure met à jour le score du joueur player.
#⚠️ Erreur out of range
def updateScore(board, n, player, score, i, j):
	iTemp = i
	jTemp = j
	hg = True
	hd = True
	bg = True
	bd = True
	compteur_pions =0
	
	for i in range(n):
		print("test")
		
	
	# Diagonale Haut gauche
	while (iTemp != -1 or jTemp !=-1)and(iTemp!=n-1 or jTemp != n-1):
		if board[iTemp][jTemp] == 0:
			hg = False
		iTemp -=1
		jTemp -=1
	iTemp = i
	jTemp = j
	# Diagonale bas Droit
	while (iTemp != -1 or jTemp !=-1)and(iTemp!=n-1 or jTemp != n-1):
		if board[iTemp][jTemp] == 0:
			bd = False
		iTemp +=1
		jTemp +=1
	iTemp = i
	jTemp = j
	# Diagonale haut Droit
	while (iTemp != -1 or jTemp !=-1)and(iTemp!=n-1 or jTemp != n-1):
		if board[iTemp][jTemp] == 0:
			bd = False
		iTemp -=1
		jTemp +=1
	iTemp = i
	jTemp = j
	# Diagonale bas Gauche
	while (iTemp != -1 or jTemp !=-1)and(iTemp!=n-1 or jTemp != n-1):
		if board[iTemp][jTemp] == 0:
			bd = False
		iTemp +=1
		jTemp -=1
	iTemp = i
	jTemp = j
	
	# Diagonale Haut gauche et Bas droit
	if hg==True and bd==True:
		while (iTemp != -1 or jTemp !=-1)and(iTemp!=n-1 or jTemp != n-1):
			if board[iTemp][jTemp] == player:
				compteur_pions += 1
			iTemp -=1
			jTemp -=1
		iTemp = i
		jTemp = j
		while (iTemp != -1 or jTemp !=-1)and(iTemp!=n-1 or jTemp != n-1):
			if board[iTemp][jTemp] == player:
				compteur_pions += 1
			iTemp +=1
			jTemp +=1
		iTemp = i
		jTemp = j
		compteur_pions -=1
	
	# Diagonale bas gauche et haut droit
	if hg==True and bd==True:
		while (iTemp != -1 or jTemp !=-1)and(iTemp!=n-1 or jTemp != n-1):
			if board[iTemp][jTemp] == player:
				compteur_pions += 1
			iTemp +=1
			jTemp -=1
		iTemp = i
		jTemp = j
		while (iTemp != -1 or jTemp !=-1)and(iTemp!=n-1 or jTemp != n-1):
			if board[iTemp][jTemp] == player:
				compteur_pions += 1
			iTemp -=1
			jTemp +=1
		compteur_pions -=1
	score[player-1]+=compteur_pions
	
#Une fonction "again(board, n)" qui retourne True si le joueur courant peut poser un pion sur le plateau et False sinon.
def again(board, n):
	casesVides = 0
	for i in range(n):
		for k in range(n):
			if board[i][k]==0:
				casesVides +=1
	return casesVides
	
#Une fonction "win(score)" qui retourne une chaîne de caractères indiquant l’issue de la partie.
def win(score):
	if score[0]==score[1]:
		print("🎉Vous avez tous les deux gagner avec un total de ",score[0]," points !🎊")
	elif score[0]>score[1]:
		print("🎉Le joueur 1 à gagner avec un total de ",score[0]," points !🎊")
	else:
		print("🎉Le joueur 2 à gagner avec un total de ",score[0]," points !🎊")


#Un programme principal "diagonals(n)" qui utilisera les sous-programmes précédents (et d’autres si besoin est) afin de permettre à deux joueurs de disputer une partie complète sur un plateau de jeu de n cases sur n cases.
		

def diagonals(n):
	player = 1
	score = [0, 0]
	print("⚠️ Dev en cour")
	newBoard(n)
	while again(board, n)!=0:
		displayBoard(board, n)
		i,j = selectSquare(board, n)
		updateBoard(board, player, i, j)
		#updateScore(board, n, player, score, i, j) # erreur out of range : désactiver
		displayScore(score)
		if player == 1:
			player =2
		else:
			player =1
	displayBoard(board, n)
	win(score)
	
diagonals(n)