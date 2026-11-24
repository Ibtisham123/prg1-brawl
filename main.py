import random

# Startvärdena väljer du själv.

mordare_namn = input("vad heter mördare?")
detektiv_namn = input("vad heter detective?")
mordare_hp = 100
detektiv_hp = 80

print(f"{mordare_namn} ({mordare_hp} HP) möter {detektiv_namn} ({detektiv_hp} HP)!")
# Ditt första kort börjar här.

while mordare_hp > 0 and detektiv_hp > 0:

    skada_till_detektiv = random.randint(10,20)
    detektiv_hp -= skada_till_detektiv

    print(f"{mordare_namn} slår för {skada_till_detektiv} skada! {detektiv_namn} har {detektiv_hp} HP kvar.")

    if detektiv_hp <= 0:
        break 

    if mordare_hp > 0:
        print (f"{mordare_namn} won!")

    else :
        print (f"{mordare_namn} lost!")


mordare_cooldown = 0
detektiv_cooldown = 0
        
        