from ast import If
from posixpath import split
import sys

#DEFINIMOS LA CLASE BUDDY
class buddy:
    
    #CONSTRUCTOR
    def __init__(self, size, Begin, mbuddy):
        self.size = size
        self.size_occu = 0
        self.begin = Begin
        self.Mbuddy = mbuddy
        self.Status = True
        self.name = ""
        self.father = None
        self.leftChild = None
        self.rightChild = None

    #LA SEPARACIÓN DEL BUDDY EN SUS HIJOS
    def split_buddy(self):

        if self.size == 1:
            return False
        
        lchild = buddy(self.size/2,self.begin + self.begin,None)
        rchild = buddy(self.size/2,self.begin +self.size/2,lchild)
        lchild.father = self
        rchild.father = self

        lchild.Mbuddy = rchild
        self.Status = False

        return (lchild, rchild)

    #LA RECONSTRUCCIÓN DEL PADRE EN BASE A LOS HIJOS
    def unite_buddy(self):

        self.leftChild = None
        self.rightChild = None
        self.Status = True
        return self

    #RESERVAR LA INFORMACIÓN( SImulación)
    def reserve_buddy(self,name, space):
        self.name = name
        self.Status = False
        self.size_occu = space

    #LIBERAR EL ESPACIO RESERVADO(SIMULACIÓN)
    def free_buddy(self):
        self.Status =True
        self.name = ""
        self.size_occu = 0


def main(argv):
    
    free_buddys = []
    full_buddys = []
    
    #Verificamos ligeramente que la entrada funcione
    if len(argv) != 2:
        print("Usage: python buddy.py [\"Quantity of Memory to simulate\"]")
    else:
        
        memory_size = int(argv[1])
        #Dado el numero de memoria introducido, la descomponemos en potencias de 2
        #Y creamos lo Buddys Iniciales
        potencia = 1
        while memory_size !=0 :
            if((potencia * 2)> memory_size) and (potencia <= memory_size ):
                free_buddys.append(buddy( potencia, 0,None))
                memory_size = memory_size - potencia
                potencia = 1
            else:
                potencia = potencia *2 
        
        #MENU INTERACTIVO
        while True:
            err = False

            entrada = input("Tell your order Master: ")
            tokens=entrada.split()

            #RESERVAS ESPACIOS DE MEMORIA
            if(tokens[0] == "RESERVAR"):

                #PRIMERO SE BUSCA SI YA EXISTE UN ESPACIO RESERVADO CON ESE NOMBRE
                buddy_found = None
                for element in full_buddys: 
                    if element.name == tokens[1]:
                        print("!!!Ya hay un espacio reservado con este nombre!!!")
                        err = True

                if(int(tokens[2]) == 0):
                    print("!!!NO PUEDES RESERVAR UNA PARTICIÓN DE TAMANO 0!!!")
                    err = True

                #SI NO HAY UN NOMBRE YA OCUPADO, SE BUSCA EL ESPACIO MÁS PEQUEÑO PARA LA MEMORIA A RESERVAR
                if  (err == False):
                    for element in free_buddys:
                        if element.size >= int(tokens[2]):
                            if buddy_found == None:
                                buddy_found = element
                            elif element.size < buddy_found.size:
                                buddy_found = element
                                        
                    if(buddy_found ==  None):
                        print("!!!No hay espacio suficiente para poder reservar la cantidad de memoria pedido!!!")
                    else:
                        #SI LA MEMORIA ES MUY GRANDE, SE VA DIVIDIENDO HASTA LO MÁS PEQUEÑO QUE PUEDA PERO AUN SIGA ENTRADO
                        while True :
                            if(buddy_found.size /2) >= int(tokens[2]):
                                free_buddys.remove(buddy_found)
                                [lchild,rchild] = buddy_found.split_buddy()
                                free_buddys.append(lchild)
                                free_buddys.append(rchild)
                                buddy_found = lchild
                                
                            else:
                                break
                        
                        buddy_found.reserve_buddy(tokens[1], int(tokens[2]))
                        full_buddys.append(buddy_found)
                        free_buddys.remove(buddy_found)
            
            #SE LIBERA EL ESPACIO DE MEMORIA, Y DE SER POSIBLE SE VUELVEN A JUNTAR LOS BUDDYS
            elif(tokens[0] == "LIBERAR"):
                
                #SE BUSCA PRIMERO SI EXISTE LA PARTICIÓN A LIBERAR 
                buddy_found = None
                for element in full_buddys:
                    if element.name == tokens[1]:
                        buddy_found = element

                #SI NO LA CONSIGUE SUELTA UN ERROR, DE CONSEGUIRLA LA LIBERA Y LUEGO REVISA SI ES POSIBLE UNIR LOS BUDDYS
                if buddy_found == None:
                    print("!!! No existe Partición con el nombre provisto")
                else:
                    buddy_found.free_buddy()
                    full_buddys.remove(buddy_found)
                    free_buddys.append(buddy_found)

                    for element in free_buddys:
                        if element.father != None and element.leftChild == None:
                            if element.Status and element.Mbuddy.Status:
                                free_buddys.remove(element)
                                free_buddys.remove(element.Mbuddy)
                                free_buddys.append(element.father)
                                element.father.unite_buddy()

            #EL DESPLIEGUE DE INFORMACIÓN
            elif(tokens[0] == "MOSTRAR"):
                print()
                print("<><><><>BLOQUES LLENOS DE MEMORIA<><><><>")
                for element in full_buddys:
                    print("------Nombre de la Partición: ",element.name ,"-----")
                    print("Partición de tamaño: ", element.size, ",con un espacicio ocupado de: ", element.size_occu)

                print()
                print("<><><><>BLOQUES VACIOS DE MEMORIA<><><><>")

                print("-----CANTIDAD DE BLOQUES VACIOS: ",len(free_buddys),"-----" )
                for element in free_buddys:
                    print("Partición de ", element.size, "libre.")
                print()

            elif(tokens[0] == "SALIR"):
                break
            else:
                pass

        
if __name__ == '__main__':
    main(sys.argv)