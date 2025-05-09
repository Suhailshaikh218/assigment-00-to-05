# mad_libs_urdu.py

print("👋 Mad Libs Game mein خوش آمدید!")
print("Zaroori lafz daaliye taake humari kahani complete ho sake:\n")

# User se input lena
sifat1 = input("Koi aik sifat (adjective) likhiye: ")
ism1 = input("Koi ek cheez ka naam (noun) likhiye: ")
fail_mazi = input("Koi aisa fail jo guzishta waqt mein hua ho (past tense verb) likhiye: ")
halat = input("Koi tareeqa (adverb) likhiye, jaise 'jaldi', 'dheere': ")
ism2 = input("Ek aur noun likhiye: ")
ism3 = input("Aur aik noun likhiye: ")
sifat2 = input("Aik aur sifat (adjective) likhiye: ")

# Kahani banana
kahani = f"""
Aaj mein zoo gaya. Wahan maine dekha ek {sifat1} {ism1} jo pedh par uchaal raha tha.
Woh {fail_mazi} {halat} ek bade se surang ke zariye jo jaata tha ek {sifat2} {ism2} tak.
Maine kuch moong phali li aur usko pinjray ke andar diya ek bohat bade {ism3} ko.
Sab bohat mazedar tha!
"""

# Kahani print karna
print("\n📜 Aapki Mad Libs Kahani:")
print(kahani)
