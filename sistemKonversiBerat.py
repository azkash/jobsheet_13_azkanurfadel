"""Azka Nur Fadel"""
def weight_conversion():


    def kg_to_lbs(weight_kg):
        # 1 kg = 2.20462 lbs
        return weight_kg * 2.20462

    def lbs_to_kg(weight_lbs):
        # 1 lbs = 0.453592 kg
        return weight_lbs * 0.453592

    jenis_konversi = input("Pilih jenis konversi\n(kg to lbs[kg] / lbs to kg[lbs]): ").lower()

    if jenis_konversi == "kg":
        weight_kg = float(input("Masukkan berat badan dalam kilogram: "))
        hasil = kg_to_lbs(weight_kg)
        print(f"{weight_kg} kg sama dengan {hasil:.2f} lbs")
        
    elif jenis_konversi == "lbs":
        weight_lbs = float(input("Masukkan berat badan dalam pound: "))
        hasil = lbs_to_kg(weight_lbs)
        print(f"{weight_lbs} lbs sama dengan {hasil:.2f} kg")
        
    else:
        print("Jenis konversi tidak valid. Silakan pilih '(kg to lbs[kg] / lbs to kg[lbs]'.")
