import random

def main():
    print("Welcome to Decision Maker!")
    print("I will help you to find an answer")
    print(" ")
    question = input("Ask a YES or NO question: ")
    while question != "":
        rand_number = random.randint(1,10)
   
    # 1. Definetly not
    # 2. Never
    # 3. Without a doubt
    # 4. As I see it, YES
    # 5. My sorces say NO
    # 6. Cannot predict now
    # 7. Most likely
    # 8. Reply hazy, try again
    # 9. YES - Definetly
    # 10. Very doubtfull

        if rand_number == 1:
            print("Definetly not")
        if rand_number == 2:
            print("Never")
        if rand_number == 3:
            print("Without a doubt")  
        if rand_number == 4:
            print("As I see it, YES")
        if rand_number == 5:
            print("My sorces say NO")
        if rand_number == 6:
            print("Cannot predict now")
        if rand_number == 7:
            print("Most likely")
        if rand_number == 8:
            print("Reply hazy, try again")
        if rand_number == 9:
            print("YES - Definetly")
        if rand_number == 10:
            print("Very doubtfull")
        print(" ")
        question = input("Ask a YES or NO question: ")

if __name__ == '__main__':
    main()