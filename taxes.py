import sys
#import locale


tps=0.05 
tvq=0.09975 
preCost=0.0 #prix avant taxes
cost = 0.0  #
nbArg= int(len(sys.argv))

if nbArg == 1:
    print("Zero arguments, I quit!")
else: 
    if nbArg>1:
        #print("Calcul de la Tps et TVq sur achats:\n")
        for i in range(1, nbArg):
            preCost += float(sys.argv[i])
            #print("preCost: ",preCost)
        
        tpsCost=preCost*tps
        tvqCost=preCost*tvq
        cost = float(float(sys.argv[1]))
        
        # voir comment justifier à droite
        # pour formater en Canadien avec le signe dollar à la fin, les décimales par une virgule et les milliers par des espaces, explorer "locale" ou "set.locale"
        print("\nCoût:", "{:.2f}".format(preCost), "$   Tps:" , "{:.2f}".format(tpsCost) , "$   Tvq:","{:.2f}".format(tvqCost), "$\n")
        print("Coût avec taxes: ", "{:.2f} $".format(preCost+tpsCost+tvqCost), "\n")
        

