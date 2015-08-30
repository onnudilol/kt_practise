# Borrowing the dictionary from http://rosettacode.org/wiki/Stable_marriage_problem

def stable_matching(proposer_pref, proposed_pref):

    """creates stable perfect matches from proposers proposing to proposees"""

    stable_match = {}
    free_men = list(proposer_pref.keys())
    already_matched = dict(zip(free_men, [[] for i in range(len(free_men))]))
    pref = 0

    while len(free_men) > 0:
        freeman = free_men.pop()
        potential_mate = proposer_pref[freeman][pref]

        if not stable_match.get(potential_mate):
            stable_match[potential_mate] = freeman
            already_matched[freeman].append(potential_mate)
            pref = 0

        else:
            alt_mate = stable_match.get(potential_mate)

            if proposed_pref[potential_mate].index(alt_mate) < proposed_pref[potential_mate].index(freeman):
                already_matched[freeman].append(potential_mate)
                free_men.append(freeman)
                pref = len(already_matched[freeman])

            else:
                already_matched[freeman].append(potential_mate)
                stable_match[potential_mate] = freeman
                free_men.append(alt_mate)
                pref = len(already_matched[alt_mate])

    return stable_match

if __name__ == '__main__':

    guyprefers = {'abe':  ['abi', 'eve', 'cath', 'ivy', 'jan', 'dee', 'fay', 'bea', 'hope', 'gay'],
                  'bob':  ['cath', 'hope', 'abi', 'dee', 'eve', 'fay', 'bea', 'jan', 'ivy', 'gay'],
                  'col':  ['hope', 'eve', 'abi', 'dee', 'bea', 'fay', 'ivy', 'gay', 'cath', 'jan'],
                  'dan':  ['ivy', 'fay', 'dee', 'gay', 'hope', 'eve', 'jan', 'bea', 'cath', 'abi'],
                  'ed':   ['jan', 'dee', 'bea', 'cath', 'fay', 'eve', 'abi', 'ivy', 'hope', 'gay'],
                  'fred': ['bea', 'abi', 'dee', 'gay', 'eve', 'ivy', 'cath', 'jan', 'hope', 'fay'],
                  'gav':  ['gay', 'eve', 'ivy', 'bea', 'cath', 'abi', 'dee', 'hope', 'jan', 'fay'],
                  'hal':  ['abi', 'eve', 'hope', 'fay', 'ivy', 'cath', 'jan', 'bea', 'gay', 'dee'],
                  'ian':  ['hope', 'cath', 'dee', 'gay', 'bea', 'abi', 'fay', 'ivy', 'jan', 'eve'],
                  'jon':  ['abi', 'fay', 'jan', 'gay', 'eve', 'bea', 'dee', 'cath', 'ivy', 'hope']}

    galprefers = {'abi':  ['bob', 'fred', 'jon', 'gav', 'ian', 'abe', 'dan', 'ed', 'col', 'hal'],
                  'bea':  ['bob', 'abe', 'col', 'fred', 'gav', 'dan', 'ian', 'ed', 'jon', 'hal'],
                  'cath': ['fred', 'bob', 'ed', 'gav', 'hal', 'col', 'ian', 'abe', 'dan', 'jon'],
                  'dee':  ['fred', 'jon', 'col', 'abe', 'ian', 'hal', 'gav', 'dan', 'bob', 'ed'],
                  'eve':  ['jon', 'hal', 'fred', 'dan', 'abe', 'gav', 'col', 'ed', 'ian', 'bob'],
                  'fay':  ['bob', 'abe', 'ed', 'ian', 'jon', 'dan', 'fred', 'gav', 'col', 'hal'],
                  'gay':  ['jon', 'gav', 'hal', 'fred', 'bob', 'abe', 'col', 'ed', 'dan', 'ian'],
                  'hope': ['gav', 'jon', 'bob', 'abe', 'ian', 'dan', 'hal', 'ed', 'col', 'fred'],
                  'ivy':  ['ian', 'col', 'hal', 'gav', 'fred', 'bob', 'abe', 'ed', 'jon', 'dan'],
                  'jan':  ['ed', 'hal', 'gav', 'abe', 'bob', 'jon', 'col', 'ian', 'fred', 'dan']}

    test_match = stable_matching(guyprefers, galprefers)

    sorted_match = (sorted(test_match.items()))

    for key, value in sorted_match:
        print('{} is engaged to {}'.format(key, value))
