count = 0
total = 0
while count < 100:
    if count % 10 == 0:
        count +=1
        continue
    else:
        total += count
        count += 1
print(total)