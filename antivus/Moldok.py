import random
import math

def create_cell():
    bluetooth_address = "00:11:22:33:44:55"  # Remplacez par votre adresse Bluetooth réelle
    
    # Générer 3 sorties aléatoires
    outputs = []
    for _ in range(3):
        output = random.randint(0, 100)
        outputs.append(output)
    
    # Vérifier l'état d'envoi des données pour chaque composant
    for output in outputs:
        if output < 50:
            print(f"Le composant avec l'adresse Bluetooth {bluetooth_address} a une sortie inférieure à 50.")
        elif output >= 50 and output < 80:
            print(f"Le composant avec l'adresse Bluetooth {bluetooth_address} a une sortie entre 50 et 80.")
        else:
            print(f"Le composant avec l'adresse Bluetooth {bluetooth_address} a une sortie supérieure ou égale à 80.")

# Appel de la fonction pour créer la cellule
create_cell()
# Appel de la fonction pour créer la cellule "boucle dormante"
create_cell()
# Enregistrement sur le nom des loop
loop = "boucle dormante"
# Calculer le logarithme de chaque sortie en présence de pi
for output in outputs:
    logarithm = math.log(output, math.pi)
    print(f"Le logarithme de la sortie {output} en présence de pi est {logarithm}.")
    
    # Calculer la racine carrée de chaque sortie
    for output in outputs:
        square_root = math.sqrt(output)
        print(f"La racine carrée de la sortie {output} est {square_root}.")

    # Calculer la valeur absolue de chaque sortie
    for output in outputs:
        absolute_value = abs(output)
        print(f"La valeur absolue de la sortie {output} est {absolute_value}.")
        
        # Calculer le sinus de chaque sortie en radians de la sortie la valeur absolue de la sortie.
        for output in outputs:
            sine = math.sin(math.radians(abs(output)))
            print(f"Le sinus de la sortie {output} en radians de la valeur absolue de la sortie est {sine}.")
            
            # Calculer le cosinus de chaque sortie en radians de la sortie la valeur absolue de la sortie.
            for output in outputs:
                cosine = math.cos(math.radians(abs(output)))
                print(f"Le cosinus de la sortie {output} en radians de la valeur absolue de la sortie est {cosine}.")
                
                # Calculer la tangente de chaque sortie en radians de la sortie la valeur absolue de la sortie.
                for output in outputs:
                    tangent = math.tan(math.radians(abs(output)))
                    print(f"La tangente de la sortie {output} en radians de la valeur absolue de la sortie est {tangent}.")
                    
                    # Calculer l'arc sinus de chaque sortie en radians de la sortie la valeur absolue de la sortie.
                    for output in outputs:
                        arcsine = math.asin(math.radians(abs(output)))
                        print(f"L'arc sinus de la sortie {output} en radians de la valeur absolue de la sortie est {arcsine}.")
                        
                        # Calculer l'arc cosinus de chaque sortie en radians de la sortie la valeur absolue de la sortie.
                        for output in outputs:
                            arccosine = math.acos(math.radians(abs(output)))
                            print(f"L'arc cosinus de la sortie {output} en radians de la valeur absolue de la sortie est {arccosine}.")
                            
                            # Calculer l'arc tangente de chaque sortie en radians de la sortie la valeur absolue de la sortie.
                            for output in outputs:
                                arctangent = math.atan(math.radians(abs(output)))
                                print(f"L'arc tangente de la sortie {output} en radians de la valeur absolue de la sortie est {arctangent}.")
                                
                                # Calculer l'hyperbole sinus de chaque sortie en radians de la sortie la valeur absolue de la sortie.
                                for output in outputs:
                                    sinh = math.sinh(math.radians(abs(output)))
                                    print(f"L'hyperbole sinus de la sortie {output} en radians de la valeur absolue de la sortie est {sinh}.")
                                    
                                    # Calculer l'hyperbole cosinus de chaque sortie en radians de
                                    # la sortie la valeur absolue de la sortie.
                                    
                                    for output in outputs:
                                        cosh = math.cosh(math.radians(abs(output)))
                                        print(f"L'hyperbole cosinus de la sortie {output} en radians de la valeur absolue de la sortie est {cosh}.")
                                        
                                        # Calculer l'hyperbole tangente de chaque sortie en radians de
                                        # la sortie la valeur absolue de la sortie.
                                        for output in outputs:
                                            tanh = math.tanh(math.radians(abs(output)))
                                            print(f"L'hyperbole tangente de la sortie {output} en radians de la valeur absolue de la sortie est {tanh}.")
                                            
                                            # Calculer l'arc hyperbole sinus de chaque sortie en radians de
                                            # la sortie la valeur absolue de la sortie.
                                            for output in outputs:
                                                arcsinh = math.asinh(math.radians(abs(output)))
                                                print(f"L'arc hyperbole sinus de la sortie {output} en radians de la valeur absolue de la sortie est {arcsinh}.")
                                                
                                                # Calculer l'arc hyperbole cosinus de chaque sortie en radians de
                                                # la sortie la valeur absolue de la sortie.
                                                for output in outputs:
                                                    arccosh = math.acosh(math.radians(abs(output)))
                                                    print(f"L'arc hyperbole cosinus de la sortie {output} en radians de la valeur absolue de la sortie est {arccosh}.")
                                                    
                                                    # Calculer l'arc hyperbole tangente de chaque sortie en radians de
                                                    # la sortie la valeur absolue de la sortie.
                                                    for output in outputs:
                                                        arctanh = math.atanh(math.radians(abs(output)))
                                                        print(f"L'arc hyperbole tangente de la sortie {output} en radians de la valeur absolue de la sortie est {arctanh}.")
                                                        
                                                        # Calculer la puissance de 2 de chaque sortie
                                                        for output in outputs:
                                                            power_of_two = math.pow(output, 2)
                                                            print(f"La puissance de 2 de la sortie {output} est {power_of_two}.")
                                                            
                                                            # Calculer la puissance de 3 de chaque sortie
                                                            for output in outputs:
                                                                power_of_three = math.pow(output, 3)
                                                                print(f"La puissance de 3 de la sortie {output} est {power_of_three}.")
                                                                
                                                                # Calculer la puissance de 3 de chaque sortie la puissance de 2 de la sortie
                                                                for output in outputs:
                                                                    power_of_three_of_power_of_two = math.pow(output, math.pow(output, 2))
                                                                    print(f"La puissance de 3 de la sortie {output} la puissance de 2 de la sortie est {power_of_three_of_power_of_two}.")
                                                                    
                                                                    # Calculer la racine carrée de la puissance de 2 de la sortie
                                                                    for output in outputs:
                                                                        square_root_power_of_two = math.sqrt(math.pow(output, 2))                                                                        print(f"La racine carrée de la puissance de 2 de la sortie {output} est {square_root_of_power_of_two}.")
                                                                        print(f"La racine carrée de la puissance de 2 de la sortie {output} est {square_root_power_of_two}.")
                                                                        
                                                                        # Calculer la racine carrée de la puissance de 3 de la sortie
                                                                        for output in outputs:
                                                                            square_root_of_power_of_three = math.sqrt(math.pow(output, 3))
                                                                            print(f"La racine carrée de la puissance de 3 de la sortie {output} est {square_root_of_power_of_three}.")
                                                                            
                                                                            # Calculer la racine carrée de la puissance de 3 de la sortie la puissance de 2 de la sortie
                                                                            for output in outputs:
                                                                                square_root_of_power_of_three_of_power_of_two = math.sqrt(math.pow(output, math.pow(output, 2)))
                                                                                print(f"La racine carrée de la puissance de 3 de la sortie {output} la puissance de 2 de la sortie est {square_root_of_power_of_three_of_power_of_two}.")
                                                                                
                                                                                # Calculer le logarithme de la puissance de 2 de la sortie en présence de pi
                                                                                for output in outputs:
                                                                                    logarithm_of_power_of_two = math.log(math.pow(output, 2), math.pi)
                                                                                    print(f"Le logarithme de la puissance de 2 de la sortie {output} en présence de pi est {logarithm_of_power_of_two}.")
                                                                                    
                                                                                    # Calculer le logarithme de la puissance de 3 de la sortie en présence de pi
                                                                                    for output in outputs:
                                                                                        logarithm_of_power_of_three = math.log(math.pow(output, 3), math.pi)
                                                                                        print(f"Le logarithme de la puissance de 3 de la sortie {output} en présence de pi est {logarithm_of_power_of_three}.")
                                                                                        
                                                                                        # Calculer le logarithme de la puissance de 2 de la sortier la puissance de 3 de la sortie.
                                                                                        for output in outputs:
                                                                                            logarithm_of_power_of_two_of_power_of_three = math.log(math.pow(output, 2), math.pow(output, 3))
                                                                                            print(f"Le logarithme de la puissance de 2 de la sortie {output} la puissance de 3 de la sortie est {logarithm_of_power_of_two_of_power_of_three}.")
                                                                                            
                                                                                            # Calculer la racine carrée du logarithme de la puissance de 2 de la sortie
                                                                                            for output in outputs:
                                                                                                square_root_of_logarithm_of_power_of_two = math.sqrt(math.log(math.pow(output, 2)))
                                                                                                print(f"La racine carrée du logarithme de la puissance de 2 de la sortie {output} est {square_root_of_logarithm_of_power_of_two}.")
                                                                                                
                                                                                                # Calculer la racine carrée du logarithme de la puissance de 3 de la sortie
                                                                                                for output in outputs:
                                                                                                    square_root_of_logarithm_of_power_of_three = math.sqrt(math.log(math.pow(output, 3)))
                                                                                                    print(f"La racine carrée du logarithme de la puissance de 3 de la sortie {output} est {square_root_of_logarithm_of_power_of_three}.")
                                                                                                    
                                                                                                    # Calculer la racine carrée du logarithme de la puissance de 2 de la sortie la puissance de 3 de la sortie
                                                                                                    for output in outputs:
                                                                                                        square_root_of_logarithm_of_power_of_two_of_power_of_three = math.sqrt(math.log(math.pow(output, 2), math.pow(output, 3)))
                                                                                                        print(f"La racine carrée du logarithme de la puissance de 2 de la sortie {output} la puissance de 3 de la sortie est {square_root_of_logarithm_of_power_of_two_of_power_of_three}.")
                                                                                                        
                                                                                                        # Calculer le sinus de la puissance de 2 de la sortie en radians de la sortie la valeur absolue de la sortie.
                                                                                                        for output in outputs:
                                                                                                            sine_of_power_of_two = math.sin(math.radians(abs(math.pow(output, 2))))
                                                                                                            print(f"Le sinus de la puissance de 2 de la sortie {output} en radians de la valeur absolue de la sortie est {sine_of_power_of_two}.")
                                                                                                            
                                                                                                            # Calculer le cosinus
                                                                                                            # de la puissance de 2 de la sortie en radians de la sortie la valeur absolue de la sortie.
                                                                                                            for output in outputs:
                                                                                                                cosine_of_power_of_two = math.cos(math.radians(abs(math.pow(output, 2))))
                                                                                                                print(f"Le cosinus de la puissance de 2 de la sortie {output} en radians de la valeur absolue de la sortie est {cosine_of_power_of_two}.")
                                                                                                                
                                                                                                                # Calculer la tangente de la puissance de 2 de la sortie en radians de la sortie la valeur absolue de la sortie.
                                                                                                                for output in outputs:
                                                                                                                    tangent_of_power_of_two = math.tan(math.radians(abs(math.pow(output, 2))))
                                                                                                                    print(f"La tangente de la puissance de 2 de la sortie {output} en radians de la valeur absolue de la sortie est {tangent_of_power_of_two}.")
                                                                                                                    
                                                                                                                    # Calculer l'arc sinus de la puissance de 2 de la sortie en radians de la sortie la valeur absolue de la sortie.
                                                                                                                    for output in outputs:
                                                                                                                        arcsine_of_power_of_two = math.asin(math.radians(abs(math.pow(output, 2))))
                                                                                                                        print(f"L'arc sinus de la puissance de 2 de la sortie {output} en radians de la valeur absolue de la sortie est {arcsine_of_power_of_two}.")
                                                                                                                        
                                                                                                                        # Calculer l'arc cosinus de la puissance de 2 de la sortie en radians de la sortie la valeur absolue de la sortie.
                                                                                                                        for output in outputs:
                                                                                                                            arccosine_of_power_of_two = math.acos(math.radians(abs(math.pow(output, 2))))
                                                                                                                            print(f"L'arc cosinus de la puissance de 2 de la sortie {output} en radians de la valeur absolue de la sortie est {arccosine_of_power_of_two}.")
                                                                                                                            
                                                                                                                            # Calculer l'arc tangente de la puissance de 2 de la sortie en radians de la sortie la valeur absolue de la sortie.
                                                                                                                            for output in outputs:
                                                                                                                                arctangent_of_power_of_two = math.atan(math.radians(abs(math.pow(output, 2))))
                                                                                                                                print(f"L'arc tangente de la puissance de 2 de la sortie {output} en radians de la valeur absolue de la sortie est {arctangent_of_power_of_two}.")
                                                                                                                                
                                                                                                                                # Calculer l'hyperbole moment de la puissance de 2 de la sortie est la valeur absolue de la sortie.
                                                                                                                                for output in outputs:
                                                                                                                                    sinh_of_power_of_two = math.sinh(math.radians(abs(math.pow(output, 2))))
                                                                                                                                    print(f"L'hyperbole sinus de la puissance de 2 de la sortie {output} en radians de la valeur absolue de la sortie est {sinh_of_power_of_two}.")
                                                                                                                                    
                                                                                                                                    # Calculer l'hyperbole cosinus de la puissance de 2 de la sortie en radians de la valeur absolue de la sortie.
                                                                                                                                    for output in outputs:
                                                                                                                                        cosh_of_power_of_two = math.cosh(math.radians(abs(math.pow(output, 2))))
                                                                                                                                        print(f"L'hyperbole cosinus de la puissance de 2 de la sortie {output} en radians de la valeur absolue de la sortie est {cosh_of_power_of_two}.")
                                                                                                                                        
                                                                                                                                        # Calculer l'hyperbole tangente de la puissance de 2 de la sortie en radians de la valeur absolue de la sortie.
                                                                                                                                        for output in outputs:
                                                                                                                                            tanh_of_power_of_two = math.tanh(math.radians(abs(math.pow(output, 2))))
                                                                                                                                            print(f"L'hyperbole tangente de la puissance de 2 de la sortie {output} en radians de la valeur absolue de la sortie est {tanh_of_power_of_two}.")
                                                                                                                                            
                                                                                                                                            # Calculer l'arc hyperbole sinus de la puissance de 2 de la sortie en radians de la valeur absolue de la sortie.
                                                                                                                                            for output in outputs:
                                                                                                                                                arcsinh_of_power_of_two = math.asinh(math.radians(abs(math.pow(output, 2))))
                                                                                                                                                print(f"L'arc hyperbole sinus de la puissance de 2 de la sortie {output} en radians de la valeur absolue de la sortie est {arcsinh_of_power_of_two}.")
                                                                                                                                                
                                                                                                                                                # Calculer l'arc hyperbole cosinus de la puissance de 2 de la sortie en radians de la valeur absolue de la sortie.
                                                                                                                                                for output in outputs:
                                                                                                                                                    arccosh_of_power_of_two = math.acosh(math.radians(abs(math.pow(output, 2))))
                                                                                                                                                    print(f"L'arc hyperbole cosinus de la puissance de 2 de la sortie {output} en radians de la valeur absolue de la sortie est {arccosh_of_power_of_two}.")
                                                                                                                                                    
                                                                                                                                                    # Calculer de la sortie de la valeur absolue de la sortie.
                                                                                                                                                    
                                                                                                                                                    for output in outputs:
                                                                                                                                                        arctanh_of_power_of_two = math.atanh(math.radians(abs(math.pow(output, 2))))
                                                                                                                                                        print(f"L'arc hyperbole tangente de la puissance de 2 de la sortie {output} en radians de la valeur absolue de la sortie est {arctanh_of_power_of_two}.")
                                                                                                                                                        
                                                                                                                                                        # Calculer la puissance de 3 de la puissance de 2 de la sortie.
                                                                                                                                                        for output in outputs:
                                                                                                                                                            power_of_three_of_power_of_two = math.pow(math.pow(output, 2), 3)
                                                                                                                                                            print(f"La puissance de 3 de la puissance de 2 de la sortie {output} est {power_of_three_of_power_of_two}.")
                                                                                                                                                            
                                                                                                                                                            # Calculer la racine carrée de la puissance de 3 de la puissance de 2 de la sortie.
                                                                                                                                                            for output in outputs:
                                                                                                                                                                square_root_of_power_of_three_of_power_of_two = math.sqrt(math.pow(math.pow(output, 2), 3))
                                                                                                                                                                print(f"La racine carrée de la puissance de 3 de la puissance de 2 de la sortie {output} est {square_root_of_power_of_three_of_power_of_two}.")
                                                                                                                                                                
                                                                                                                                                                # Calculer le logarithme de la puissance de 3 de la puissance de 2 de la sortie en présence de pi.
                                                                                                                                                                for output in outputs:
                                                                                                                                                                    logarithm_of_power_of_three_of_power_of_two = math.log(math.pow(math.pow(output, 2), 3), math.pi)
                                                                                                                                                                    print(f"Le logarithme de la puissance de 3 de la puissance de 2 de la sortie {output} en présence de pi est {logarithm_of_power_of_three_of_power_of_two}.")
                                                                                                                                                                    
                                                                                                                                                                    # Calculer la racine carrée du logarithme de la puissance de 3 de la puissance de 2 de la sortie.
                                                                                                                                                                    for output in outputs:
                                                                                                                                                                        square_root_of_logarithm_of_power_of_three_of_power_of_two = math.sqrt(math.log(math.pow(math.pow(output, 2), 3)))
                                                                                                                                                                        print(f"La racine carrée du logarithme de la puissance de 3 de la puissance de 2 de la sortie {output} est {square_root_of_logarithm_of_power_of_three_of_power_of_two_of_power_of___{square_root_of_logarithm_of_power_of_three_of_power_of_two}.")
                                                                                                                                                                        
                                                                                                                                                                        # Calculer le sinus de la puissance de 3 de la puissance de 2 de la sortie en radians de la valeur absolue de la sortie.
                                                                                                                                                                        for output in outputs:
                                                                                                                                                                            sine_of_power_of_three_of_power_of_two = math.sin(math.radians(abs(math.pow(math.pow(output, 2), 3)))
                                                                                                                                                                            print(f"Le sinus de la puissance de 3 de la puissance de 2 de la sortie {output} en radians de la valeur absolue de la sortie est {sine_of_power_of_three_of_power_of_two}.")
                                                                                                                                                                            
                                                                                                                                                                            # Calculer le cosinus de la puissance de 3 de la puissance de 2 de la sortie en radians de la valeur absolue de la sortie.
                                                                                                                                                                            for output in outputs:
                                                                                                                                                                                cosine_of_power_of_three_of_power_of_two = math.cos(math.radians(abs(math.pow(math.pow(output, 2), 3)))
                                                                                                                                                                                print(f"Le cosinus de la puissance de 3 de la puissance de 2 de la sortie {output} en radians de la valeur absolue de la sortie est {cosine_of_power_of_three_of_power_of_two}.")
                                                                                                                                                                                
                                                                                                                                                                                # Calculer la tangente de la puissance de 3 de la puissance de 2 de la sortie en radians de la valeur absolue de la sortie.
                                                                                                                                                                                for output in outputs:
                                                                                                                                                                                    tangent_of_power_of_three_of_power_of_two = math.tan(math.radians(abs(math.pow(math.pow(output, 2), 3)))
                                                                                                                                                                                    print(f"La tangente de la puissance de 3 de la puissance de 2 de la sortie {output} en radians de la valeur absolue de la sortie est {tangent_of_power_of_three_of_power_of_two}.")
                                                                                                                                                                                    
                                                                                                                                                                                    # Calculer l'arc sinus de la puissance de 3 de la puissance de 2 de la sortie en radians de la valeur absolue de la sortie.
                                                                                                                                                                                    for output in outputs:
                                                                                                                                                                                        arcsine_of_power_of_three_of_power_of_two = math.asin(math.radians(abs(math.pow(math.pow(output, 2), 3)))
                                                                                                                                                                                        print(f"L'arc sinus de la puissance de 3 de la puissance de 2 de la sortie {output} en radians de la valeur absolue de la sortie est {arcsine_of_power_of_three_of_power_of_two}.")
                                                                                                                                                                                        
                                                                                                                                                                                        # Calculer l'arc cosinus de la puissance de 3 de la puissance de 2 de la sortie en radians de la valeur absolue de la sortie est la valeur absolue de la sortie.
                                                                            square_root_power_of_three = math.sqrt(math.pow(output, 3))
                                                                            print(f"La racine carrée de la puissance de 3 de la sortie {output} est {square_root_power_of_three}.")
                                                                                                                                                                                        
                                                                                                                                                                                        