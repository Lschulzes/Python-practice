import random


guess = int(input('Tente adivinhar o número que eu estou pensando entre 0 à 5: '))
num = random.randint(0, 5)
if guess == num:
    print("Parabéns, você acertou!")
else:
    print(f"Você errou! O número era {num}, e você chutou {guess}")
