import re

def arithmetic_arranger(problems: list) -> str:

    n_problems = len(problems)

    if n_problems > 5:
        return 'Error: Too many problems.'
    

    joined_problems = ' '.join(problems)
    if ('*' in joined_problems) or ('/' in joined_problems):
        return "Error: Operator must be '+' or '-'."


    valid_characters = ['1','2','3','4','5','6','7','8','9','-','+',' ']
    characters = set(joined_problems)
    for c in characters:
        if c not in valid_characters:
            return 'Error: Numbers must only contain digits.'
    
    problems_result = []
    
    for problem in problems:
        if '+' in problem:
            operands = problem.replace(' ', '').split('+')
            operands.append('+')
            print(operands)

        else:
            operands = problem.replace(' ', '').split('-')
            operands.append('-')
        
        max_len = len(max(operands[:2], key=len))
        print(max_len)
        
        if max_len > 4:
            return 'Error: Numbers cannot be more than four digits.'
    
        problem_result = [f"{operands[0].rjust(max_len + 2 - len(operands[0]), ' ')}", 
                          f"{operands[2] + operands[1].rjust(max_len + 2 - len(operands[1]), ' ')}",
                          f"{'-' * (max_len + 2 )}"
                        ]
        
        problems_result.append('\n'.join(problem_result))
    
    return '\n'.join(problems_result)


print(arithmetic_arranger(['2 + 1', '3 + 9999']))