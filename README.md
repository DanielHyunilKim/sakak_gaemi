# Sakak Gaemi

Sakak Gaemi explores ways to find the middle two digits of a term in the look-and-say (LNS) sequence.

Starting with `1`, each term describes the consecutive groups of digits in the preceding term:

```text
1 → 11 → 21 → 1211 → 111221 → 312211 → ...
```

For example, `111221` contains three `1`s, two `2`s, and one `1`, so its next term is `312211`. This project accepts term numbers from 4 through 99. The exact scalable solution assumes the starting value `L = 1`.

## Installation

This project requires [uv](https://docs.astral.sh/uv/) and Python 3.14 or later.

Clone the repository and enter the project directory:

```bash
git clone https://github.com/DanielHyunilKim/sakak_gaemi.git
cd sakak_gaemi
```

Create the virtual environment and install the locked dependencies:

```bash
uv sync
```

Run the test suite to verify the installation:

```bash
uv run pytest
```

## Usage

`gaemi_conway` is the exact implementation intended for the full supported range:

```python
from gaemi_conway import gaemi_conway

gaemi_conway(12)  # 11
gaemi_conway(99)  # 11
```

The function returns `-1` when `n` is outside the range 4 through 99 or when `L` is not `1`.

## Approaches

| Approach | Exact | Scales to term 99 | Purpose |
|---|---:|---:|---|
| `gaemi_brute` | Yes | No | Construct complete terms and provide a reference result |
| `gaemi_trim` | No | Yes | Explore a bounded central-window heuristic |
| `gaemi_conway` | Yes | Yes | Find the middle digits through Conway's atomic elements |

### gaemi_brute

The `gaemi` function in `gaemi_brute.py` builds the complete nth LNS term. It starts with `L` as term 1 and applies `next_lns` another `n - 1` times. `gaemi_middle` then selects the two middle digits from the completed term.

`next_lns` scans the current term from left to right and groups adjacent copies of the same digit. It maintains three pieces of state:

- `tracking_c`: the digit in the current group
- `count`: the number of consecutive copies seen
- `lns`: a list of count-and-digit pieces for the next term

When the digit changes, the function adds the completed group's count and digit to `lns`, then begins a new group. After the scan, it adds the final group and joins the list into one string. For example, the groups `111`, `22`, and `1` are encoded as `31`, `22`, and `11`, producing `312211`.

#### Analysis

Let $m_i$ be the number of digits in term $i$. A transformation must read all $m_i$ digits and construct all $m_{i+1}$ output digits. With a linear-time output builder, computing term $n$ takes:

- Time: $O(m_1 + m_2 + \dots + m_n)$
- Space: $O(m_n)$, because the current and next terms must be held in memory

A term can be at most twice as long as the preceding term, giving loose worst-case bounds of $O(2^n)$ time and space when the starting length is constant. These bounds are not a tight description of typical growth, but they show why constructing term 99 is impractical.

The implementation achieves linear construction time by collecting the encoded pieces in a list and joining them once. This avoids repeatedly copying an immutable output string, but it does not avoid the cost of creating the complete term.

### gaemi_trim

`gaemi_trim` attempts to find the middle two digits without retaining each complete term. A `chunk` is a maximal group of one repeated digit, such as `111`, `22`, or `1`. In the standard sequence, each chunk is encoded as a count followed by its digit, so the middle two digits of the next term come from at most two chunks in the current term.

| Term | LNS term | Chunks, with relevant chunks in bold | Encoded relevant chunks | Middle of next term |
|---:|---|---|---:|---:|
| 3 | 21 | **2 1** | 1211 | 21 |
| 4 | 1211 | 1 **2** 11 | 12 | 12 |
| 5 | 111221 | 111 **22** 1 | 22 | 22 |
| 6 | 312211 | 3 **1 22** 11 | 1122 | 12 |
| 7 | 13112221 | 1 3 **11** 222 1 | 21 | 21 |

After constructing each new term, the implementation retains at most 100 digits. It removes approximately half of the excess from each end, moving each cut to a chunk boundary so that a retained chunk is never split. The shortened term is then used to compute the next generation.

This is a bounded-memory heuristic, not an exact algorithm. Cutting only at chunk boundaries prevents partial chunks from being encoded incorrectly, but it does not preserve enough information to locate future midpoints. The discarded sides can contain different numbers of chunks and therefore produce different output lengths. Rounding the cuts can also remove different numbers of digits from the two sides. Either effect can move the true midpoint away from the middle of the retained window.

#### Analysis

Let $C$ be the maximum retained length, currently 100. Each iteration transforms at most $C$ retained digits, divides the result into chunks, and joins the retained chunks again. With linear-time string construction, the bounds are:

- Time: $O(nC)$
- Space: $O(C)$

Because $C$ is fixed at 100, these bounds simplify to $O(n)$ time and $O(1)$ space with respect to `n`. These bounds describe only the heuristic's resource use; they do not guarantee a correct result.

### gaemi_conway

The trimming approach fails because ordinary chunks do not remain independent across later generations. [Conway's Cosmological Theorem](https://en.wikipedia.org/wiki/Look-and-say_sequence#Cosmological_decay) provides a safe alternative: a look-and-say term eventually separates into a finite set of atomic elements whose descendants do not interact with neighboring elements.

For the sequence starting with `1`, term 8 decomposes into two such elements:

```text
1113213211 = 11132 + 13211
             Hf      Sn
```

This gives the starting state `BASE_ATOMS = ("Hf", "Sn")`. The data in `conway.py` stores the digit sequence for each of the 92 elements and the ordered child elements it produces after one generation. For example, `Hf` decays into `Lu`, while `Sn` decays into `In`.

`gaemi_conway` uses this data without constructing the complete nth term:

1. Calculate how many generations remain after term 8.
2. Use `element_length` to calculate the future length of each base atom. The `@cache` decorator ensures that each `(element, generation)` pair is calculated only once.
3. Add the base-atom lengths to find the complete term's length and its two middle indexes.
4. Use `sequence_digit` to locate the base atom containing each index.
5. Use `element_digit` to descend through only the child atoms containing that index, stopping at a stored digit sequence.

The full term may contain an enormous number of digits, but the algorithm materializes only the small atom strings at the ends of the two required paths. Terms before term 8 are small and use the brute-force implementation. This solution is specific to the starting value `L = 1` and the supplied Conway element table.

#### Analysis

Let $G = n - 8$, $A$ be the number of Conway elements, and $B$ be the maximum number of children in one decay. There are at most $A(G + 1)$ distinct `(element, generation)` length calculations, and each calculation adds the lengths of at most $B$ children:

- Memoized length calculations: $O(AGB)$ time and $O(AG)$ space
- Two middle-digit lookups: $O(GB)$ time and $O(G)$ recursion depth

The element table fixes $A = 92$, and $B$ is also a fixed small constant. Omitting those constants, the complete algorithm uses:

- Time: $O(n)$
- Space: $O(n)$

These bounds treat arithmetic on stored lengths as constant-time. The algorithm's work grows with the number of generations rather than with the number of digits in the complete nth term.
