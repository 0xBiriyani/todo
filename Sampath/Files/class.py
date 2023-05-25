class Naruto_Shippuden:
    def __init__(sampath, name, village, jutsu):
        sampath.name = name
        sampath.village = village
        sampath.jutsu = jutsu

    def jutsu_used(sampath):
        print(f"{sampath.name} uses {sampath.jutsu}")

Naruto = Naruto_Shippuden("Naruto Uzumaki", "Hidden Leaf Village", "Rasengan")
Gaara = Naruto_Shippuden("Gaara", "Hidden Sand Village", "Sand Coffin")
Raikage = Naruto_Shippuden("Raikage", "Hidden Cloud Village", "Lightning Release: Lariat")


print(Naruto.name)        
print(Naruto.village)     
print(Naruto.jutsu)  
Naruto.jutsu_used()  
print("\n")  

print(Gaara.name)    
print(Gaara.village)   
print(Gaara.jutsu)
Gaara.jutsu_used() 
print("\n")        

print(Raikage.name)
print(Raikage.village)
print(Raikage.jutsu)
Raikage.jutsu_used()
print("\n")