import random

def generate_random_integer(minimum: int, maximum: int) -> int:
    """Generates a random integer between the specified minimum and maximum values.

    Parameters
    ----------
    minimum : int
        The minimum value for the random integer.
    maximum : int
        The maximum value for the random integer.

    Returns
    -------
    int
        A random integer between the specified minimum and maximum values.
    """
    return random.randint(minimum, maximum)

def choose_operator() -> str:
    """
    Chooses a random arithmetic operator from the set {+, -, *}.

    Returns
    -------
    str
        A randomly chosen arithmetic operator.
    """
    return random.choice(['+', '-', '*'])

def perform_operation(number1, number2, operator: str) -> tuple:
    """
    Performs an arithmetic operation on two numbers based on the given operator.

    Parameters
    ----------
    number1 : int
        The first operand.
    number2 : int
        The second operand.
    operator : str
        The arithmetic operator.

    Returns
    -------
    tuple
        A tuple containing the formatted operation string and the result of the operation.
    """
    operation_str = f"{number1} {operator} {number2}"

    if operator == '+': 
        result = number1 + number2
    elif operator == '-': 
        result = number1 - number2
    else: 
        result = number1 * number2

    return operation_str, result

def math_quiz() -> None:
    """
    Conducts a math quiz game where the user is presented with math problems and needs to provide correct answers.
    """
    score = 0
    total_questions = 3

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total_questions):
        number1 = generate_random_integer(1, 10); number2 = generate_random_integer(1, 5); operator = choose_operator()

        problem_str, solution = perform_operation(number1, number2, operator)
        print(f"\nQuestion: {problem_str}")

        while True:
            try:
                user_answer = int(input("Your answer: "))
                break
            except ValueError:
                print("Error: Please enter a valid number.")

        if user_answer == solution:
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {solution}.")

    print(f"\nGame over! Your score is: {score}/{total_questions}")

if __name__ == "__main__":
    math_quiz()
