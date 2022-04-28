import time


input_str_second = input("how many second you want= ")
int_second = int(input_str_second)

for stopwatch in range(1, int_second):
    time.sleep(1)
    print(stopwatch)
time.sleep(1)
print(f"reached {input_str_second}")

