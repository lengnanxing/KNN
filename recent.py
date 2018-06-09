for passenger in f0:
    passenger0 = []
    for i in range (12):
        if i==3:
            continue
        if passenger[i]=="":
            passenger[i]="0"
        passenger0.append(passenger[i])
    csv_write.writerow(passenger0)
    print(passenger0)

f0=csv.reader(open("train1.csv","r"))
f1=csv.reader(open("train_Ticket0.csv","r"))
f2=csv.reader(open("train_Cabin0.csv","r"))
out=open("tri.csv","a",newline="")
csv_write=csv.writer(out,dialect="excel")
train=[]
ticket=[]
cabin=[]
for tri in f0:
    train.append(tri)
for tic in f1:
    ticket.append(tic)
for cab in f2:
    cabin.append(cab)
f0=csv.reader(open("train1.csv","r"))
f1=csv.reader(open("train_Ticket0.csv","r"))
f2=csv.reader(open("train_Cabin0.csv","r"))
out=open("tri.csv","a",newline="")
csv_write=csv.writer(out,dialect="excel")
train=[]
ticket=[]
cabin=[]
for tri in f0:
    train.append(tri)
for tic in f1:
    ticket.append(tic)
for cab in f2:
    cabin.append(cab)
print(train[77][3])
print(len(ticket),len(train),len(cabin))
for i in range (len(train)):
    train[i][7] = ticket[i][1]
    train[i][9] = cabin[i][1]
    if train[i][3]=="male":
        train[i][3]="0"
    else:
        train[i][3]="1"
    if train[i][10]=="S":
        train[i][10]="0"
    if train[i][10]=="Q":
        train[i][10]="1"
    if train[i][10]=="C":
        train[i][10]="2"
for i in range(len(train)):
    csv_write.writerow(train[i])