from .text import centerprint, enter_select
import time


def TrainingPlayer(hero):
    print('='*30)
    centerprint("== Training ==")
    print('=' * 30)

    if hero.type_hero == 'mage':
        print("1.Magic \n\t|Magic + {} | - {} Coin|".format(hero.UpPower, hero.reqCoinPower))
    else:
        print("1.Power \n\t|Power + {} | - {} Coin|".format(hero.UpPower, hero.reqCoinPower))

    print("2.Crit \n\t|Crit + {}% | - {} Coin|".format(hero.UpCrit, hero.reqCoinCrit))
    print("3.Health \n\t|Hp    + {} | - {} Coin|".format(hero.UpHp, hero.reqCoinHp))

    if hero.type_hero == 'mage':
        print("4.Mana \n\t|Mp    + {} | - {} Coin|".format(hero.UpMp, hero.reqCoinMp))
        print('5.Keluar')
    else:
        print('4.Keluar')

    print("="*30)
    index = input("==> ")

    if index == '1':
        training_power(hero)
    elif index == '2':
        training_Crit(hero)
    elif index == '3':
        training_Hp(hero)

    elif hero.type_hero == 'mage' and index == '4':
        training_Mp(hero)
    elif hero.type_hero == 'mage' and index == '5':
        from source.stargame import camp
        return camp()

    elif index == '4':
        from source.stargame import camp
        return camp()

    else:
        TrainingPlayer(hero)


def training_Hp(hero):
    print("=" * 30)
    if hero.coin >= hero.reqCoinHp:
        hero.coin -= hero.reqCoinHp
        hero.reqCoinHp += round(hero.reqCoinHp / 3)  # Untik Menambahkan Coin

        # Proses Penambahan health dan Max Health Ke hero
        hero.health += hero.UpHp
        hero.healthMax += hero.UpHp
        print("Tunggu")
        time.sleep(2)
        centerprint("Health + {}".format(hero.UpHp))
        time.sleep(1)
        centerprint("Health Max + {}".format(hero.UpHp))
        time.sleep(1)
        print("Selesai")

        hero.UpHp += 10  # Menambahkan Up Health Ketika Ke Training Lagi
        TrainingPlayer(hero)
    else:
        limit_coin = hero.coin - hero.reqCoinHp
        centerprint("Coin Anda Kurang {}".format(limit_coin))
        enter_select()
        training_Hp(hero)


def training_Mp(hero):
    print("=" * 30)
    if hero.coin >= hero.reqCoinMp:
        hero.coin -= hero.reqCoinMp
        hero.reqCoinMp += round(hero.reqCoinMp / 3)

        # Proses penambahan Mana
        hero.mana += hero.UpMp
        hero.manaMax += hero.UpMp
        print("Tunggu")
        time.sleep(2)
        centerprint("Mana + {}".format(hero.UpMp))
        time.sleep(1)
        centerprint("Mana Max + {}".format(hero.UpMp))
        time.sleep(1)
        print("Selesai")

        hero.UpMp += 5
        TrainingPlayer(hero)
    else:
        limit_coin = hero.coin - hero.reqCoinMp
        centerprint("Coin Anda Kurang {}".format(limit_coin))
        enter_select()
        training_Hp(hero)


def training_power(hero):
    print("=" * 30)
    if hero.coin >= hero.reqCoinPower:
        hero.coin -= hero.reqCoinPower
        hero.reqCoinPower += round(hero.reqCoinPower / 2)

        print("Tunggu")
        time.sleep(2)
        if hero.type_hero == 'mage':
            hero.magic += hero.UpPower
            centerprint("Magic + {}".format(hero.UpPower))
        else:
            hero.attPower += hero.UpPower
            centerprint("Power + {}".format(hero.UpPower))
        time.sleep(1)
        print("Selesai")

        hero.UpPower += 5
        TrainingPlayer(hero)
    else:
        limit_coin = hero.coin - hero.reqCoinPower
        centerprint("Coin Anda Kurang {}".format(limit_coin))
        enter_select()
        training_Hp(hero)


def training_Crit(hero):
    print("=" * 30)
    if hero.coin >= hero.reqCoinCrit:
        hero.coin -= hero.reqCoinCrit
        hero.reqCoinCrit += round(hero.reqCoinCrit / 2)

        hero.crit += hero.UpCrit
        print("Tunggu")
        time.sleep(2)
        centerprint("Crit + {}%".format(hero.UpCrit))
        time.sleep(1)
        print("Selesai")

        hero.UpCrit += 1
        TrainingPlayer(hero)
    else:
        limit_coin = hero.coin - hero.reqCoinCrit
        centerprint("Coin Anda Kurang {}".format(limit_coin))
        enter_select()
        training_Hp(hero)
