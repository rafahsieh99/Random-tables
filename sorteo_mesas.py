import pandas as pd
import random
import math

def asignar_mesas_csv(
    ruta_csv,
    miembros_por_mesa=4,
    salida_excel="mesas.xlsx"
):
    # 1) Lee el CSV (saltando la primera fila vacía)
    df = pd.read_csv(ruta_csv, header=1)

    # 2) Detecta columna de nombres
    col_nombres = next(
        (c for c in df.columns if 'nombre' in c.lower()), 
        None
    )
    if col_nombres is None:
        raise KeyError("No se encontró ninguna columna que contenga 'nombre'")

    # 3) Detecta columna de estado “Activo”
    col_estado = next(
        (c for c in df.columns 
        if df[c].astype(str).str.strip().str.lower().eq('activo').any()),
        None
    )
    if col_estado is None:
        raise KeyError("No se encontró ninguna columna con valores 'Activo'")

    # 4) Filtra solo alumnos activos
    df_activos = df[df[col_estado].str.strip().str.lower() == 'activo']

    # 5) Extrae y baraja la lista de nombres
    nombres = df_activos[col_nombres].dropna().tolist()
    random.shuffle(nombres)

    # 6) Calcula número de mesas y distribuye de forma balanceada
    total = len(nombres)
    num_mesas = math.ceil(total / miembros_por_mesa)
    base = total // num_mesas
    extra = total % num_mesas

    # Las primeras 'extra' mesas tendrán tamaño (base+1), el resto tamaño 'base'
    tamaños = [base + 1] * extra + [base] * (num_mesas - extra)

    # 7) Agrupa según esos tamaños
    mesas = []
    idx = 0
    for tam in tamaños:
        mesa = nombres[idx: idx + tam]
        mesas.append(mesa)
        idx += tam

    # 8) Construye filas para el Excel (una sola columna)
    filas = []
    for i, mesa in enumerate(mesas, start=1):
        filas.append(f"Mesa {i} ({len(mesa)} miembros):")
        for alumno in mesa:
            filas.append(f"- {alumno}")
        filas.append("")  # línea en blanco

    df_output = pd.DataFrame({"Mesas": filas})

    # 9) Exporta todo a una sola hoja de Excel
    with pd.ExcelWriter(salida_excel, engine="openpyxl") as writer:
        df_output.to_excel(writer, sheet_name="Mesas", index=False)

    print(f"✅ Se ha generado el Excel: {salida_excel}  "
        f"({num_mesas} mesas: {extra} de {base+1} y "
        f"{num_mesas-extra} de {base} integrantes)")

if __name__ == "__main__":
    asignar_mesas_csv("alumnos.csv")
