import matplotlib.pyplot as plt
import matplotlib.animation as animation

def intercalar(list1_length, list2_length):
    # Generar listas con valores fijos de 1 y 2
    list1 = [1] * list1_length
    list2 = [2] * list2_length
    
    ans = list1 + list2 

    # Index del ultimo elemento para identificar hasta donde hacer el swap
    last_element_of_list_1_index = len(list1)-1 
    list2_index = 1
    list1_index = 0
    steps = [ans.copy()]  # Guardamos el estado inicial
    # Intercambiamos los elementos con su opuesto en la otra lista.
    # Dede el centro hacia afuera para no sobreescribir los cambios.
    while len(list2) >= list2_index and len(list1) >= list1_index:
        ans[last_element_of_list_1_index+list2_index], ans[last_element_of_list_1_index-list1_index] = ans[last_element_of_list_1_index-list1_index], ans[last_element_of_list_1_index+list2_index]
        list2_index += 2
        list1_index += 2
        steps.append(ans.copy())  # Guardamos cada paso intermedio
    return steps

# Obtener los pasos intermedios
steps = intercalar(100, 100)
# steps = intercalar(100, 80) # Caso con longitudes distintas
# steps = intercalar(80, 100)

fig, ax = plt.subplots()
bar_container = plt.bar(range(len(steps[0])), steps[0], color=['blue' if x == 1 else 'red' for x in steps[0]])

def animate(i):
    for bar, h, c in zip(bar_container, steps[i], ['blue' if x == 1 else 'red' for x in steps[i]]):
        bar.set_height(h)
        bar.set_color(c)

    ax.set_yticks([1, 2])
    ax.set_yticklabels(['1', '2'])

    ax.set_xlabel('Elementos')
    ax.set_ylabel('Valores')
    ax.set_title('Intercambiamos elementos desde el centro.')

ani = animation.FuncAnimation(fig, animate, frames=len(steps), interval=100)

plt.show()