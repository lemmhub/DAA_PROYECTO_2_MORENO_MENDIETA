import random
from Clases.Grafo import Grafo
from Clases.Arista import Arista
from Clases.Nodo import Nodo
from Clases.Modelos_grafos import grafoMalla, grafoErdosRenyi, grafoGilbert, grafoGeografico, grafoBarabasiAlbert, grafoDorogovtsevMendes
from Clases.Disposiciones import *

def main():
    path = ("C:\\Users\\Precision\\Desktop\\PROYECTO_1\\PROYECTO_4_MORENO_MENDIETA\\GV_FILES")

    Nodos_totales=[500]
    for nodos in Nodos_totales:
        m_erdos = random.randint(nodos+1,nodos*2)
        p_gilbert = random.uniform(0.1,1)
        r_geografico = random.uniform(0.1,1)
        d_barabasi = random.randint(1,nodos)
        malla_a=random.randint(2,nodos)
        malla_b=0
        if (nodos%malla_a==0):
            malla_b=nodos/malla_a
        else:
            while malla_b==0:
                malla_a-=1
                if (nodos%malla_a==0):
                    malla_b=nodos/malla_a
        malla_a=int(malla_a)
        malla_b=int(malla_b)

        #grafito = grafoMalla(*(malla_a,malla_b))
        #grafito.to_graphviz(path + grafito.id + ".gv")
        #grafito.generar_pesos()

        #kruskal = grafito.KruskalD()
        #kruskal.to_graphviz(path + kruskal.id + ".gv")
        #kruskalI = grafito.KruskalI()
        #kruskalI.to_graphviz(path + kruskalI.id + ".gv")
        #prim = grafito.Prim()
        #prim.to_graphviz(path + prim.id + ".gv")
        #print(f'\nMALLA')
        #print(f"MST kruskal: {kruskal.costo()}")
        #print(f"MST kruskalI: {kruskalI.costo()}")
        #print(f"MST Prim: {prim.costo()}")

       



        #grafito = grafoErdosRenyi(nodos, m_erdos)
        #grafito.to_graphviz(path + grafito.id + ".gv")
        #grafito.generar_pesos()
        #kruskal = grafito.KruskalD()
        #kruskal.to_graphviz(path + kruskal.id + ".gv")
        #kruskalI = grafito.KruskalI()
        #kruskalI.to_graphviz(path + kruskalI.id + ".gv")
        #prim = grafito.Prim()
        #prim.to_graphviz(path + prim.id + ".gv")
        #print(f'\nERDOS')
        #print(f"MST kruskal: {kruskal.costo()}")
        #print(f"MST kruskalI: {kruskalI.costo()}")
        #print(f"MST Prim: {prim.costo()}")
        #Proyecto 5




        grafito = grafoGilbert(nodos, p_gilbert, dirigido=False, auto=False)
        # grafito.to_graphviz(path + grafito.id + ".gv")
        # grafito.generar_pesos()
        # kruskal = grafito.KruskalD()
        # kruskal.to_graphviz(path + kruskal.id + ".gv")
        # kruskalI = grafito.KruskalI()
        # kruskalI.to_graphviz(path + kruskalI.id + ".gv")
        # prim = grafito.Prim()
        # prim.to_graphviz(path + prim.id + ".gv")
        # print(f'\nGILBERT')
        # print(f"MST kruskal: {kruskal.costo()}")
        # print(f"MST kruskalI: {kruskalI.costo()}")
        # print(f"MST Prim: {prim.costo()}")

        





        # grafito = grafoGeografico(nodos, r_geografico)
        # grafito.to_graphviz(path + grafito.id + ".gv")
        # grafito.generar_pesos()
        # kruskal = grafito.KruskalD()
        # kruskal.to_graphviz(path + kruskal.id + ".gv")
        # kruskalI = grafito.KruskalI()
        # kruskalI.to_graphviz(path + kruskalI.id + ".gv")
        # prim = grafito.Prim()
        # prim.to_graphviz(path + prim.id + ".gv")
        # print(f'\nGEOGRÁFICO')
        # print(f"MST kruskal: {kruskal.costo()}")
        # print(f"MST kruskalI: {kruskalI.costo()}")
        # print(f"MST Prim: {prim.costo()}")

        




        # grafito = grafoBarabasiAlbert(nodos, d_barabasi, auto=False)
        # grafito.to_graphviz(path + grafito.id + ".gv")
        # grafito.generar_pesos()
        # kruskal = grafito.KruskalD()
        # kruskal.to_graphviz(path + kruskal.id + ".gv")
        # kruskalI = grafito.KruskalI()
        # kruskalI.to_graphviz(path + kruskalI.id + ".gv")
        # prim = grafito.Prim()
        # prim.to_graphviz(path + prim.id + ".gv")
        # print(f'\nBARABASI')
        # print(f"MST kruskal: {kruskal.costo()}")
        # print(f"MST kruskalI: {kruskalI.costo()}")
        # print(f"MST Prim: {prim.costo()}")

       



        # grafito = grafoDorogovtsevMendes(nodos, dirigido=False)
        # grafito.to_graphviz(path + grafito.id + ".gv")
        # grafito.generar_pesos()
        # kruskal = grafito.KruskalD()
        # kruskal.to_graphviz(path + kruskal.id + ".gv")
        # kruskalI = grafito.KruskalI()
        # kruskalI.to_graphviz(path + kruskalI.id + ".gv")
        # prim = grafito.Prim()
        # prim.to_graphviz(path + prim.id + ".gv")
        # print(f'\nDOROGOVSTEV')
        # print(f"MST kruskal: {kruskal.costo()}")
        # print(f"MST kruskalI: {kruskalI.costo()}")
        # print(f"MST Prim: {prim.costo()}")

       
        spring(grafito)

if __name__ == "__main__":
        main()