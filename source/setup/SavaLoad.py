import os
import datetime
import pickle
from .text import centerprint


def loadgame():
    # load hero object from pickle file
    dirlist = os.listdir('./saves/')
    for i, item in enumerate(dirlist):
        print(str(i) + ' - ' + str(item))
        print(str(datetime.datetime.fromtimestamp(os.path.getmtime('./saves/' + item))))
        print('')
    index = input("Pilih Save Game\nOr [c]ancel : ")
    if index == '':
        index = 0
    if index == 'c':
        from source.stargame import play
        return play()
    index = int(index)
    ourpickle = open(('./saves/' + str(dirlist[index])), "rb")
    player = pickle.load(ourpickle)
    return player


# pickle our hero to file
def savegame(data):
    # pickle hero object to file
    # should prompt to overwrite
    print("=" * 30)
    heroname = input('Nama save game\nOr [c]ancel : ')
    print("=" * 30)
    if heroname == 'c':
        from source.stargame import camp
        return camp()
    savefolder = "./saves/"
    filepath = savefolder + heroname + '.hero'
    gamedata = data
    if not os.path.isfile(filepath):
        with open(filepath, 'wb') as f:
            pickle.dump(gamedata, f, -1)
    else:
        print("Nama save game sudah Ada")
        answer = input('Timpa save game [y/n] : ')
        print("=" * 30)
        if answer.lower() == 'y':
            os.remove(filepath)
            # print(os.listdir('./saves/'))
            with open(filepath, 'wb') as f:
                pickle.dump(gamedata, f, -1)
        elif answer.lower() == 'n':
            print("Masukan nama Save Game Baru")
            newname = input('>>> : ')
            newfilepath = savefolder + newname + '.hero'
            print("="*30)
            with open(newfilepath, 'wb') as f:
                pickle.dump(gamedata, f, -1)
        else:
            centerprint("Save game Failed")
            from source.stargame import camp
            return camp()
