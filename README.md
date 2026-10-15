# hello-world

A minimal Python hello-world project, growing over time.

## Files

| File | Version | Description |
|---|---|---|
| `hello.py` | v1 | Smallest possible example |
| `hello_v2.py` | v2 | CLI greeting tool (arguments, options, tests) |
| `test_hello_v2.py` | — | Unit tests for v2 (stdlib `unittest`) |

## v1 — `hello.py`

```sh
python hello.py
```

```
Hello, World!
```

## v2 — `hello_v2.py`

A command-line greeting tool: no third-party dependencies.

```sh
python hello_v2.py                              # Hello, World!
python hello_v2.py Alice                        # Hello, Alice!
python hello_v2.py Alice Bob --greeting Hi      # one line per name
python hello_v2.py Alice --count 2 --shout      # HELLO, ALICE!  x2
python hello_v2.py --version                    # hello_v2 2.0.0
```

### Options

| Flag | Meaning |
|---|---|
| `NAME ...` | One or more names to greet (default: `World`) |
| `-g`, `--greeting` | Greeting word (default: `Hello`) |
| `-c`, `--count` | Repeat each greeting N times (default: `1`) |
| `-s`, `--shout` | Uppercase the output |
| `-V`, `--version` | Print the version and exit |

Exit codes: `0` success, `2` invalid input (e.g. `--count 0`).

## Tests

```sh
python -m unittest -v test_hello_v2
```

## License

MIT
