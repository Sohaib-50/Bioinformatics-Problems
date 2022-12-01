import random
def solution(homozygous_dominant, heterozygous, homozygous_recessive):
    '''
    given the number of homozygous dominant, heterozygous, and homozygous recessive organisms in a population,
    returns the probability that two randomly selected organisms will produce an individual possessing a dominant allele

    solved by calculating all possible outcomes of two randomly selected organisms and summing the probability of each outcome (drew a tree diagram to help, link: https://imgur.com/a/MbJmrlo)
    '''
    population_size = homozygous_dominant + heterozygous + homozygous_recessive
    probability = 0

    # 1st parent is homozygous dominant cases
    probability += (homozygous_dominant / population_size) * ((homozygous_dominant - 1) / (population_size - 1))  # both parents are homozygous dominant
    probability += (homozygous_dominant / population_size) * (heterozygous / (population_size - 1))  # one parent is homozygous dominant and the other is heterozygous
    probability += (homozygous_dominant / population_size) * (homozygous_recessive / (population_size - 1))  # one parent is homozygous dominant

    # 1st parent is heterozygous cases
    probability += (heterozygous / population_size) * (homozygous_dominant / (population_size - 1))  # one parent is heterozygous and the other is homozygous dominant
    probability += (heterozygous / population_size) * ((heterozygous - 1) / (population_size - 1)) * (3 / 4)  # both parents are heterozygous
    probability += (heterozygous / population_size) * (homozygous_recessive / (population_size - 1)) * (1 / 2)  # one parent is heterozygous and the other is homozygous recessive

    # 1st parent is homozygous recessive cases
    probability += (homozygous_recessive / population_size) * (homozygous_dominant / (population_size - 1))  # one parent is homozygous recessive
    probability += (homozygous_recessive / population_size) * (heterozygous / (population_size - 1)) * (1 / 2)  # one parent is homozygous recessive and the other is heterozygous

    return probability
         

with open('rosalind_iprb.txt', 'r') as f:
    homozygous_dominant, heterozygous, homozygous_recessive = map(int, f.read().strip().split(' '))

ans = solution(homozygous_dominant, heterozygous, homozygous_recessive)
print(ans)