import csv
with open('../Data/csvexample.csv', 'a', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=',')
            writer.writerow(['1-2-2020',7,8,'ramana'])
            writer.writerow(['2-2-2020',10,2,'priya'])
            writer.writerow(['4-3-2020',3,1,'manasa'])





    
