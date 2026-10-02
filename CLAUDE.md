# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

A personal Python learning repo that is being turned into a public, interview-prep reference for DevOps / Data Engineering roles. The remote is `JRThaker24/python-mastery-notes-for-devops-and-data-engineers-interview-prep`. There is no package, build, dependency file, linter config or test suite. Each topic folder holds small standalone practice scripts, plus (once written) a `README.md` of revision notes.

The full brief for the README work is in `Complete-Detail-Python-Notes-Repo-Claude-Prompt.md`. Read it before generating or changing any topic notes.

## Running code

- Each `.py` file is an independent script: `python3 <Folder>/<File>.py`. Nothing imports anything else across files.
- Many scripts call `input()` (e.g. `Basics_of_Python_01/input_fucntion.py`, several `Loops_Python_07/` files, `conditional_practice/`). To run them non-interactively, pipe in stdin: `printf '5\n2.5\n' | python3 Basics_of_Python_01/input_fucntion.py`.
- `Files_Handing_Python_10/` scripts open `Sample_file.txt` / `Sample_file1.txt` by relative path, so run them from inside that folder. `File_Write.py` and `File_Copy.py` create `Sample_file1.txt`, and `File_Delete.py` removes it.
- Check snippets with `python3 -c "..."`. The local `python3` is 3.9, so 3.10+ features (`match`, `int.bit_count()`) won't run locally. Label them with their version in the notes.

## Repo layout quirks (don't "fix" these without asking)

- The folder names have uneven numbering and typos that the notes depend on: `Sets_Python_07` and `Loops_Python_07`, `Classes_Python_12` and `Inheritance_Python_12`, `Iterators_Python_14` and `Python_Scope_14`, `Tuples_Python_O5` (letter O), `Files_Handing_Python_10`. Filenames have typos too (`input_fucntion.py`, `Handling_Excemption.py`). Renaming them breaks links and history.
- Loose root files (`Array-In-Python.py`, `New-Learnings.py`, `Testing.py`, `if-else-01.py`, empty `if-else-02.py`) don't get their own READMEs. Their content goes into the nearest topic README instead:
  - `Array-In-Python.py` → Lists
  - `if-else-01.py` → `conditional_practice`
  - `Testing.py` → Loops (while-else) and Decorators (closures)
  - `New-Learnings.py` → Module (`math`), Functions (`**kwargs`), Scope (`globals()`) and Loops (fibonacci, prime check)
  - The root README lists all of them in a "Misc / scratch files" section.
- New topic folders use `Title_Case_With_Underscores` and contain one small runnable example `.py` plus a `README.md`.

## README conventions

Every topic `README.md` uses exactly this section order: `# Title` → `> **One-line definition:**` → `## 🎯 TL;DR (30-second recall)` → `## 📖 Concept Explained (from this folder's code)` → `## 🧠 Important Notes You Should Also Know` (**exactly 8 bullets**, plus at most one small comparison table) → `## 💡 Where This Shows Up in DevOps / Data Engineering Work` → `## ❓ Interview Questions & Answers` (**exactly 10** numbered items tagged **[Beginner]/[Intermediate]/[Advanced]**, DevOps/DE scenarios as **[Scenario]**; roughly 3 / 3–4 / 1–2 / 1–2, at least 3 "predict the output") → `## 🔗 Related Topics` (an "Also worth knowing" list plus 2–4 relative links to other topic READMEs) → a `---` line → `## ⚡ Quick Revision: 5-Minute Interview Cheat Sheet` as the **last** section.

The Quick Revision section has a `> **Say it in one breath:**` line, then `### 📋 Cheat sheet` (table `Need to... | Use | Example → Result`, 8–12 rows), `### 🔥 Output drills (cover the right column, predict, then check)` (table `Code | Output`, 6–8 rows), `### 🧷 Rules & traps to remember` (6–8 bold-keyword one-liners) and `### ✅ Last-minute checklist` (4–5 `- [ ] I can ...` items). Drill rows must be machine-checkable: each Code cell is one self-contained snippet that prints (no 3.10+ features), each Output cell is the exact stdout, and a `|` inside a cell is written `\|`. Keep drills and cheat-sheet examples different from the 10 questions.

- `Basics_of_Python_01/README.md` and `Bitwise_Operators_02/README.md` are the approved style references. Match their tone, length (about 190–240 lines) and structure.
- Roll the work out two topic folders at a time (parallel agents, one per folder, then a check of the output), then stop and wait for the user to review and say "continue". New topic folders and the root README come after all existing folders are done.
- Snippets in "Concept Explained" must be copied from the folder's actual files, not invented. Read every file first.
- **Don't edit the learner's `.py` files.** If a code comment or the logic is wrong, explain the correction in the README as a `> ⚠️` callout. Known examples:
  - The bitwise shift comments: the correct rules are `n << k == n * 2**k` and `n >> k == n // 2**k`.
  - The odd/even check in `if-else-01.py`: it uses `num/2 == 0` and should be `num % 2 == 0`.
- Run every "predict the output" answer and stated result before writing it down. Use `python3 -B` so no `__pycache__` is created in the repo.
- URL-encode special characters in relative links (`&` → `%26`, `'` → `%27`). Two files need this: `Print_Vaules_of_Variables_&_String_Formatting.py` and `Bitwise_One's_Complement_Operator.py`.

## Sensitive content

- A real personal phone number appears in `New-Learnings.py` (the `person(...)` example and a comment above it) and in `Inheritance_Python_12/Inheritance.py`. Never copy it into READMEs; use placeholder values, and check any other file you quote from.
- `settings.json` contains a local machine path with a username.
- Don't change these files unless the user asks.
