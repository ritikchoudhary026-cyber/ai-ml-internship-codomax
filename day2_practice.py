def predict_score_simple(study_hours):
    # Simple logic (not ML yet, just practice)
    predicted_score = study_hours * 10
    return predicted_score

hours = float(input("Enter study hours: "))
score = predict_score_simple(hours)
print(f"If you study {hours} hours, estimated score = {score}")


#odd and even checker------
def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

num = int(input("Enter a number: "))
print(f"{num} is {check_even_odd(num)}")


#sum of list using loops------

numbers = [10, 20, 30, 40, 50]
total = 0

for num in numbers:
    total += num

print("Sum of list:", total)
print("Average:", total / len(numbers))