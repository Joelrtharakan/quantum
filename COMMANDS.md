# Commands – Case 16 (Grover's Search, marked |01>)

Run every command from the project folder:

```bash
cd /Users/joeltharakan/Documents/Quantum
```

The commands use the local environment `.venv`, so no `source .venv/bin/activate` is needed. These terminal commands are for checking and for extra output. The assignment's main evidence is the VS Code **Run** and **Histogram** screenshots (see README.md).

If `.venv` is missing or broken, recreate it:

```bash
python3 -m venv .venv && .venv/bin/pip install qsharp reportlab
```

---

## 1. Run the program once (prints register number + result)

```bash
.venv/bin/python -W ignore -c "import qsharp; qsharp.init(); qsharp.eval(open('URK23AI1047_Case16.qs').read()); print(qsharp.eval('Main()'))"
```

Expected: your register number on the first line, then `[Zero, One]` (that is |01>). `Main` runs with whatever `iterations` is set to in the file (it should be 1).

## 2. Run one Grover iteration, 1000 shots, with a text histogram

```bash
.venv/bin/python -W ignore -c "
import qsharp, collections
qsharp.init(); qsharp.eval(open('URK23AI1047_Case16.qs').read())
n=1
c=collections.Counter(''.join('0' if str(x)=='Zero' else '1' for x in qsharp.eval(f'Search({n})')) for _ in range(1000))
print('Iterations =',n)
for s in ['00','01','10','11']: print(f'  |{s}>  {c[s]:4d}  {c[s]/10:5.1f}%  '+'#'*(c[s]//20))
"
```

Expected: |01> 1000, 100.0%, and 0 for the others.

## 3. Run two Grover iterations, 1000 shots, with a text histogram

Same command with `n=2`:

```bash
.venv/bin/python -W ignore -c "
import qsharp, collections
qsharp.init(); qsharp.eval(open('URK23AI1047_Case16.qs').read())
n=2
c=collections.Counter(''.join('0' if str(x)=='Zero' else '1' for x in qsharp.eval(f'Search({n})')) for _ in range(1000))
print('Iterations =',n)
for s in ['00','01','10','11']: print(f'  |{s}>  {c[s]:4d}  {c[s]/10:5.1f}%  '+'#'*(c[s]//20))
"
```

Expected: all four states near 25% (about 220 to 280 counts each). The exact counts change on every run, because of random shot noise.

## 4. Both experiments in one go

```bash
.venv/bin/python -W ignore -c "
import qsharp, collections
qsharp.init(); qsharp.eval(open('URK23AI1047_Case16.qs').read())
for n in (1,2):
    c=collections.Counter(''.join('0' if str(x)=='Zero' else '1' for x in qsharp.eval(f'Search({n})')) for _ in range(1000))
    print('Iterations =',n)
    for s in ['00','01','10','11']: print(f'  |{s}>  {c[s]:4d}  {c[s]/10:5.1f}%  '+'#'*(c[s]//20))
"
```

## 5. Show the exact quantum state (amplitudes, no shot noise)

Useful for the viva. After 1 iteration: amplitude −1 on |01> (the sign is a global phase). After 2 iterations: ±0.5 on all four states.

```bash
.venv/bin/python -W ignore -c "
import qsharp
qsharp.init(); qsharp.eval(open('URK23AI1047_Case16.qs').read())
qsharp.eval('operation Dump(n:Int):Unit{use q=Qubit[2];H(q[0]);H(q[1]);for _ in 1..n{Oracle(q);Diffusion(q);}Microsoft.Quantum.Diagnostics.DumpMachine();ResetAll(q);}')
print('--- 1 iteration ---');  qsharp.eval('Dump(1)')
print('--- 2 iterations ---'); qsharp.eval('Dump(2)')
"
```

## 6. Check that the oracle marks only |01>

After the oracle alone, the |01> amplitude should have a minus sign and the other three a plus sign (all of size 0.5):

```bash
.venv/bin/python -W ignore -c "
import qsharp
qsharp.init(); qsharp.eval(open('URK23AI1047_Case16.qs').read())
qsharp.eval('operation T():Unit{use q=Qubit[2];H(q[0]);H(q[1]);Oracle(q);Microsoft.Quantum.Diagnostics.DumpMachine();ResetAll(q);}')
qsharp.eval('T()')
"
```

## 7. Check the file is ready for submission

Make sure the iteration count is back to 1 and the register number(s) are printed:

```bash
grep -n "iterations =\|Message" URK23AI1047_Case16.qs
```

Expected: `let iterations = 1;` and a `Message("...")` line with the real register numbers of all team members.

## 8. Build and open the report

Edit the `TEAM` list at the top of `report_tools/build_report.py` first, and save your screenshots in `screenshots/` with the names in README.md. Then:

```bash
.venv/bin/python report_tools/build_report.py && open URK23AI1047_Case16_Report.pdf
```

Any screenshot still missing shows as a red "NOT YET CAPTURED" box.

## 9. Check which screenshots are in place

```bash
ls -1 screenshots/
```

Required names: `1_code.png`, `2_output.png`, `3_histogram_1_iteration.png`, `4_histogram_2_iterations.png`.

## 10. In VS Code (main evidence)

- Open `URK23AI1047_Case16.qs`.
- Use the links on the line above `operation Main`: **Run**, **Histogram** (enter 1000 shots), **Circuit**.
- Or press Cmd+Shift+P and run `Q#: Run file`, `Q#: Show histogram` or `Q#: Show circuit`.
- To switch experiments, change `let iterations = 1;` to `2`, save with Cmd+S, and run again. Change it back to 1 before submitting.
