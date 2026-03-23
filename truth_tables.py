import ttg

premises   = [
    "P → Q",
    "Q",
]
conclusion = "P"


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
    # [1,2,3,4,5,6]

    print(f"\n\t\tTABLA DE VERDAD")
    tabla = ttg.Truths(variables, translated, ints=False)
    print(tabla)

    df        = tabla.as_pandas
    col_names = list(df.columns)
    prem_idxs = [col_names.index(p) for p in prem_translated]
    conc_idx  = len(col_names) - 1

    invalid_rows  = []
    critical_rows = []
    critical_index = []
    ivalid_index = []

    for _, row in df.iterrows():
        row_vals       = list(row)
        all_prems_true = all(row_vals[i] == True for i in prem_idxs)
        conc_true      = row_vals[conc_idx] == True

        if all_prems_true:
            if conc_true:
                critical_rows.append(row_vals)
                critical_index.append(_)
                print(f"Filas criticas: {critical_rows}")
                print(f"Indice crítico: {_}")
            else:
                invalid_rows.append(row_vals)
                ivalid_index.append(_)
                print(f"Filas invalidas: {invalid_rows}")

    print()
    if invalid_rows:
        print("ARGUMENTO INVALIDO")
        valor = "INVALIDO"
    elif critical_rows:
        print("ARGUMENTO VALIDO")
        valor = "VALIDO"
    else:
        print("las premisas nunca son todas T al mismo tiempo")
        valor = "NO HAY RENGLONES CRÍTICOS"
    
    #debug
    print(f"Indice renglón: {critical_index}")
    print(f"Renglones críticos: {critical_rows}")
    print(f"Tipo de dato df: {type(df)}")
    print(f"Validez: {valor}")

    return valor, df, critical_index, ivalid_index


if __name__ == "__main__":
    generateTruthTable(premises, conclusion)