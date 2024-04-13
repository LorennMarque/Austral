#   
def intercalar(list1, list2):
    # Nueva lista juntando las anteriores
    ans = list1 + list2 

    # Index del ultimo elemento para identificar hasta donde hacer el swap
    list1_last_index = len(list1)-1 

    list2_index = 1
    list1_index = 0
    # Intercambiamos los elementos con su opuesto en la otra lista.
    # Dede el centro hacia afuera para no sobreescribir los cambios.
    while len(list2) >= list2_index and len(list1) >= list1_index:
        ans[list1_last_index+list2_index], ans[list1_last_index-list1_index] = ans[list1_last_index-list1_index], ans[list1_last_index+list2_index]
        list2_index += 2
        list1_index += 2
    print(ans)

intercalar([1,1,1,1,1,1,1,1,1],[2,2,2,2,2,2,2,2,2,2])

# Con el archivo visualize.py se puede ver una animación que ilustra este proceso.
#Nota: En la linea 27 y 28 de visualize.py hay algunos casos donde el algoritmo se ve limitado por la cantidad de elementos.
