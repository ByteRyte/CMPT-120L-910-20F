def prime_or_composite(number):
    counter = 0
    x = 1
    while x <= number:
        if number % x == 0:
            counter += 1
        x += 1
        if counter > 2:
            return "Composite"
    return "Prime"

if __name__ == "__main__":
    numbers = [1, 2, 10, 31, 47, 89, 101, 103, 97, 187, 981, 19201]
    # If you want to test the efficency of your algorithm add this number to the array above -7
    # If you want to test the efficency of your algorithm add this number to the array above 47055833459
    answers = []
    for number in numbers:
        answers.append(prime_or_composite(number))
    
    print(answers)