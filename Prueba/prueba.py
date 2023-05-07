import csv

datos = [["Nicolas", "Piccart"],
         ["Esteban", "Benetti"],
         ["Agustin", "Gomez"]]

with open('receptor.csv', 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerows(datos)
