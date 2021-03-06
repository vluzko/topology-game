import random
import pickle
from sys import argv


PROPERTIES = {
    'connected',
    'path connected',
    'locally connected',
    'locally path connected',
    'totally disconnected',
    'arc connected',
    'simply connected',
    'locally simply connected',
    'contractible',
    'hyperconnected',
    'ultraconnected',
    'compact',
    'sequentially compact',
    'countably compact',
    'pseudocompact',
    'sigma-compact',
    'Lindelof',
    'paracompact',
    'locally compact',
    'finite',
    'countable',
    'bigger than R',
    'T_0',
    'T_1 (Frechet)',
    'T_2 (Hausdorff)',
    'T_2.5 (Urysohn)',
    'T_3 (regular Hausdorff',
    'T_3.5 (Tychonoff',
    'T4 (normal Hausdorff)',
    'T5 (completely normal Hausdorff)',
    'T6 (perfectly normal Hausdorff)',
    'no isolated points',
    'separable',
    'first countable',
    'second countable',
    'metrizable',
    'locally metrizable',
    'homogeneous',
    'alexandrov',
    'zero dimensional',
    'Abelian fundamental group',
    'Finitely generated fundamental group',
    'Free fundamental group',
    'Finite fundamental group',
    'Countable fundamental group',
    # Can't read 91-97
    'Embeddable in R',
    'Embeddable in R^2',
    'Embeddable in R^3',
    'Embeddable in R^4'
    'Embeddable in R^n',
    'Embeddable in R^\infty',
    'Topological manifold',
    'Genus 0',
    'Genus 1',
    'Genus 2',
    'Has dispersion point'
    'Scattered',
    'Meager',
    'Strongly connected',
    # Can't read 127
    'Countably paracompact',
    'Metacompact',
    'Countably metacompact',
    'Noetherian',
    'Infinite genus',
    'Uncountable genus',
    'Point genus 0',
    'Point genus 1',
    'Point genus >=2',
    # Can't read 147 through 159
    'Infinite point genus',
    'Quasi-metrizable',
    'Pseudometrizable',
    'Countably tight',
    'Angelic',
    # Can't read 171 or 173
    'All subsets open xor closed'
    # Can't read 177 - end
}


def prop_string(p: str) -> str:
    p_not_p = '' if random.randrange(2) else 'not '
    return f'{p_not_p}{p}'


def main():
    global PROPERTIES
    # Can't sample from a set anymore
    a, b = random.sample(list(PROPERTIES), 2)
    print(f'Properties:\n    {prop_string(a)}\n    {prop_string(b)}')
    PROPERTIES -= {a, b}
    done = False

    while not done:
        i = input('Next property? ')
        if i == 'q':
            done = True
            continue
        else:
            c = random.sample(list(PROPERTIES), 1)[0]
            PROPERTIES -= {c}
            print(f'New property: {prop_string(c)}')



if __name__ == "__main__":
    main()
