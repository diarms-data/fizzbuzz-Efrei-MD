def fizzbuzz(n=100):
    results = []
    for i in range(1, n + 1):
        output = ""
        if i % 3 == 0:
            output += "Fizz"
        if "3" in str(i):
            output += "Fizz"    
        if i % 5 == 0:
            output += "Buzz"
        if "5" in str(i):
            output += "Buzz"
        results.append(output or i)
    return results

if __name__ == '__main__':
    for value in fizzbuzz():
        print(value)