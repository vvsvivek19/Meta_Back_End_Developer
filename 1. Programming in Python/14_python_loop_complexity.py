import time
start_time = time.time()

#outer loop
for i in range(100):
    #inner loop
    for j in range(500):
        print(0, end = " ")
    #printing an emptyline
    print()

print("Total time taken:",round((time.time() - start_time),2))