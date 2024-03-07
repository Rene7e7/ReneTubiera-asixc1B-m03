import pinche

def mostrarIngredients(ingredients):

   for i in ingredients:

       print(i)



def ferTruita():

   print("CUINER: Estic fent truita")

   ingredients=pinche.comprarIngredientsTruita()
   pinche.pelarPatates()
   pinche.cuino_ous()
   mostrarIngredients(ingredients)



def ferMacarrons():

   print("CUINER: Estic fent MAcarrons")

   ingredients=pinche.comprarIngredientsMacarrons()

   mostrarIngredients(ingredients)

def ferSushi():

   print("CUINER: Estic fent Sushi")

   ingredients=pinche.comprarIngredientsSushi()
   pinche.Cuinar_arros()
   mostrarIngredients(ingredients)
