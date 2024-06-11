import networkx as nx
import sys
from PyQt5.QtWidgets import QApplication, QGraphicsScene, QGraphicsView, QGraphicsEllipseItem, QGraphicsLineItem, QGraphicsTextItem, QGraphicsRectItem
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPen, QBrush, QFont
import tkinter as tk
from tkinter import ttk

class WeightedGraph:
    def __init__(self):
        self.graph = nx.DiGraph()

    def add_edge(self, source, target, weight):
        self.graph.add_edge(source, target, weight=weight)

    def find_shortest_path(self, start, end):
        length, path = nx.single_source_dijkstra(self.graph, start, end)
        return length, path

def find_shortest_path():
    start = entry_start.get()
    end = entry_end.get()
    length, path = G.find_shortest_path(start, end)
    result_text = f"کوتاه ترین مسیر موجود از مبداء {start} به مقصد {end}، مسیر گذرنده از شهرهای {path}، به طول {length} کیلومتر است. سفر شما{length/100} ساعت خواهد بود و هزینه عوارضی این مسیر {length/50} هزار تومان است."
    result_label.config(text=result_text)
    app = QApplication(sys.argv)
    scene = QGraphicsScene()
    node_color = Qt.green
    edge_color = Qt.gray
    text_color = Qt.black
    length, path = G.find_shortest_path(start, end)
    pos = nx.spring_layout(G.graph)
    header_text = QGraphicsTextItem(result_text)
    header_text.setDefaultTextColor(Qt.black) 
    header_text.setFont(QFont("Arial", 12))
    header_text.setPos((-200), (-200))
    scene.addItem(header_text)
    for node in path:
        x, y = pos[node]
        square = QGraphicsRectItem(x*500, y*500, 100, 100)
        square.setBrush(QBrush(node_color))
        scene.addItem(square)
        text = QGraphicsTextItem(node)
        text.setDefaultTextColor(text_color)
        text.setPos(x*500 + 50 - text.boundingRect().width()/2, y*500 + 50 - text.boundingRect().height()/2)
        scene.addItem(text)
    for i in range(len(path)-1):
        source, target = path[i], path[i+1]
        source_x, source_y = pos[source]
        target_x, target_y = pos[target]
        mid_x = (source_x + target_x) / 2
        mid_y = (source_y + target_y) / 2
        line_to_mid = QGraphicsLineItem(source_x*500, source_y*500, mid_x*500, mid_y*500)
        line_to_mid.setPen(QPen(edge_color, 4))
        scene.addItem(line_to_mid)
        line_from_mid = QGraphicsLineItem(mid_x*500, mid_y*500, target_x*500, target_y*500)
        line_from_mid.setPen(QPen(edge_color, 4))
        scene.addItem(line_from_mid)
    view = QGraphicsView(scene)
    view.resize(5000, 5000)
    view.show()
    sys.exit(app.exec_())

G = WeightedGraph()
G.add_edge('اردبیل','آبادان',600)
G.add_edge('اردبیل','تهران',1000)
G.add_edge('اردبیل','همدان',200)
G.add_edge('آبادان', 'اردبیل', 600)
G.add_edge('آبادان', 'همدان', 400)
G.add_edge('آبادان','تهران',1200)
G.add_edge('آبادان','اصفهان',800)
G.add_edge('تهران','آبادان',1200)
G.add_edge('تهران','رشت',500)
G.add_edge('تهران','ساری',300)
G.add_edge('تهران','اردبیل',1000)
G.add_edge('تهران','همدان',700)
G.add_edge('رشت','تهران',500)
G.add_edge('رشت','ساری',400)
G.add_edge('ساری','تهران',300)
G.add_edge('ساری','رشت',400)
G.add_edge('ساری','اصفهان',900)
G.add_edge('اصفهان','ساری',900)
G.add_edge('اصفهان','آبادان',800)
G.add_edge('اصفهان','همدان',500)
G.add_edge('همدان','اصفهان',500)
G.add_edge('همدان','آبادان',400)
G.add_edge('همدان','اردبیل',200)

cities = ['اردبیل','آبادان','تهران','همدان','اصفهان','رشت','ساری']

root = tk.Tk()
root.geometry("500x300")
root.title("مسیریابی")

label_start = tk.Label(root, text="شهر مبداء شما کدام است؟")
label_start.pack()
entry_start = ttk.Combobox(root,width=20)
entry_start.config(values=list(cities),state='readonly')
entry_start.current=(cities[6])
entry_start.pack()

label_end = tk.Label(root, text="شهر مقصد شما کدام است؟")
label_end.pack()
entry_end = ttk.Combobox(root,width=20)
entry_end.config(values=list(cities),state='readonly')
entry_end.current=(0)
entry_end.pack()



button = tk.Button(root, text="!بهترین و کوتاه ترین مسیر را پیدا کن", command=find_shortest_path)
button.pack()
result_label = tk.Label(root, text="")
result_label.pack()
 
root.mainloop()