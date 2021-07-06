from random import randint
import emoji
def start():
    icon=[':meat_on_bone:',':fried_shrimp:',':hamburger:']
    team1=['','','']
    team2=['','','']
    team3=['','','']
    output='[----拉霸機----]\n'
    for i in range(3):
        team1[i]=icon[randint(0,2)]
        team2[i]=icon[randint(0,2)]
        team3[i]=icon[randint(0,2)]
        output+=emoji.emojize('    '+team1[i]+team2[i]+team3[i]+'\n')
    flag=0
    for i in range(3):
        if team1[i]==team2[i]==team3[i]:
            flag+=1
    if team1[0]==team1[1]==team1[2]:
        flag+=1
    if team2[0]==team2[1]==team2[2]:
        flag+=1
    if team3[0]==team3[1]==team3[2]:
        flag+=1
    if team1[0]==team2[1]==team3[2]:
        flag+=1
    if team3[0]==team2[1]==team1[2]:
        flag+=1
    if flag>=1:
        output+=('[----有中獎----]')
    else:
        output+=('[----沒中獎----]')
    return(output)