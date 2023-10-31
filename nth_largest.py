lst = [14, 67, 48, 23, 5, 62]
N = int(input("Which largest number: "))

if N <= 0 or N > len(lst):
    print("Invalid input for N.")
else:
    sorted_list = sorted(lst, reverse=True)
    if N == len(lst):
        nth_largest = sorted_list[0]
    else:
        nth_largest = sorted_list[N-1]
    print(f"{N}th Largest number: {nth_largest}")
