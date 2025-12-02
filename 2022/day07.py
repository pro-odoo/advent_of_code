from collections import defaultdict


def solve_file(filename: str) -> int:
    sizes = []          # tailles finales de tous les dossiers
    stack = []          # pile des tailles cumulées du chemin courant

    with open(filename, encoding="utf-8") as f:
        for raw in f:
            parts = raw.strip().split()
            if not parts:
                continue

            if parts[0] == '$' and parts[1] == 'cd':
                tgt = parts[2]
                if tgt == '/':
                    # remonter à la racine
                    while len(stack) > 1:
                        s = stack.pop()
                        stack[-1] += s
                        sizes.append(s)
                    if not stack:
                        stack = [0]  # créer la racine si vide
                elif tgt == '..':
                    if len(stack) > 1:
                        s = stack.pop()
                        stack[-1] += s
                        sizes.append(s)
                else:
                    stack.append(0)  # entrer dans un sous-dossier
            elif parts[0].isdigit():
                # ligne fichier: "<size> <name>"
                size = int(parts[0])
                if not stack:
                    # sécurité si l'entrée ne commence pas par "cd /"
                    stack = [0]
                stack[-1] += size
            # "$ ls" et "dir <name>" ignorés

    # clôturer en fin de fichier
    while len(stack) > 1:
        s = stack.pop()
        stack[-1] += s
        sizes.append(s)
    if stack:
        sizes.append(stack[0])

    return sum(s for s in sizes if s <= 100_000)


if __name__ == "__main__":
    print(solve_file("input07.txt"))
