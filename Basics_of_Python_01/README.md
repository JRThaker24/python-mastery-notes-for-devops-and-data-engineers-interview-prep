# Basics of Python: Variables, Output, Input & Operators

> **One-line definition:** Python is a **dynamically typed** language. A variable is just a name pointing to an object, and operators act on those objects to calculate, compare or combine values.

## 🎯 TL;DR (30-second recall)
- **Dynamic typing:** there's no type declaration. The *object* has a type, the *name* doesn't. `x = 10` then `x = "hi"` is fine.
- `==` checks **value equality**. `is` checks **identity**, meaning the same object in memory (`id()`).
- **f-strings** (`f"{name}"`) are the modern, fastest and most readable way to format output.
- `input()` **always returns `str`**. Convert it with `int()` / `float()`.
- `/` always returns a `float`. `//` is **floor division** and rounds **down toward −∞**, not toward zero.
- `and` / `or` **short-circuit** and return one of the **operands**, not necessarily `True`/`False`.

## 📖 Concept Explained (from this folder's code)

### 1. Dynamic typing, `id()` and identity operators: [Dynamic_Nature_Python.py](Dynamic_Nature_Python.py)

```python
a = 10
print(id(a))          # an integer, unique for this object while it lives

x = 10
y = 10
if x is y:            # prints "same"
    print("same")
```

- In C or Java you write `int a = 10;`. In Python you write `a = 10` and the type is decided at **runtime**.
- **`id(obj)`** returns the object's identity. In CPython (the standard Python interpreter) this is the memory address.
- **`is` / `is not`** compare identities, not values.
- **Why does `x is y` print "same" here?** CPython keeps a **small-integer cache** for -5 to 256. Every `10` in your program points to the *same* pre-built object. That's an implementation detail, so never rely on it (see Notes).

> 🏷️ **Analogy:** a variable is a **sticky label**, not a box. `x = 10` and `y = 10` can be two labels stuck on the same object.

### 2. Escape sequences and raw strings: [Escape_Sequence.py](Escape_Sequence.py)

```python
print("Happy\tnew\tYear")     # \t = tab
print("Hello \nWorld ")       # \n = new line
print("Hello \'world\' ")     # \' = literal single quote
print("Hello \"World\" ")     # \" = literal double quote
print(r"\n")                  # r"" = raw string, prints the 2 characters \ and n
```

- An **escape sequence** is a backslash plus a character that means something special inside a string.
- A **raw string** (`r"..."`) turns escaping off. That's why the file uses `r"..."` to *display* `\n` and `\t` literally.
- You could skip `\'` by mixing quote types: `"Hello 'world'"`.

### 3. Five ways to print variables: [Print_Vaules_of_Variables_&_String_Formatting.py](Print_Vaules_of_Variables_%26_String_Formatting.py)

```python
name = "Python"
year = "2025"

print("Name: ", name, "Year: ", year)                    # 1. comma
print("Name: " + name + " Year: " + str(year))           # 2. concatenation
print("Name: {} Year: {}".format(name, year))            # 3. format() (auto order)
print("Name: {0} Year: {1}".format(name, year))          # 4. format() (positions)
print("Name: {n} Year: {y}".format(n=name, y=year))      #    format() (keywords)
print(f"Name: {name} Year: {year}")                      # 5. f-string ✅
```

| Method | Auto-converts types? | Readability | Notes |
|---|---|---|---|
| `print(a, b)` comma | ✅ | OK | Adds a space between items. Change it with `sep=`. |
| `+` concatenation | ❌ (`TypeError` on `int`) | Poor | Needs `str()`. In this file `year` is already a string, so `str(year)` does nothing, but it would matter if `year = 2025`. |
| `"%s" % x` (old style) | ✅ | OK | Legacy, but still used by the `logging` module |
| `str.format()` | ✅ | Good | Useful for reusable template strings |
| **f-string** `f"{x}"` | ✅ | **Best** | Python 3.6+. Fastest. Any expression works inside `{}`. |

### 4. Taking user input: [input_fucntion.py](input_fucntion.py)

```python
a = int(input("Enter any number: "))
b = float(input("Enter any number: "))
c = a + b          # int + float -> float
print(c)
```

- `input()` returns a **string**, so the code wraps it in `int()` / `float()`.
- `int + float` gives a `float`. Python **widens** to the more general numeric type.
- ⚠️ Typing `3.5` at the `int()` prompt raises `ValueError`. `int()` won't parse a decimal string.

### 5. Operators: [Operators/](Operators/)

| File | Operator(s) | Example from the file | Result |
|---|---|---|---|
| [Assignment_Operator.py](Operators/Assignment_Operator.py) | `= += -= *= /= %= **= //=` | `a += b` means `a = a + b` | n/a |
| [Floor_Division_Operator.py](Operators/Floor_Division_Operator.py) | `//` | `5 // 2` | `2` |
| [Power_Operator.py](Operators/Power_Operator.py) | `**` | `5 ** 3` | `125` |
| [Relational_Operator.py](Operators/Relational_Operator.py) | `== != < <= > >=` | `10 == 10` | `True` |
| [Logical_Operators.py](Operators/Logical_Operators.py) | `and or not` | *(comments only, see below)* | n/a |

`Logical_Operators.py` only lists the three operators. Here's the runnable version:

```python
print(True and False)   # False: both sides must be truthy
print(True or False)    # True: at least one side truthy
print(not True)         # False

# They return an OPERAND, not a bool:
print(0 or "default")   # 'default'
print(3 and 5)          # 5
print(0 and 5)          # 0  (stops at the first falsy value)
```

> ⚠️ **Note on `Floor_Division_Operator.py`:** the comment says floor gives the "nearest whole number". More precisely, it rounds **down toward −∞**. `5 // 2 == 2`, but `-7 // 2 == -4`, not `-3`.

## 🧠 Important Notes You Should Also Know

| | `==` | `is` |
|---|---|---|
| Checks | Values are equal (`__eq__`) | Same object (`id(a) == id(b)`) |
| `[1] == [1]` | `True` | `False` (two different lists) |
| Use it for | Almost everything | **Only** `None`, `True`, `False` and sentinels: `if x is None:` |

- **Small-int cache:** `a = 256; b = int("256")` gives `a is b` → `True`, but with `257` it is `False` even though `a == b`. Never use `is` to compare numbers or strings.
- **Negative floor and modulo:** `-7 // 2 == -4` and `-7 % 2 == 1`. Python keeps `a == (a // b) * b + (a % b)` true.
- **Float precision:** `0.1 + 0.2 == 0.3` is `False`. Use `math.isclose()` for measurements and `decimal.Decimal` for money. `round(2.5) == 2` because ties go to the nearest even number.
- **`**` quirks:** it is right-associative (`2 ** 3 ** 2 == 512`) and binds tighter than unary minus (`-2 ** 2 == -4`).
- **No `++` / `--`:** `a++` is a `SyntaxError`. Write `a += 1`.
- **`+=` on a list changes it in place** (other names pointing to it see the change). `a = a + [x]` builds a **new** list.
- **Truthy / falsy:** `0`, `0.0`, `""`, `[]`, `{}`, `set()` and `None` are falsy. `"False"` and `"0"` are truthy. `bool` is a subclass of `int` (`True + True == 2`). Chained comparisons work: `1 < x < 5`.
- **f-string and `print()` tricks:** `f"{x=}"` prints `x=5` (3.8+), `f"{3.14159:.2f}"` gives `3.14`, `f"{1234567:,}"` gives `1,234,567`, and `print("a", "b", sep="-", end="!\n")` prints `a-b!`.

## 💡 Where This Shows Up in DevOps / Data Engineering Work
- **Config defaults with `or`:** `env = os.environ.get("APP_ENV") or "dev"` falls back when the variable is missing *or* empty.
- **Safe `None` checks:** `if response is None:` in API or DB code. `== None` can be fooled by a custom `__eq__`.
- **Batching and pagination with `//`:** the number of pages is `(total + size - 1) // size`. For 101 rows in pages of 25, that's `5` API calls or DB chunks.
- **Building commands and log lines with f-strings:** `f"kubectl rollout status deploy/{app} -n {ns}"`. Use raw strings for regex patterns in log parsing (`r"\d{3}"`).
- **Don't use `input()` in pipelines.** CI/CD jobs are non-interactive and will hang or fail. Use `argparse`, environment variables or config files.

## ❓ Interview Questions & Answers

1. **[Beginner] What does "dynamically typed" mean?**
   Types are checked at runtime and belong to *objects*, not variable names. You never declare a type, and one name can point to an `int` and later a `str`.

2. **[Beginner] What's the difference between `==` and `is`?**
   `==` compares values. `is` checks whether both names point to the **same object**. Use `is` only with `None`, `True` and `False`.

3. **[Beginner] What type does `input()` return?**
   Always `str`. `int(input())` converts it, and raises `ValueError` if the text isn't a valid integer (for example `"3.5"`).

4. **[Intermediate] Predict the output:** `print(-7 // 2, -7 % 2)`
   `-4 1`. Floor division rounds toward −∞, and the modulo result takes the divisor's sign.

5. **[Intermediate] Predict the output:** `print(0 or "N/A", 3 and 5, [] and 10)`
   `N/A 5 []`. `or` returns the first truthy operand. `and` returns the first falsy operand, or the last operand if all are truthy.

6. **[Intermediate] Why does `a = 10; b = 10; a is b` print `True`, but it can be `False` for `257`?**
   CPython caches the integers −5 to 256 as single shared objects. Larger integers created at runtime are separate objects. It's an implementation detail, so compare numbers with `==`.

7. **[Intermediate] Which string formatting method would you use, and why?**
   f-strings: they're the most readable and fastest, and allow inline expressions. The exception is `logging`, where you pass `%s` arguments (`log.info("user %s", uid)`) so formatting only happens if the message is actually logged.

8. **[Advanced] What's the difference between `a += [4]` and `a = a + [4]` when `b = a` was set earlier?**
   `+=` changes the list **in place**, so `b` sees `[..., 4]`. `a = a + [4]` builds a **new** list and rebinds `a`, so `b` keeps the old list.

9. **[Advanced] Is `0.1 + 0.2 == 0.3`? How would you compare floats in a data pipeline?**
   `False`, because of binary floating-point precision. Use `math.isclose(a, b)` for measurements and `decimal.Decimal` for currency.

10. **[Scenario] A CI script uses `if os.getenv("DEBUG"):` and debug mode turns on even with `DEBUG=false`. Why?**
    Environment variables are strings, and any non-empty string is truthy, including `"false"` and `"0"`. Parse it explicitly: `os.getenv("DEBUG", "").lower() in ("1", "true", "yes")`.

## 🔗 Related Topics
- **Also worth knowing:**
  - **Data types overview:** `int`, `float`, `complex`, `bool`, `str` and `NoneType`. `type()` returns an object's type, and `isinstance(x, int)` is preferred for type checks.
  - **Mutable vs immutable:** numbers, strings and tuples are immutable, while lists, dicts and sets are mutable. This explains the `+=` gotcha above.
  - **Type conversion:** `int("10")`, `float("2.5")`, `str(5)`, `bool([])`. `int("0x1A", 16)` parses hexadecimal.
  - **Type hints** document intent without changing dynamic typing: `def add(a: int, b: int) -> int:`. Check them with `mypy`.
  - **Walrus operator `:=`** (Python 3.8+) assigns inside an expression: `while (line := f.readline()):`.
  - **Operator precedence (high → low):** `**` → unary `-` → `* / // %` → `+ -` → bitwise → comparisons → `not` → `and` → `or`.
- **Read alongside:**
  - [Bitwise Operators](../Bitwise_Operators_02/README.md): the other half of Python's operators
  - [Strings](../String_Python_03/README.md): more on string methods, slicing and formatting
  - [Conditional Practice](../conditional_practice/README.md): relational and logical operators in `if`/`else`
  - [Python Scope](../Python_Scope_14/README.md): how variable names are looked up

---

## ⚡ Quick Revision: 5-Minute Interview Cheat Sheet

> **Say it in one breath:** Python is dynamically typed: names are labels on objects, `==` compares values, `is` compares identity, `input()` always gives a string, `/` always gives a float, and `and` / `or` return one of their operands.

### 📋 Cheat sheet

| Need to... | Use | Example → Result |
|---|---|---|
| Check type / identity | `type(x)`, `id(x)` | `type(5 / 1)` → `<class 'float'>` |
| Compare values vs objects | `==` vs `is` | `a = [1]; b = [1]` → `a == b` is `True`, `a is b` is `False` |
| Format output (best way) | f-string | `f"{name!r} {3.14159:.2f}"` → `'Python' 3.14` |
| Read a number from the user | `int(input())` / `float(input())` | `int("3.5")` → `ValueError` |
| Divide / floor-divide / remainder | `/`, `//`, `%` | `7 / 2, 7 // 2, 7 % 2` → `3.5 3 1` |
| Power / modular power | `**`, `pow(b, e, m)` | `2 ** 10` → `1024` |
| Fall back to a default | `x or default` | `0 or "N/A"` → `'N/A'` |
| Test a range | `a < x < b` | `1 < 3 < 5` → `True` |
| Compare floats safely | `math.isclose(a, b)` | `math.isclose(0.1 + 0.2, 0.3)` → `True` |
| Print a literal `\n` | raw string `r"..."` | `print(r"\n")` → `\n` |
| Convert types | `int()`, `float()`, `str()`, `bool()` | `bool("False")` → `True` |

### 🔥 Output drills (cover the right column, predict, then check)

| Code | Output |
|---|---|
| `print(7 / 2, 7 // 2, 7 % 2, 2 ** 3)` | `3.5 3 1 8` |
| `print(2 ** 3 ** 2, -2 ** 2)` | `512 -4` |
| `print(True + True, bool("False"))` | `2 True` |
| `print(0.1 + 0.2 == 0.3)` | `False` |
| `print(round(2.5), round(3.5))` | `2 4` |
| `print(1 < 3 > 2)` | `True` |
| `print(7 % -3, -7 % 3)` | `-2 2` |
| `print("a", "b", sep="-", end="!")` | `a-b!` |

### 🧷 Rules & traps to remember
- **`is` is for `None`:** write `if x is None`, never `x is 256`.
- **`input()` is always `str`:** convert it. `int("3.5")` fails, so use `int(float("3.5"))` if decimals are possible.
- **Floor rounds toward −∞:** `-7 // 2 == -4`, not `-3`.
- **`**` goes right to left** and beats unary minus: `-2 ** 2 == -4`.
- **`and` / `or` return operands**, not just `True` / `False`.
- **Floats are approximate:** use `math.isclose`, and `Decimal` for money.
- **Env vars are strings:** `"false"` is truthy, so parse it explicitly.
- **No `++` / `--`**, and a raw string can't end in a single backslash.

### ✅ Last-minute checklist
- [ ] I can explain dynamic typing and "names are labels" in one sentence.
- [ ] I can say when `is` is correct and why `==` is the default.
- [ ] I can list the 5 ways to format output and name the best one.
- [ ] I can predict `//` and `%` with negative numbers.
- [ ] I know why `0.1 + 0.2 != 0.3` and what to use instead.
