file = open('transactions.txt', 'r')
lines = file.readlines()
file.close()

recipients = []
totals = []

for line in lines:
    line = line.strip()
    
    parts = line.split('|')
    
    to_part = parts[1]
    to_person = int(to_part.split(':')[1])
    
    amount_part = parts[2]
    amount = int(amount_part.split(':')[1])
    
    found = False
    position = 0
    for i in range(len(recipients)):
        if recipients[i] == to_person:
            found = True
            position = i
            break
    
    if found:
        totals[position] = totals[position] + amount
    else:
        recipients.append(to_person)
        totals.append(amount)

max_amount = 0
max_recipient = 0

for i in range(len(recipients)):
    if totals[i] > max_amount:
        max_amount = totals[i]
        max_recipient = recipients[i]

print("Person who received the most money:", max_recipient)
print("Total amount received:", max_amount)