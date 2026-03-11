import truth_table_generator as ttg
import pandas as pd

tabla = ttg.Truths(
    ['p', 'q', 'r', 's'],
    [
        'p or q',        
        'r or s',        
        '(p or q) and (r or s)'  
    ]
)

df = tabla.as_pandas

criticos = df[
    (df['p or q'] == True) &
    (df['r or s'] == True) &
    (df['(p or q) and (r or s)'] == True)
]

invalido = df[
    (df['p or q'] == True) &
    (df['r or s'] == True) &
    (df['(p or q) and (r or s)'] == False)
]

if invalido.empty:
    print("\nRenglones críticos:")
    print(criticos)
else:
    print("\nArgumento Invalido")
    print(invalido)



print('='*20)
print("TABLA INVALIDA")
print('='*20)

tabla_invalida = ttg.Truths(['p', 'q'], ['p or q', 'p and q'])
df = tabla_invalida.as_pandas

criticos = df[
    (df['p or q'] == True) &
    (df['p and q'] == True) 
]

invalido = df[
    (df['p or q'] == True) &
    (df['p and q'] == False) 
]

if invalido.empty:
    print("\nRenglones críticos:")
    print(criticos)
else:
    print("\nArgumento Invalido")
    print(invalido)






