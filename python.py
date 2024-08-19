import random

def tas_kagit_makas_Sude_Rabia_Karaaslan():
    print('Welcome to the game')
    print('Rule1: There are 3 characters: Tas, Kagıt, and Makas. Kagıt wins against Tas, Tas wins against Makas, Makas wins against Kagıt')
    print('Rule2: The player who reaches 3 points wins')

    choices = ["Tas", "Kagıt", "Makas"]
    user_score = 0
    computer_score = 0

    while user_score < 3 and computer_score < 3:
        # Secim yapma
        user_choice = input("Choose Tas, Kagıt, or Makas: ").capitalize()

        # Kullanıcının geçersiz bir seçim yapması
        if user_choice not in choices:
            print("Seçenek değil. Lütfen seçeneklerden birini yazınız: Tas, Kagıt, veya Makas.")
            continue  # Bu turu atla ve bir sonraki tur için döngüye devam et

        # Bilgisayarın rastgele bir seçim yapması
        computer_choice = random.choice(choices)

        print(f"You chose {user_choice}, computer chose {computer_choice}")

        # Kazananın belirlenmesi
        if user_choice == computer_choice:
            print("No point. Try again.")
        elif (
            (user_choice == 'Tas' and computer_choice == 'Makas') or
            (user_choice == 'Kagıt' and computer_choice == 'Tas') or
            (user_choice == 'Makas' and computer_choice == 'Kagıt')
        ):
            print("Congrats! You win one point.")
            user_score += 1
        else:
            print("You lost. Computer wins one point.")
            computer_score += 1

        print(f"Score: You {user_score} - Computer {computer_score}")

    # Sonuc
    if user_score > computer_score
        print("Game finished. Congrats, you won!")
    else:
        print("Game finished. Sorry, you lost.")
tas_kagit_makas_Sude_Rabia_Karaaslan()
