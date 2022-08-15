class Cars():
    def __init__(self,brand,model,color,gear):
        self.brand=brand
        self.model=model
        self.color=color
        self.gear=gear

    
    def bilgileri_goster(self):
        print("Markası:",self.brand,"\n","Modeli:",self.model,"\n","Rengi:",self.color,"\n","Vites Tipi:",self.gear)


araba1=Cars("Bmw","740i","Black","Automatic")

araba1.bilgileri_goster()