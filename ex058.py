import random


num = random.randint(0, 100)
guess = int(input('Olá, sou o seu computador e acabei de pensar num número. Tente adivinhar o número que eu pensei entre 0 à 100: '))
palpites = 1
acertou = False
if guess == num:
    print(f"Parabéns, você acertou! Foi necessária apenas uma tentativa para você ganhar, impressionante!!!")
else:
    while guess != num or acertou == False:
        palpites += 1
        if guess == num:
            acertou = True
            print(
                f"Parabéns, você acertou! Foram necessários {palpites} tentativa(s) para você ganhar!")
        elif (guess - num) < 5 and (num - guess) < 5:
            guess = int(input(
                f'Seu palpite foi [{guess}], e ele está: QUENTE IGUAL UM VULCANO! Tente novamente: '))
        elif (guess - num) < 10 and (num - guess) < 10:
            guess = int(
                input(f'Seu palpite foi [{guess}], e ele está: QUENTE! Tente novamente: '))
        elif (guess - num) < 30 and (num - guess) < 30:
            guess = int(
                input(f'Seu palpite foi [{guess}], e ele está: Morno! Tente novamente: '))
        elif (guess - num) < 70 and (num - guess) < 70:
            guess = int(
                input(f'Seu palpite foi [{guess}], e ele está: Frio! Tente novamente: '))
        else:
            guess = int(input(
                f'Seu palpite foi [{guess}], e ele está: Frio congelante! Não sabia que era possível ser tão ruim assim nesse jogo!'))
