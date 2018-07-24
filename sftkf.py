# -*- coding: utf-8 -*-

suji = ["一","二","三","四","五","六","七","八","九"]
zenkaku = ["１","２","３","４","５","６","７","８","９"]
koma = {"P":"歩",
        "L":"香",
        "N":"桂",
        "S":"銀",
        "G":"金",
        "K":"玉",
        "B":"角",
        "R":"飛",
        "+P":"と",
        "+L":"杏",
        "+N":"圭",
        "+S":"全",
        "+R":"龍",
        "+B":"馬",
}

#sf = raw_input("sfen > ")
sf = raw_input()
        
usimoves = sf.split(" ")

board = [ ["l","n","s","g","k","g","s","n","l"],
              ["","b","","","","","","r",""],
              ["p","p","p","p","p","p","p","p","p"],
              ["","","","","","","","",""],
              ["","","","","","","","",""],
              ["","","","","","","","",""],
              ["P","P","P","P","P","P","P","P","P"],
              ["","R","","","","","","B",""],
              ["L","N","S","G","K","G","S","N","L"] ]
c = 0
sfd = {'a': 0, 'c': 2, 'b': 1, 'e': 4, 'd': 3, 'g': 6, 'f': 5, 'i': 8, 'h': 7}
moji = ""

for move in usimoves:
    #print move
    if len(move)<4:
        pass
    elif move=="moves":
        pass
    elif move[1]=="*":
        piece = move[0]
        c += 1 
        board[sfd[move[3]]][int(move[2])-1] = piece
        m = "  {} {}{}{}打   ( 0:00/00:00:00)".format(c,zenkaku[int(move[2])-1],suji[sfd[move[3]]],koma[piece])
    else:
        piece = board[sfd[move[1]]][int(move[0])-1].upper()
        if move[-1]=="+":
            piece = "+"+piece
        board[sfd[move[3]]][int(move[2])-1] = piece
        board[sfd[move[1]]][int(move[0])-1] = ""
        c += 1 
        m = "  {} {}{}{}({}{})   ( 0:00/00:00:00)".format(c,zenkaku[int(move[2])-1],suji[sfd[move[3]]],koma[piece],move[0],sfd[move[1]]+1)
    #print m
    moji += m + "\n"



moji = """#KIF version=2.0 encoding=UTF-8
開始日時：2018/03/28
棋戦：電脳(弾丸)
持ち時間：1分
手合割：平手
先手：black
後手：white
手数----指手---------消費時間--
"""+moji

print moji
