# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def Fibonacci_series_generator(Number_of_terms):
    series_array = [0, 1]
    if(Number_of_terms<2):
        print("Sorry but you can not have a Fibonacci series for this term")
    else:
        print("Generating the series now")
        for a in range(2, Number_of_terms):
            next_term = series_array[a - 1] + series_array[a - 2]
            series_array.append(next_term)
        print(series_array)
    return series_array


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Welcome to the Fibonacci series generator")
    x=int(input("enter the number of terms"))
    answer=Fibonacci_series_generator(x)






# See PyCharm help at https://www.jetbrains.com/help/pycharm/
