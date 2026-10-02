# Bitwise Operators

> **One-line definition:** **Bitwise operators** work on integers **one binary bit at a time**: AND `&`, OR `|`, XOR `^`, NOT `~`, and the shifts `<<` and `>>`.

## 🎯 TL;DR (30-second recall)
- `&` gives 1 only if **both** bits are 1. `|` gives 1 if **either** bit is 1. `^` gives 1 if the bits are **different**.
- `~n == -(n + 1)` because Python uses **two's complement** (explained below).
- `n << k == n * 2**k` and `n >> k == n // 2**k` (floor division).
- They work on **`int`** (and `bool`). Sets reuse the same symbols for union, intersection and so on.
- Classic tricks: `n & 1` checks odd/even, `n & (n - 1) == 0` checks for a power of 2, and `a ^ a == 0` finds the unique item.
- Real-world uses: **file permissions**, **subnet masks**, **flags** and **pandas boolean masks**.

## 📖 Concept Explained (from this folder's code)

Every file follows the same pattern: two ints, one operator, print the result. The trick is to **write the numbers in binary and line up the columns**.

| File | Code | Binary working | Result |
|---|---|---|---|
| [Bitwise_AND.py](Bitwise_AND.py) | `5 & 9` | `0101 & 1001 = 0001` | **1** |
| [Bitwise_OR.py](Bitwise_OR.py) | `10 \| 12` | `1010 \| 1100 = 1110` | **14** |
| [Bitwise_XOR.py](Bitwise_XOR.py) | `5 ^ 9` | `0101 ^ 1001 = 1100` | **12** |
| [Bitwise_One's_Complement_Operator.py](Bitwise_One%27s_Complement_Operator.py) | `~5` | `-(5 + 1)` | **-6** |
| [Bitwise_Leftshift_Operator.py](Bitwise_Leftshift_Operator.py) | `4 << 3` | `100` → `100000` | **32** |
| [Bitwise_Rightshift_Operator.py](Bitwise_Rightshift_Operator.py) | `128 >> 3` | `10000000` → `10000` | **16** |

### 1. AND, OR, XOR: column-by-column logic

```python
a = 5
b = 9
c = a & b      # 1
```

```
  5 = 0 1 0 1
  9 = 1 0 0 1
  ----------- &   (1 only where BOTH are 1)
      0 0 0 1  = 1
```

- **AND `&`** is a **filter**. It keeps only the bits set in both numbers.
- **OR `|`** is a **combiner**. `10 | 12` → `1010 | 1100 = 1110 = 14`.
- **XOR `^`** is a **difference detector**. `5 ^ 9` → `0101 ^ 1001 = 1100 = 12`.

> 💡 **Analogy:** think of each bit as a light switch. AND says "on only if both rooms are on". OR says "on if any room is on". XOR says "on if exactly one room is on".

### 2. One's complement `~`

```python
A = 5
B = ~5        # -6, matching the file's formula -(n+1)
```

**Why is it negative?** Python stores negative integers in **two's complement** form, where `-x` equals `~x + 1`. Rearranging gives `~x = -x - 1 = -(x + 1)`. Flipping every bit of `...0101` gives `...1010`, which represents `-6`.

### 3. Left and right shift

```python
B = 4 << 3     # 32
B = 128 >> 3   # 16
```

- **`<<` k** moves every bit **k places left** and fills the right side with zeros. Each step doubles the value.
- **`>>` k** moves bits **k places right**. The lowest bits drop off and each step halves the value (rounding down).

> ⚠️ **Correction to the code comments:** the files say `n * (2)n` and `n / (2)n`. The precise rules use the **shift count `k`**, not `n`:
> - `n << k == n * 2**k`, so `4 << 3 == 4 * 8 == 32`
> - `n >> k == n // 2**k`, so `128 >> 3 == 128 // 8 == 16`
>
> It's **floor** division (`//`), not `/`. That matters for odd and negative numbers: `-9 >> 1 == -5`.

## 🧠 Important Notes You Should Also Know

- **Python ints never overflow.** They have unlimited size, so `~5` is `-6`, not a fixed-width `250`. Apply a mask to get C-style results: `~5 & 0xFF == 250`.
- **`bin()` doesn't show two's complement:** `bin(-5)` is `'-0b101'`. Use `format(n & 0xFF, "08b")` to see the real 8-bit pattern.
- **Base conversions:** `bin(10)` → `'0b1010'`, `hex(255)` → `'0xff'`, `oct(8)` → `'0o10'`, `int("1010", 2)` → `10`, `f"{10:08b}"` → `'00001010'`. Literals: `0b1010`, `0o755`, `0xFF`.
- **Precedence:** arithmetic binds tighter than shifts (`1 << 2 + 1 == 8`). Bitwise operators bind tighter than comparisons, so `x & 1 == 0` works (unlike C). When in doubt, add parentheses.
- **`&` / `|` vs `and` / `or`:** `and` / `or` short-circuit and return operands. `&` / `|` always evaluate both sides and work bit by bit.
- **Same symbols on sets:** `{1, 2} & {2, 3} == {2}` (intersection), `|` is union and `^` is symmetric difference.
- **Counting and sizing bits:** `bin(n).count("1")` counts set bits (`n.bit_count()` on Python 3.10+). `n.bit_length()` gives the bits needed.
- **Classic tricks:** `n & 1` is the odd/even test, `n & (n - 1) == 0` is the power-of-two test, and XOR cancels pairs (`a ^ a == 0`). The full list is in the cheat sheet below.

## 💡 Where This Shows Up in DevOps / Data Engineering Work
- **Linux file permissions:** `0o755` is three 3-bit groups (rwx for owner, group, other).
  - Check the owner's execute bit with `mode & stat.S_IXUSR`.
  - umask works by masking: `0o777 & ~0o022 == 0o755`.
- **Networking and CIDR:** the network address is `ip & netmask`. For example, `192.168.1.77 & 255.255.255.0` gives `192.168.1.0`. The `ipaddress` module does this for you, but interviewers like asking how.
- **Feature flags and permission sets:** `enum.IntFlag` stores many on/off options in one integer.

  ```python
  from enum import IntFlag
  class Perm(IntFlag):
      READ = 4
      WRITE = 2
      EXEC = 1
  p = Perm.READ | Perm.WRITE    # int(p) == 6
  Perm.WRITE in p               # True
  ```

- **pandas boolean masks:** `df[(df.status == 500) & (df.latency > 2)]`. pandas requires `&` / `|`, not `and` / `or`, and the **parentheses are mandatory** because `&` binds tighter than `==` and `>`.

## ❓ Interview Questions & Answers

1. **[Beginner] What's the difference between `&` and `and`?**
   `&` works on each bit of an integer and always evaluates both sides. `and` is logical, short-circuits, and returns one of its operands.

2. **[Beginner] Predict the output:** `print(5 & 9, 10 | 12, 5 ^ 9, ~5)`
   `1 14 12 -6`. Line up the binary columns: `0101 & 1001 = 0001`, `1010 | 1100 = 1110`, `0101 ^ 1001 = 1100`, and `~5 = -(5 + 1)`.

3. **[Beginner] What do `<<` and `>>` do mathematically?**
   `n << k` multiplies by `2**k`. `n >> k` floor-divides by `2**k`. So `4 << 3 == 32` and `128 >> 3 == 16`.

4. **[Intermediate] Why is `~5` equal to `-6` and not `250`?**
   Python ints have unlimited size and use two's complement, where `~x == -x - 1`. You only get `250` by masking to 8 bits: `~5 & 0xFF`.

5. **[Intermediate] Check whether a number is a power of two in one line.**
   `n > 0 and n & (n - 1) == 0`. Subtracting 1 flips the single set bit and every bit below it, so AND gives 0 only when exactly one bit was set.

6. **[Intermediate] Predict the output:** `print(1 << 2 + 1, -9 >> 1)`
   `8 -5`. `+` binds tighter than `<<`, and `>>` floors toward −∞.

7. **[Intermediate] In a list, every number appears twice except one. Find it in O(n) time and O(1) space.**
   XOR everything together: `reduce(operator.xor, nums)`. Pairs cancel (`a ^ a == 0`) and `x ^ 0 == x`.

8. **[Advanced] Why does `df[df.a > 1 and df.b < 5]` fail in pandas, and how do you fix it?**
   `and` tries to turn a whole Series into one `bool`, which raises `ValueError: truth value of a Series is ambiguous`. Use `(df.a > 1) & (df.b < 5)` with parentheses.

9. **[Scenario] A deploy script must check whether a file is executable by its owner. How?**
   `bool(os.stat(path).st_mode & stat.S_IXUSR)`. AND the mode with the single permission bit you care about.

10. **[Scenario] Given an IP and a CIDR prefix like `/24`, how do you compute the network address with bitwise operators?**
    Build the mask with `mask = (0xFFFFFFFF << (32 - prefix)) & 0xFFFFFFFF`, then compute `network = ip_int & mask`. In production code, use `ipaddress.ip_network()`.

## 🔗 Related Topics
- **Also worth knowing:**
  - **Binary, octal and hex literals:** `0b`, `0o` and `0x`. Octal is everywhere in `chmod`, and hex shows up in hashes, colors and memory addresses.
  - **Two's complement** is how almost every CPU stores negative integers. Knowing it explains both `~` and right shifts of negative numbers.
  - **`enum.Flag` / `IntFlag`** is the readable, Pythonic way to use bitmasks.
  - **`hash & (n - 1)`** buckets a hash into `n` slots when `n` is a power of two. It's the idea behind dict internals and data partitioning.
- **Read alongside:**
  - [Basics of Python](../Basics_of_Python_01/README.md): arithmetic, logical and comparison operators, and precedence
  - [Sets](../Sets_Python_07/README.md): the same `& | ^` symbols used as set operations
  - [Conditional Practice](../conditional_practice/README.md): odd/even checks (`n % 2` vs `n & 1`)

---

## ⚡ Quick Revision: 5-Minute Interview Cheat Sheet

> **Say it in one breath:** Bitwise operators work on the binary bits of integers: `&` means both, `|` means either, `^` means different, `~n` is `-(n + 1)`, and `<<` / `>>` multiply / floor-divide by `2**k`.

### 📋 Cheat sheet

| Need to... | Use | Example → Result |
|---|---|---|
| Keep bits set in both | `a & b` | `12 & 10` → `8` |
| Keep bits set in either | `a \| b` | `12 \| 10` → `14` |
| Find the differing bits | `a ^ b` | `12 ^ 10` → `6` |
| Flip all bits | `~n` (same as `-(n + 1)`) | `~12` → `-13` |
| Multiply by 2ᵏ | `n << k` | `1 << 10` → `1024` |
| Floor-divide by 2ᵏ | `n >> k` | `-9 >> 1` → `-5` |
| Odd or even | `n & 1` | `7 & 1` → `1` |
| Power of two? | `n > 0 and n & (n - 1) == 0` | `16` → `True`, `12` → `False` |
| Find the unique item | `reduce(operator.xor, nums)` | `[4, 1, 2, 1, 2]` → `4` |
| Count set bits | `bin(n).count("1")` | `bin(255).count("1")` → `8` |
| 8-bit pattern of a negative | `format(n & 0xFF, "08b")` | `format(-5 & 0xFF, "08b")` → `11111011` |
| Check one permission bit | `mode & stat.S_IXUSR` | `0o755 & stat.S_IXUSR` → `64` (truthy) |

### 🔥 Output drills (cover the right column, predict, then check)

| Code | Output |
|---|---|
| `print(12 & 10, 12 \| 10, 12 ^ 10)` | `8 14 6` |
| `print(~0, ~-1)` | `-1 0` |
| `print(1 << 2 + 1)` | `8` |
| `print(-9 >> 1)` | `-5` |
| `print(~5 & 0xFF)` | `250` |
| `print(6 & 1 == 0, 7 & 1 == 0)` | `True False` |
| `print(bin(5 ^ 9), int("1010", 2))` | `0b1100 10` |
| `print(True & False, True \| False)` | `False True` |

### 🧷 Rules & traps to remember
- **Memory trick:** `&` = both, `|` = either, `^` = different.
- **`~n == -(n + 1)`** because of two's complement. Mask with `& 0xFF` for a fixed width.
- **Shifts use the count `k`:** `n << k == n * 2**k` and `n >> k == n // 2**k` (not `n * 2**n`, as the old code comments say).
- **`>>` floors:** `-9 >> 1 == -5`, not `-4`.
- **Not `and` / `or` in pandas:** use `&` / `|` and wrap each comparison in parentheses.
- **Precedence:** `1 << 2 + 1 == 8`. Add parentheses when unsure.
- **No overflow in Python:** values never wrap around unless you mask them.

### ✅ Last-minute checklist
- [ ] I can compute `5 & 9`, `10 | 12` and `5 ^ 9` by writing the binary columns.
- [ ] I can explain why `~5 == -6`.
- [ ] I can state both shift formulas using the shift count `k`.
- [ ] I can write the odd/even, power-of-two and XOR-unique tricks.
- [ ] I can name two DevOps uses (file permissions and CIDR masks).
