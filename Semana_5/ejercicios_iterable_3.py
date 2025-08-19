# 3-Cree un programa que intercambie el primer y ultimo elemento de una lista. Debe funcionar con listas de cualquier tamaño.

def names(lst):
    if len(lst) < 2:
        return lst  # Nothing to swap
    lst[0], lst[-1] = lst[-1], lst[0]
    return lst

my_list = ['Robinson', 'Luis', 'Isabelle', 'Bryan', 'Alex']
result = names(my_list)
print(result)
