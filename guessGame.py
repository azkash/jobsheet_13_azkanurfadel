"""Azka Nur Fadel"""

def guessNumber():
    secret_number = 9  # angka yang perlu di tebak
    guess_count = 0
    guess_limit = 3  # limit melakukan guessing

    while guess_count < guess_limit:
        user = int(input("guess: "))

        if user == secret_number:
            print("Anda berhasil")
            break
        else:
            print("Anda kurang beruntung")
            guess_count += 1
            print("Sisa kesempatan:", guess_limit - guess_count)
    else:
        print("Kesempatan anda habis")
