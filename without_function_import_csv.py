import csv
with open('../Data/example.csv', 'a', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=',')
            writer.writerow(['1-2-2019',7,8,'ram'])
            writer.writerow(['2-4-2019',10,2,'priyanka'])
            writer.writerow(['4-4-2019',3,1,'manashi'])





    
