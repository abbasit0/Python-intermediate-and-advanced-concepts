while True:
    num = input("Enter numbers separated by spaces, or 'N' to exit:\n")

    if num.lower() == 'n':
        print("OK!")
        break

    try:
        num = num.split()
        num = [int(numbers) for numbers in num]
    except ValueError:
        print("Please enter only numbers separated by spaces.")
    else:
        total = sum(num)
        print('The sum is', total)


    
# if we  come to that there are many errors in the try block we can use except* to deal with them