def permutation_function_using_built_in_function(user_list) :
    from itertools import permutations
    result = []
    for permutation in permutations(user_list) :
        result = result + [list(permutation)]
    return result
def main() :
    a = list(eval(input('>> Please enter a numbers seprated by Comma : ')))
    result = permutation_function_using_built_in_function(a)
    print()
    print('--> ',result)
    print()
    print('--> Total number of Permutations : ',len(result))
    print()
main()
