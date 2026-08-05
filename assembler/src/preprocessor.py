import re
 
import re

def split_args(s):
    args, cur, depth = [], "", 0
    for c in s:
        if c == "," and depth == 0:
            args.append(cur.strip())
            cur = ""
        else:
            depth += (c == "(") - (c == ")")
            cur += c
    return args + [cur.strip()] if s.strip() else []

def preprocess(src):
    macros = {}
    code = []

    # Parse #defines
    for line in src.splitlines():
        if m := re.match(r"\s*#define\s+(\w+)\((.*?)\)\s+(.+)", line):
            macros[m[1]] = (m[2].split(",") if m[2] else [], m[3])
        elif m := re.match(r"\s*#define\s+(\w+)\s+(.+)", line):
            macros[m[1]] = m[2]
        else:
            code.append(line)

    code = "\n".join(code)

    for _ in range(100):
        old = code

        # Function-like macros
        for name, macro in macros.items():
            if isinstance(macro, tuple):
                params, body = macro
                while m := re.search(rf"\b{name}\s*\(", code):
                    i = m.end()
                    depth = 1
                    while depth:
                        depth += (code[i] == "(") - (code[i] == ")")
                        i += 1

                    args = split_args(code[m.end():i-1])
                    if len(args) != len(params):
                        break

                    text = body
                    for p, a in zip(params, args):
                        text = re.sub(rf"\b{p}\b", a, text)

                    code = code[:m.start()] + text + code[i:]

        # Object-like macros
        for name, value in macros.items():
            if isinstance(value, str):
                code = re.sub(rf"\b{name}\b", value, code)

        if code == old:
            break

    return code
