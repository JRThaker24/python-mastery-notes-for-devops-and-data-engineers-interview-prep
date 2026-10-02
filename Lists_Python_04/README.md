# Lists in Python

> **One-line definition:** A **list** is an **ordered** (items keep their position, they are not sorted), **mutable** (changeable after creation) collection in square brackets, and it can mix types: `[10, "a", 2.5]`.

## 🎯 TL;DR (30-second recall)
- A list is **ordered** and **mutable**, and it can hold mixed types. Indexes start at **0**, and `-1` is the last item.
- A **slice** `a[start:stop]` includes `start`, **excludes** `stop`, and gives a **new** list. A bad index raises `IndexError`, but an **out-of-range** slice never does.
- Add with `append` (one item), `extend` (many items) or `insert(i, x)`. Remove with `remove(value)`, `pop(index)`, `del` or `clear()`.
- `b = a` does **not** copy. Both names share one list. Copy with `a.copy()`, `a[:]` or `list(a)`.
- An **array** (`import array`) is the typed, compact cousin: every item has the same type. For data work, use NumPy.

## 📖 Concept Explained (from this folder's code)

> 🏷️ **Analogy:** a list is a **row of numbered lockers**. The locker number is the **index** (the position, starting at 0). Each locker can hold anything, and you can add, empty or swap lockers at any time.

### 1. What a list is, looping and `in`: [List.py](List.py)

```python
Data = ["Python", 2.24, 2025]

for x in Data:
    print(x)

if 2025 in Data:
    print("Yes Present")
```

- **`for x in Data`** hands over the items one by one, in order. The three items have three types (`str`, `float`, `int`), and a list does not care.
- **`2025 in Data`** is a **membership test**: Python compares each item with `2025`, left to right, and answers `True` or `False`.

> ⚠️ **Note on `List.py`:** the comment `Data = ["Python, 2.24, 2025"]` makes a **one-item** list, because the quotes wrap everything into one string (`len` is `1`). Quote each item separately. The comment `colors = [red, blue, green]` (no quotes) raises `NameError: name 'red' is not defined`, because Python looks for variables called `red`, `blue` and `green`.

### 2. Indexing: [List_Index.py](List_Index.py)

```python
numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print("First Element: ", numbers[0] )              # 10
print("Fifth Element: ", numbers[5] )              # 60
print("Last Element: ", numbers[-1])               # 100
print("Fifth from Last Element: ", numbers[-5])    # 60
numbers[3] = 200
print(numbers)     # [10, 20, 30, 200, 50, 60, 70, 80, 90, 100]
```

- An **index** is an item's position. Forward indexes start at **0**. **Reverse** indexes count from the end: for `[10, 20, 30]` they are `-3, -2, -1`. So `a[-k]` is just `a[len(a) - k]`, where `len(a)` counts the items (it prints `5` for the list in `List_Methods.py`).
- `numbers[3] = 200` puts a new object into slot 3 of the **same** list. No new list is made, because lists are mutable.

> ⚠️ **Note on `List_Index.py`:** `numbers[5]` is labelled "Fifth Element", but it is the **sixth** item (60), because counting starts at 0. The fifth is `numbers[4]` (50). `numbers[-5]` is also 60 only because the list has 10 items: `-5` means `10 - 5 = 5`.

### 3. List methods: [List_Methods.py](List_Methods.py)

| Goal | Code from the file | Returns | Good to know |
|---|---|---|---|
| Join two lists | `numbers + numbers2` | a **new** list | originals unchanged, so `numbers3` never gets the later `2028` |
| Add one item at the end | `numbers.append(2028)` | `None` | adds exactly one object |
| Add at a position | `numbers3.insert(1, "Data_Structure_Algorithms")` | `None` | later items shift right |
| Delete by **value** | `numbers3.remove(15)` | `None` | first match only, `ValueError` if missing |
| Delete by **index** | `numbers3.pop(2)` and `numbers3.pop()` | the removed item | `pop()` takes the last, `IndexError` if out of range |
| Delete an index or slice | `del numbers3[3]` | nothing | `del` is a **statement** (a keyword command, like `if`), not a method |
| Add many items | `numbers3.extend(["java", "SQL"])` | `None` | adds each item of any **iterable** (anything you can loop over) |
| Empty the list | `numbers.clear()` | `None` | the list stays, now `[]` |

```python
combine = [figures, alpha]    # figures = [1,2,3,4] and alpha = ["a","b","c","d"]
print(combine)                # [[1, 2, 3, 4], ['a', 'b', 'c', 'd']]
del numbers                   # removes the name itself
print(numbers)                # NameError: name 'numbers' is not defined
```

> ⚠️ **Note on `List_Methods.py`:** the last two lines (`del numbers`, then `print(numbers)`) raise `NameError: name 'numbers' is not defined`, so the script ends with a traceback (an error report). A **name** is a label stuck on an object: `del` removes the label, whereas `clear()` empties the list but keeps it.

> ⚠️ **Note on `List_Methods.py`:** a comment says `del` can "delete multiple values", but `del numbers3[3]` deletes one index. To delete several, use a slice: `del lst[1:3]` turns `[0, 1, 2, 3, 4]` into `[0, 3, 4]`.

> ⚠️ **Note on `List_Methods.py`:** `combine = [figures, alpha]` makes a **nested list** (a list of lists), not a merged one. To merge, use `figures + alpha` (new list) or `figures.extend(alpha)` (in place).

### 4. Slicing: [Slicicng_List.py](Slicicng_List.py)

```python
numbers = [10, 20, 30, 40, 50]
print(numbers[1:4])                  # [20, 30, 40]   start included, stop excluded
print(numbers[-4:-1])                # [20, 30, 40]   negative indexes work too
print(numbers[:4])                   # [10, 20, 30, 40]   start defaults to 0
print(numbers[3:])                   # [40, 50]   stop defaults to the end
numbers[:4] = [-10, -20, -30, -40]   # replace a slice -> [-10, -20, -30, -40, 50]
numbers[:2] = []                     # replace with nothing = delete -> [-30, -40, 50]
numbers_copy = numbers[:]            # full slice = copy
numbers[:] = []                      # replace everything = clear -> []
```

- A **slice** `a[start:stop]` copies the items from `start` up to, but **not including**, `stop` into a **new** list. So reading a slice never changes the original.
- **Assigning** to a slice does change the list, and the new part can be any length, so the list can grow or shrink. `a[:2] = []` equals `del a[:2]`.
- `numbers[:]` is a **shallow copy**: a new outer list holding the same inner objects. `numbers[:] = []` empties the **same** list, so every name pointing at it sees `[]`. `numbers = []` would only re-point one name.

### 5. Array vs list: [Array-In-Python.py](../Array-In-Python.py)

```python
import array
vals = array.array('i',[1, 2, 3, 4, 5])   # 'i' = signed int
vals.append(6)
vals.insert(2, 7)
vals.remove(4)
vals.pop(2)
vals.tolist()              # returns a list, but nothing keeps it
print(vals)                # still array('i', [...])
newarray = array.array(vals.typecode, (a*a for a in vals))   # squares, same type code
```

An **array** (from the `array` module) is a list-like container where every item must be the **same type**, usually numbers. `'i'` is the **type code** for a signed int (a whole number, positive or negative), and `'d'` is for floats. It stores the raw numbers side by side. A list stores one **pointer** (a reference to an object kept elsewhere) per item. That is why big numeric data takes less memory in an array.

| | `list` | `array.array` | `tuple` |
|---|---|---|---|
| Item types | any mix | **one** type (`'i'` int, `'d'` float) | any mix |
| Mutable? | yes | yes | **no** |
| Stores | pointers to Python objects | raw values (typically 4 bytes each for `'i'`) | pointers, like a list |
| Written as | `[1, "a"]` | `array.array('i', [1, 2])` | `(1, "a")` |
| Use it for | everyday collections | big numeric buffers, binary I/O | fixed records, dict keys |

- A wrong type raises `TypeError` (`append(2.5)` on an `'i'` array). A number too big for the type raises `OverflowError`.
- It has the usual list methods (`append`, `extend`, `insert`, `remove`, `pop`, `reverse`, `count`, `index`) but **no `sort()`, `clear()` or `copy()`** (checked on Python 3.9.6; newer versions may add some).

> ⚠️ **Note on `Array-In-Python.py`:** `vals.tolist()` returns a **new list**, but the result is thrown away, so `print(vals)` still shows an `array`. Write `as_list = vals.tolist()`. Also, `vals.count(2)` returns how many times `2` appears (here `1`), not "the number of elements" as the comment says.

## 🧠 Important Notes You Should Also Know

| Start with `a = [1]` | What it does | Result |
|---|---|---|
| `a.append([2, 3])` | adds **one** object, so it nests | `[1, [2, 3]]` |
| `a.extend([2, 3])` | adds **each item**; changes `a` itself (**in place**) | `[1, 2, 3]` |
| `a + [2, 3]` | builds a **new** list, `a` is unchanged | `[1, 2, 3]` |
| `a += [2, 3]` | same as `extend`, in place | `[1, 2, 3]` |

- **Alias vs copy:** `b = a` makes `b` an **alias** (a second name for the SAME list). `a.copy()`, `a[:]` and `list(a)` make **shallow** copies (inner lists still shared). Use `copy.deepcopy(a)` for nested data.
- **The `[[0] * 3] * 3` trap:** `*` repeats the same inner list three times (three references to one object). Build rows with `[[0] * 3 for _ in range(3)]`.
- **Index vs slice:** `a[99]` raises `IndexError`, but `a[99:]` quietly gives `[]` and `a[1:99]` stops at the end. Slices are clipped to the list, indexes are not.
- **`sort()` vs `sorted()`:** `a.sort()` sorts in place and returns `None` on purpose, so you notice no copy was made. `sorted(a)` returns a new list. Both accept `key=` (what to compare by) and `reverse=`, and are **stable** (equal items keep their order).
- **Don't add or remove while looping:** deleting shifts later items left, so the loop skips one. Loop over a copy (`for x in a[:]`) or build a new list with a list comprehension (`[x for x in a if ...]`).
- **Speed:** `a[i]` and `append` are **O(1)** (constant time; `append` is *amortised*, i.e. averaged). `insert(0, x)`, `pop(0)` and `x in a` are **O(n)** (grows with length): use `collections.deque` (fast at both ends) or a `set` (fast lookup).
- **Dedupe:** `list(dict.fromkeys(xs))` removes duplicates and keeps first-seen order (dicts keep insertion order since Python 3.7). `list(set(xs))` makes no order promise.
- **Return values and errors:** `append`, `extend`, `insert`, `remove` and `clear` return `None`, so `a = a.append(1)` makes `a` equal `None`. `remove(x)` raises `ValueError` if `x` is missing, and `pop()` on an empty list raises `IndexError`.

## 💡 Where This Shows Up in DevOps / Data Engineering Work
- **Batching API or DB calls:** services often cap the items per call (check the vendor docs for the limit), so split a list: `for i in range(0, len(ids), n): batch = ids[i:i + n]`. The last batch is just shorter, and the slice never raises.
- **Log files as lists of lines:** after `from pathlib import Path`, `lines = Path("app.log").read_text().splitlines()` gives a list of strings. Then `errors = [ln for ln in lines if "ERROR" in ln]` keeps the ones you care about.
- **Newest files first:** `sorted(Path("logs").glob("*.log"), key=lambda p: p.stat().st_mtime, reverse=True)` orders files by modified time. Take `[:5]` for the five newest.
- **JSON-like records:** an API's JSON array loads as a **list of dicts**, such as `[{"id": 1, "status": "ok"}]`. Filter with a comprehension and dedupe IDs with `list(dict.fromkeys(ids))`.

## ❓ Interview Questions & Answers

1. **[Beginner] What is a list, and how does it differ from a tuple and an `array`?**
   A list is an ordered, mutable collection that can mix types. A **tuple** is ordered but **immutable** (it can't change after creation), so it can be a dict key if its items are immutable too. An `array.array` is mutable but holds **one** type (usually numbers), which makes it compact.

2. **[Beginner] Predict the output:** `a = [10, 20, 30, 40, 50]; print(a[1:4], a[-2:], a[::-1])`
   `[20, 30, 40] [40, 50] [50, 40, 30, 20, 10]`. The stop index is excluded, `-2:` takes the last two items, and a step of `-1` walks backwards.

3. **[Beginner] Predict the output:** `a = [1, 2]; a.append([3, 4]); b = [1, 2]; b.extend([3, 4]); print(a, b)`
   `[1, 2, [3, 4]] [1, 2, 3, 4]`. `append` adds **one** object (a nested list). `extend` adds **each item**.

4. **[Intermediate] How do `remove`, `pop`, `del` and `clear` differ?**
   `remove(v)` deletes the first item equal to `v` (`ValueError` if absent). `pop(i)` deletes by index (the last item by default) and **returns** it. `del a[i]` or `del a[i:j]` is a statement that also accepts slices. `clear()` empties the list in place, while `del a` removes the name itself.

5. **[Intermediate] Predict the output:** `nums = [3, 1, 2]; print(nums.sort(), sorted(nums, reverse=True), nums)`
   `None [3, 2, 1] [1, 2, 3]`. `sort()` works in place and returns `None`. `sorted()` returns a new list. Arguments are evaluated left to right, so `nums` is already sorted when it is printed.

6. **[Intermediate] Predict the output:** `grid = [[0] * 3] * 3; grid[0][0] = 1; print(grid)`
   `[[1, 0, 0], [1, 0, 0], [1, 0, 0]]`. `* 3` repeats the **reference** to one inner list. Fix: `[[0] * 3 for _ in range(3)]`.

7. **[Advanced] Predict the output:** `import copy; a = [[1, 2], [3]]; b = a; c = a.copy(); d = copy.deepcopy(a); a[0].append(99); print(b, c, d)`
   `[[1, 2, 99], [3]] [[1, 2, 99], [3]] [[1, 2], [3]]`. `b` is the same list. `c` is a **shallow** copy, so its inner lists are shared. `d` is a **deep** copy with its own inner lists.

8. **[Advanced] What do `append`, `insert(0, x)`, `pop(0)` and `x in a` cost, and what can you use instead?**
   `append` is O(1) *amortised*: spare room is pre-allocated, so resizes are rare. `insert(0, x)`, `pop(0)` and `x in a` are O(n) because items shift or get scanned. Use `collections.deque` for queues (O(1) at both ends) and a `set` for fast membership tests.

9. **[Scenario] A cleanup script loops over `files` and calls `files.remove(f)` for every name ending in `.tmp`. With `["a.tmp", "b.tmp", "c.log"]` it leaves `b.tmp` behind. Why, and what is the fix?**
   Removing `a.tmp` shifts `b.tmp` into slot 0, but the loop moves on to slot 1, so `b.tmp` is skipped. The result is `['b.tmp', 'c.log']`. Fix: `files = [f for f in files if not f.endswith(".tmp")]`.

10. **[Scenario] An API returns thousands of IDs with duplicates, and its bulk endpoint accepts at most 500 per call. How do you prepare the calls and keep the order?**
    `ids = list(dict.fromkeys(ids))` dedupes and keeps first-seen order. Then `for i in range(0, len(ids), 500): call(ids[i:i + 500])`. The last slice is simply shorter and never raises.

## 🔗 Related Topics
- **Also worth knowing:**
  - **List comprehensions:** `[x * 2 for x in xs if x > 0]` builds a list in one line. List_Dict_Set_Comprehensions covers the dict and set versions too.
  - **`enumerate`, `zip` and unpacking:** `for i, x in enumerate(xs)`, `zip(a, b)` and `first, *rest = xs` replace most index juggling.
  - **Stack, queue and heap:** a list is a fine stack (`append` / `pop`). Use `collections.deque` for a queue, `heapq` for a priority queue and `bisect` for binary search on a sorted list.
  - **Generators and `yield`** (Generators_And_Yield): produce items one at a time instead of building a whole list in memory. `itertools.batched` (Python 3.12+, not run here) batches any iterable.
  - **Mutable vs immutable and hashable:** this is why a list can't be a dict key or set member (`TypeError: unhashable type: 'list'`), but a tuple can.
- **Read alongside:**
  - [Tuples](../Tuples_Python_O5/README.md): the immutable cousin of a list
  - [Dictionaries](../Dictionary_Python_06/README.md): a list of dicts is the shape of most JSON data
  - [Sets](../Sets_Python_07/README.md): unique items and fast membership tests
  - [Strings](../String_Python_03/README.md): same slicing rules, and `split` / `join` convert between `str` and list

---

## ⚡ Quick Revision: 5-Minute Interview Cheat Sheet

> **Say it in one breath:** A list is an ordered, mutable collection that can mix types. Indexes start at 0, a slice excludes its stop index, and `b = a` shares the list instead of copying it, so use `a.copy()` or `a[:]`.

### 📋 Cheat sheet

| Need to... | Use | Example → Result |
|---|---|---|
| Add one item / many items | `append(x)` / `extend(it)` | `a = [1]; a.append(2); a.extend([3, 4])` → `[1, 2, 3, 4]` |
| Insert at an index | `insert(i, x)` | `a = [1, 3]; a.insert(1, 2)` → `[1, 2, 3]` |
| Delete by value (first match) | `remove(v)` | `a = [1, 2, 1]; a.remove(1)` → `[2, 1]` |
| Delete by index and get it back | `pop(i)` or `pop()` | `a = [1, 2, 3]; a.pop()` → `3`, and `a` is `[1, 2]` |
| Delete an index or a slice | `del a[i]` / `del a[i:j]` | `a = [0, 1, 2, 3, 4]; del a[1:3]` → `[0, 3, 4]` |
| Empty it but keep it | `a.clear()` or `a[:] = []` | `a = [1, 2]; a.clear()` → `[]` |
| Copy (shallow / deep) | `a.copy()`, `a[:]`, `list(a)` / `copy.deepcopy(a)` | `b = a[:]` → `b is a` is `False` |
| Sort | `a.sort()` (returns `None`) / `sorted(a)` (new list) | `sorted([3, 1, 2], reverse=True)` → `[3, 2, 1]` |
| Reverse | `a[::-1]` (new) / `a.reverse()` (in place) | `[1, 2, 3][::-1]` → `[3, 2, 1]` |
| Dedupe, keep order | `list(dict.fromkeys(a))` | `[3, 1, 3, 2]` → `[3, 1, 2]` |

### 🔥 Output drills (cover the right column, predict, then check)

| Code | Output |
|---|---|
| `a = [1, 2]; b = a; a += [3]; a = a + [4]; print(b, a)` | `[1, 2, 3] [1, 2, 3, 4]` |
| `a = [1]; a.extend("hi"); print(a)` | `[1, 'h', 'i']` |
| `a = [1, 2, 3]; a.insert(-1, 9); print(a)` | `[1, 2, 9, 3]` |
| `print(sorted(["10", "9", "2"]), sorted([10, 9, 2]))` | `['10', '2', '9'] [2, 9, 10]` |
| `a = [1, 2, 3, 4]; a[1:3] = [9]; print(a)` | `[1, 9, 4]` |
| `a = [1, 2]; b = a; a = []; c = [1, 2]; d = c; c[:] = []; print(b, d)` | `[1, 2] []` |
| `print(list({"b": 1, "a": 2}), list("hi"))` | `['b', 'a'] ['h', 'i']` |

### 🧷 Rules & traps to remember
- **Index vs slice:** `a[5]` is the 6th item and a bad index raises `IndexError`. An out-of-range slice never does, and `a[i:j]` excludes `j`.
- **Slice assignment:** `a[i:j] = [...]` changes the list itself and can change its length.
- **Shared references:** `b = a` and `[[0] * 3] * 3` both share objects. Copy with `a.copy()` and use `copy.deepcopy` for nested lists.
- **`None` returns:** in-place methods (`append`, `sort`, `reverse`, `extend`) return `None`, so never write `a = a.sort()`.
- **`+` vs `+=`:** `+=` changes the list in place (aliases see it), while `a = a + [x]` builds a new one.
- **`del` vs `clear`:** `del a` deletes the name (later use gives `NameError`). `a.clear()` or `a[:] = []` empties the list.
- **Looping:** never add or remove items while looping over the same list. Loop over `a[:]` or build a new list.
- **Speed:** `x in a`, `insert(0, x)` and `pop(0)` are O(n). Use a `set` or a `deque`.

### ✅ Last-minute checklist
- [ ] I can explain list vs tuple vs array in one sentence each.
- [ ] I can predict slices like `a[1:4]`, `a[-2:]` and `a[::-1]`, and slice assignment.
- [ ] I can choose between `remove`, `pop`, `del` and `clear`, and name the error each can raise.
- [ ] I can explain alias vs shallow copy vs deep copy with a nested-list example.
- [ ] I can name the cost of `append`, `insert(0, x)` and `x in a`, and the faster alternative.
