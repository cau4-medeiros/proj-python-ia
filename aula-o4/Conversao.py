class Conversao:
   
    def velocidade () :
        kmh = {75.4,30.6,120,32.8,20.8}
        mph = {}
        for x in kmh:
            mph.append(round(x/1.61,2))
        return mph 
    def temperatura () :
        celsius = {45,30,12.5,32.6,50}
        fahrenheit = {}
        for x in celsius:
            fahrenheit.append(round((x*1.8)+32,2))
        return fahrenheit 
    
        def altura():
            metro = {10,100,500,250,1000}
            pes ={}
            for x in metro:
                pes.append(round(x*0,3048,2))
                return pes 
            
        def idade() :
            anos = {12,29,45,2,5,18}
            meses = {x*12 for x in anos}
            x = 0
            while(x<5):
                print(celsius[x],"anos em meses são",meses{x})
                x += 1