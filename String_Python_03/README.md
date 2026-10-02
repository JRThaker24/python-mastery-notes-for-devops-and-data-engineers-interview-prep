# Strings in Python

> **One-line definition:** A **string** (`str`) is text stored as a **read-only** row of characters: you can read or slice any part of it, but every "change" gives you a **new** string.

## 🎯 TL;DR (30-second recall)
- **Immutable:** `s[0] = "J"` raises `TypeError`. Methods like `upper()` and `replace()` **return a new string** and leave the original alone.
- **Index** = position number. It starts at `0`, and negative numbers count from the end (`s[-1]` is the last character). A bad index raises `IndexError`.
- **Slice** = `s[start:stop:step]`. `start` is **included**, `stop` is **excluded**, and `s[::-1]` reverses. Out-of-range slice bounds don't raise. They just give a shorter string or `''`.
- **Everyday tools:** `len`, `replace`, `strip`, `lower` / `upper`, `split`, `join`, `count`, `find`, `startswith` / `endswith`, and `in` to test "contains".
- **`strip("abc")` removes a set of characters**, not a prefix or suffix. For those, use `removeprefix` / `removesuffix` (Python 3.9+).
- **`str` is text, `bytes` is raw data.** `.encode()` turns text into bytes and `.decode()` turns bytes back into text.

## 📖 Concept Explained (from this folder's code)

### 1. Indexing, negative indexing and immutability: [string.py](string.py)

```python
pl = "Python"
print(f"First Charchater, {pl[0]}  ")        # P
print("Third Charchater, ", pl[3])           # h
print("First Reverse Character ", pl[-1])    # n
print("Third Reverse Character ", pl[-3])    # h
# We cannot replace string characters in python because strings in python is immutable ...
```

An **index** is the position number of one character. Python counts from `0` on the left and from `-1` on the right:

| Letter | `P` | `y` | `t` | `h` | `o` | `n` |
|---|---|---|---|---|---|---|
| Index | `0` | `1` | `2` | `3` | `4` | `5` |
| Negative index | `-6` | `-5` | `-4` | `-3` | `-2` | `-1` |

- The index is an **offset** (steps from the start), so the first letter sits at `0`. `s[-k]` is shorthand for `s[len(s) - k]`, which is why `pl[3]` and `pl[-3]` are both `'h'` here.
- The first `print` uses an **f-string** (the `f` prefix fills `{pl[0]}` with its value, see the [Basics README](../Basics_of_Python_01/README.md)).
- **Immutable** means the object can't change after it is created. So Python refuses to overwrite one character, and every string method has to build a new string instead.

> **Analogy:** a string is a **printed ticket** with one letter per numbered slot. You can read any slot or photocopy a stretch of slots (slicing), but you can't scribble on the ticket. To "change" it you print a new ticket.

> ⚠️ **Note on `string.py`:** the label "Third Charchater" for `pl[3]` is wrong. Index `3` is the **fourth** character (`'h'`) because counting starts at `0`. The third character is `pl[2]` (`'t'`). The "Third Reverse Character" label is correct, since negative counting starts at `-1`.

> ⚠️ **Note on `string.py`:** the last comment (strings are immutable) is true, but nothing in the file runs it. `s = "Python"` then `s[0] = "J"` gives `TypeError: 'str' object does not support item assignment`. Build a new string instead: `"J" + s[1:]` is `'Jython'`.

> ⚠️ **Note on `string.py`:** the file name is the same as the standard-library module `string`. (The **standard library** is the set of modules that ship with Python. A **module** is a `.py` file you can `import`.) Python searches the script's folder **before** the standard library, so from inside this folder `import string` loads *this file* and runs its `print` lines. Then `string.ascii_lowercase` fails with `AttributeError: module 'string' has no attribute 'ascii_lowercase'`. Even `import logging` fails with an `ImportError`, because `logging` runs `from string import Template`. (Checked on Python 3.9.6.) Rename the file, for example `string_indexing.py`.

### 2. Slicing: [Slicing_Strings.py](Slicing_Strings.py)

```python
str = "Python"
print(str[0:3])      # Pyt
print(str[-4:-1])    # tho
print(str[:3])       # Pyt   (start left out, so it starts at 0)
print(str[3:])       # hon   (stop left out, so it runs to the end)
```

A **slice** is a copy of part of a string, written `s[start:stop:step]`. The **step** is how far to move each time (default `1`).

- **`start` is included, `stop` is excluded.** `s[0:3]` takes indexes `0, 1, 2`, so it has `stop - start` characters. This way `s[:3] + s[3:]` rebuilds `s` with no gap and no overlap.
- `str[-4:-1]` starts at `-4` (`'t'`) and stops *before* `-1` (`'n'`), so you get `'tho'`.
- Left-out values default to the ends: `start=0`, `stop=len(s)`, `step=1`. A **negative step** walks backwards (and flips those defaults), so `s[::-1]` reverses the string.
- A slice returns a **new** string and leaves the original alone, exactly as the file's first comment says.

| Slice of `"Python"` | Result | Meaning |
|---|---|---|
| `s[-3:]` | `'hon'` | last 3 characters |
| `s[:]` | `'Python'` | full copy |
| `s[::2]` | `'Pto'` | every 2nd character |
| `s[::-1]` | `'nohtyP'` | reversed |

> ⚠️ **Note on `Slicing_Strings.py` and `String_Methods.py`:** both write `str = "Python"`. That **shadows** (hides) Python's built-in `str` type behind your variable. After it, `str(5)` fails with `TypeError: 'str' object is not callable`. Neither file calls `str()` later, so they still run, but it's a trap. Use `text` or `s`. (`del str` brings the built-in back.)

### 3. String methods: [String_Methods.py](String_Methods.py)

A **method** is a function that belongs to an object and is called with a dot, like `"abc".upper()`.

```python
str = "Python"
new_str= str.replace("t","T")
print(new_str)                  # PyThon  (str itself is still "Python")
str2 = " Python "
print(str2.strip())             # Python
str6= "Python-Scripting-Language"
print(str6.split("-"))          # ['Python', 'Scripting', 'Language']
print(str6.count("P"))          # 1
```

| Call (values from the file) | Result | What to remember |
|---|---|---|
| `len("Python")` | `6` | counts characters (a built-in function, not a method) |
| `"Python".replace("t","T")` | `'PyThon'` | replaces **every** match. A 3rd argument limits it: `"banana".replace("a","o",1)` gives `'bonana'` |
| `" Python ".strip()` | `'Python'` | cuts whitespace (spaces, tabs, newlines) from the **two ends** only. `lstrip` / `rstrip` do one side |
| `"python".upper()`, `"PYTHON".lower()` | `'PYTHON'`, `'python'` | change case |
| `"Python,Language".split(",")` | `['Python', 'Language']` | cuts at each separator and returns a **list** |
| `"Python-Scripting-Language".count("P")` | `1` | counts matches, case-sensitive (the file has no heading for it, it sits under "Split") |

**Key idea:** none of these change `str`. Strings are immutable, so each method returns a new string. A bare `str.replace(...)` line is thrown away unless you store the result, as the file does with `new_str`.

## 🧠 Important Notes You Should Also Know

| Tool | If found | If missing | Use it when |
|---|---|---|---|
| `s.find(x)` | index (`0` or more) | `-1` | you need the position and no exception |
| `s.index(x)` | index | raises `ValueError` | a missing value means a bug |
| `x in s` | `True` | `False` | you only need yes or no |

- **Why immutable?** A string's **hash** (the number dicts use to find a key) can never change, so strings are safe dict keys. The cost: every "change" is a copy.
- **`strip(chars)` takes a set:** `"text.txt".strip(".txt")` gives `'e'`. Use `removesuffix` (3.9+), `os.path.splitext(p)` or `pathlib.Path(p).stem` instead.
- **Slice vs index:** `"abc"[5:]` is `''`, but `"abc"[5]` raises `IndexError`. So `s[:1]` is a safe "first character or empty".
- **`+=` vs `join`:** `+=` in a loop can recopy the whole string each time, which is slow on big inputs. Collect the pieces in a list and call `"".join(pieces)` once.
- **`split()` vs `split(sep)`:** no argument splits on any run of whitespace and drops empty pieces. `split(",", 1)` cuts once. `partition(sep)` returns `(before, sep, after)`.
- **`count` is case-sensitive and non-overlapping:** `"aaaa".count("aa")` is `2` and `"Python".count("p")` is `0`. Lowercase first to ignore case.
- **`str` vs `bytes`:** `bytes` is raw data (binary files, sockets, `subprocess`). `chr(233)` (`'é'`) has `len` 1 but is 2 bytes in **UTF-8**, an *encoding* (a rule mapping characters to bytes).
- **`sorted()` and `reversed()` don't return strings:** `sorted("cab")` is a list and `reversed("cab")` is an iterator (a one-pass stream). Wrap them in `"".join(...)`.

## 💡 Where This Shows Up in DevOps / Data Engineering Work
- **Parsing log lines:** `day, clock, level, msg = line.split(" ", 3)` on `"2026-10-02 10:15:03 ERROR payment-api timeout after 30s"` gives `level == 'ERROR'`. The `3` is **`maxsplit`** (the most cuts allowed), so the message stays in one piece.
- **Cleaning CSV / column headers** before loading into pandas or SQL: `" Order ID ".strip().lower().replace(" ", "_")` gives `'order_id'`. Stray spaces and capitals can't break joins.
- **Masking secrets in logs:** `"*" * (len(token) - 4) + token[-4:]` turns `demo-token-9876` into `***********9876`. Tokens of 4 characters or fewer would be shown in full, so mask those completely. Better still, never log secrets.
- **Splitting cloud paths:** `uri.removeprefix("s3://")` (3.9+) then `.split("/", 1)` turns `s3://my-bucket/raw/orders.parquet` into `['my-bucket', 'raw/orders.parquet']`, and `uri.endswith((".parquet", ".csv"))` filters file types.

## ❓ Interview Questions & Answers

1. **[Beginner] What does "strings are immutable" mean, and how do you "change" one?**
   You can't modify a string after it is created: `s[0] = "J"` raises `TypeError: 'str' object does not support item assignment`. Build a new one (`"J" + s[1:]` or `s.replace("P", "J")`) and re-assign the name. Methods never change the original.

2. **[Beginner] Predict the output:** `s = "Python"; print(s[2:], s[:-2], s[::2])`
   `thon Pyth Pto`. `s[2:]` starts at index 2, `s[:-2]` drops the last two letters, and `s[::2]` takes every second letter. (`s[::-1]` would reverse the string.)

3. **[Beginner] How do you turn `[1, 2, 3]` into the text `"1,2,3"`, and back?**
   `",".join(map(str, [1, 2, 3]))`. `join` needs strings: with ints it raises `TypeError: sequence item 0: expected str instance, int found`. Back: `"1,2,3".split(",")` gives `['1', '2', '3']` (still strings).

4. **[Intermediate] Predict the output:** `print("text.txt".strip(".txt"))`
   `e`. `strip(chars)` removes **any** of the characters `.`, `t`, `x` from both ends, not the text `.txt`. It stops at `e` because `e` isn't in that set. Use `"text.txt".removesuffix(".txt")` (3.9+) or `os.path.splitext`.

5. **[Intermediate] Predict the output:** `s = "abc"; print(repr(s[5:]), s[1:99])`, then `print(s[5])`
   `'' bc`, then `IndexError: string index out of range`. A slice trims out-of-range bounds to the string's ends. An index has nothing to return, so it raises. (`repr` shows the empty string as `''`.)

6. **[Intermediate] Predict the output:** `print("a  b".split(), "a  b".split(" "))`
   `['a', 'b'] ['a', '', 'b']`. `split()` treats any run of whitespace as one gap and drops empty pieces. `split(" ")` cuts at every single space, so two spaces leave an empty string between them.

7. **[Intermediate] How do `find` and `index` differ, and what is wrong with `if s.find("x"):`?**
   Both return the first match's position. With no match, `find` returns `-1` and `index` raises `ValueError`. `-1` is truthy (counts as true in an `if`) and a match at position `0` is falsy, so the `if` is wrong both ways. Use `if "x" in s:`.

8. **[Advanced] Why is `"".join(parts)` better than `result += part` in a loop?**
   Strings are immutable, so `+=` can build a new string and recopy everything so far on each step. The total work grows with the square of the length. `join` adds up the sizes first and copies once. CPython (the standard interpreter) speeds up a plain local `s += x`, but not when the string is also held elsewhere (for example in a list item), so don't rely on it.

9. **[Scenario] Your `.env` parser (a `.env` file holds `KEY=VALUE` settings) does `key, value = line.split("=")` and crashes on `BASE_URL=https://example.com/?a=1`. Why, and what is the fix?**
   The line has two `=` signs, so `split("=")` returns 3 pieces, and `key, value = ...` fails with `ValueError: too many values to unpack (expected 2)`. Cut only at the first `=`: `key, _, value = line.partition("=")` (or `line.split("=", 1)`).

10. **[Scenario] A script logs `b'deploy ok\n'`, and `out == "deploy ok"` is never true. Why?**
    `subprocess.run(..., capture_output=True).stdout` (`subprocess` runs another program) is **bytes**, and a `bytes` never equals a `str`. Decode it and trim the newline: `out.decode("utf-8").strip()`. Or pass `text=True` to get a `str` directly (the trailing newline is still there).

## 🔗 Related Topics
- **Also worth knowing:**
  - **Formatting:** `f"{x:.2f}"` and `str.format()` (the Basics README covers f-strings).
  - **Check and case helpers:** `isdigit()`, `isalpha()`, `isalnum()` (`"-12".isdigit()` is `False`), `title()`, `capitalize()`, and `casefold()` (a stronger `lower()` for comparing text).
  - **Padding and lines:** `zfill(5)`, `ljust` / `rjust` / `center`, and `splitlines()` for multi-line text.
  - **Characters and bytes:** `ord("A")` is `65` and `chr(97)` is `'a'`. Python 3 `str` is **Unicode** (a number for every character), and UTF-8 is the usual way to store it as bytes. Pass `encoding="utf-8"` to `open()`.
  - **String interning:** Python may reuse identical strings, so `is` can seem to work. Always compare strings with `==`.
  - **`pathlib` and `shlex`:** `pathlib.Path("data/sales.csv").stem` gives `'sales'`, which beats slicing file names. `shlex.split` and `shlex.quote` handle shell command strings safely.
  - **Regular_Expressions** (planned topic): the `re` module for patterns that `split` and `replace` can't express.
  - **List_Dict_Set_Comprehensions** (planned topic): one-line loops such as `[c.strip().lower() for c in cols]`.
- **Read alongside:**
  - [Basics of Python](../Basics_of_Python_01/README.md): f-strings, escape sequences and raw strings
  - [Lists](../Lists_Python_04/README.md): `split` / `join` convert between `str` and `list`, and slicing works the same way
  - [Tuples](../Tuples_Python_O5/README.md): also immutable, so many of the same rules apply
  - [Loops](../Loops_Python_07/README.md): looping over a string with `for ch in s`

---

## ⚡ Quick Revision: 5-Minute Interview Cheat Sheet

> **Say it in one breath:** "A string is an immutable row of characters: I index it with `s[0]` and `s[-1]`, slice it with `s[start:stop:step]` (stop excluded), and every method returns a new string. For real work I use `split`, `join`, `strip`, `partition` and `in`, and I decode `bytes` into `str`."

### 📋 Cheat sheet

| Need to... | Use | Example → Result |
|---|---|---|
| Read one character (from either end) | `s[i]` | `"Python"[-1]` → `'n'` |
| Take part of a string | `s[start:stop]` (stop excluded) | `"Python"[1:4]` → `'yth'` |
| Reverse a string | `s[::-1]` | `"abc"[::-1]` → `'cba'` |
| Ignore case when comparing | `s.lower()` | `"AbC".lower()` → `'abc'` |
| Replace text | `s.replace(old, new)` | `"banana".replace("a", "o")` → `'bonono'` |
| Trim spaces and newlines | `s.strip()` | `"  hi\n".strip()` → `'hi'` |
| Drop a known suffix (3.9+) | `s.removesuffix(x)` | `"data.csv".removesuffix(".csv")` → `'data'` |
| Split into a list | `s.split(sep, maxsplit)` | `"a,b,c".split(",", 1)` → `['a', 'b,c']` |
| Join a list into text | `sep.join(items)` | `"-".join(["a", "b"])` → `'a-b'` |
| Cut at the first `=` | `s.partition("=")` | `"k=v=w".partition("=")` → `('k', '=', 'v=w')` |
| Check how text starts or ends | `s.startswith(x)` / `s.endswith((a, b))` | `"x.csv".endswith((".csv", ".tsv"))` → `True` |
| Test "contains" | `x in s` | `"ell" in "hello"` → `True` |

### 🔥 Output drills (cover the right column, predict, then check)

| Code | Output |
|---|---|
| `print("aaaa".count("aa"))` | `2` |
| `print(bool("hello".find("h")), bool("hello".find("z")))` | `False True` |
| `print("web.com".lstrip("www."))` | `eb.com` |
| `print("a,b,,c".split(","), "".split(","), "".split())` | `['a', 'b', '', 'c'] [''] []` |
| `print("abcdef"[4:1:-1], "abcdef"[::-2])` | `edc fdb` |
| `s = "hi"; t = s; s += "!"; print(t, s)` | `hi hi!` |
| `print(len(chr(233)), len(chr(233).encode("utf-8")))` | `1 2` |
| `print(sorted("cab"), "".join(reversed("cab")))` | `['a', 'b', 'c'] bac` |

### 🧷 Rules & traps to remember
- **Immutable:** `s[0] = "J"` raises `TypeError`, and a bare `s.upper()` is thrown away. Write `s = s.upper()`.
- **Slice vs index:** `"abc"[5:]` is `''`, but `"abc"[5]` raises `IndexError`.
- **Stop is excluded:** `s[a:b]` has `b - a` characters, and `s[-3:]` is the last three.
- **`strip(chars)`:** removes any of those characters from the ends, not a prefix or suffix. Use `removesuffix`.
- **`find`:** `-1` counts as true and `0` as false, so test with `in`, not `if s.find(x):`.
- **No auto-convert:** `"id" + 5` raises `TypeError`. Use `f"id{5}"` or `str(5)`.
- **Don't shadow:** never name a variable `str`, and never name a file `string.py`.
- **Bytes are not text:** decode `subprocess` and socket output, and compare strings with `==`, never `is`.

### ✅ Last-minute checklist
- [ ] I can explain why `s[0] = "J"` fails and show two ways to get the changed text.
- [ ] I can predict any slice by hand, including negative bounds, a step and `[::-1]`.
- [ ] I can say what `strip(".txt")` really does and give the safe replacement.
- [ ] I can parse a log line or a `KEY=VALUE` line with `split(sep, maxsplit)` or `partition`.
- [ ] I can say when I get `bytes` and how to turn it into `str`.
