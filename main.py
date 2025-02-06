def fizzbuzz(n=100):
    results = []
    for i in range(1, n + 1):
        output = ""
        if i % 3 == 0:
            output += "fizz"
        if "3" in str(i):
            output += "fizz"    
        if i % 5 == 0:
            output += "buzz"
        if "5" in str(i):
            output += "buzz"
        results.append(output or i)
    return results

if __name__ == '__main__':
    for value in fizzbuzz():
        print(value)