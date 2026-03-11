import ttg

premises   = [
    "p→q",
    "p∧r",
    "¬q∨r"
]
conclusion = "r"


def translateFormula(formula: str) -> str:
    f = formula.replace(" ", "")
    f = f.replace("¬", "not ")
    f = f.replace("∧", " and ")
    f = f.replace("∨", " or ")
    f = f.replace("→", " => ")
    f = f.replace("↔", " = ")
    return f


SYMBOLS = {'¬', '∧', '∨', '→', '↔', '(', ')', ' '}

def extractVariables(formulas: list) -> list:
    variables = set()
    for formula in formulas:
        for token in formula:
            if token not in SYMBOLS:
                variables.add(token)
    return sorted(variables)


def generateTruthTable(premises: list, conclusion: str):
    all_formulas    = premises + [conclusion]
    variables       = extractVariables(all_formulas)
    translated      = [translateFormula(f) for f in all_formulas]
    prem_translated = translated[:-1]

    print(f"\n\t\tTABLA DE VERDAD")
    tabla = ttg.Truths(variables, translated, ints=False)
    print(tabla)

    df        = tabla.as_pandas
    col_names = list(df.columns)
    prem_idxs = [col_names.index(p) for p in prem_translated]
    conc_idx  = len(col_names) - 1

    invalid_rows  = []
    critical_rows = []

    for _, row in df.iterrows():
        row_vals       = list(row)
        all_prems_true = all(row_vals[i] == True for i in prem_idxs)
        conc_true      = row_vals[conc_idx] == True

        if all_prems_true:
            if conc_true:
                critical_rows.append(row_vals)
                #print(f"Filas criticas: {critical_rows}")
            else:
                invalid_rows.append(row_vals)
                #print(f"Filas invalidas: {invalid_rows}")

    print()
    if invalid_rows:
        print("ARGUMENTO INVALIDO")
    elif critical_rows:
        print("ARGUMENTO VALIDO")
    else:
        print("las premisas nunca son todas T al mismo tiempo")


if __name__ == "__main__":
    generateTruthTable(premises, conclusion)