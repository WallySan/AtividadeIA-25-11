import argparse
from pathlib import Path

import joblib
import pandas as pd

MODELO_PATH = Path("models/modelo_penguins.joblib")


def main():
    parser = argparse.ArgumentParser(
        description="Classifica a espécie de um pinguim com o modelo implantado."
    )
    parser.add_argument("--ilha", default="Biscoe", help="Ilha: Biscoe, Dream ou Torgersen")
    parser.add_argument("--comprimento-bico", type=float, default=46.5, help="bill_length_mm")
    parser.add_argument("--altura-bico", type=float, default=14.8, help="bill_depth_mm")
    parser.add_argument("--nadadeira", type=float, default=220.0, help="flipper_length_mm")
    parser.add_argument("--massa", type=float, default=5050.0, help="body_mass_g")
    parser.add_argument("--sexo", default="male", help="male ou female")
    args = parser.parse_args()

    if not MODELO_PATH.exists():
        raise SystemExit("Modelo não encontrado. Execute o notebook primeiro para gerar models/modelo_penguins.joblib")

    novo = pd.DataFrame(
        [
            {
                "island": args.ilha,
                "bill_length_mm": args.comprimento_bico,
                "bill_depth_mm": args.altura_bico,
                "flipper_length_mm": args.nadadeira,
                "body_mass_g": args.massa,
                "sex": args.sexo,
            }
        ]
    )
    novo["proporcao_bico"] = novo["bill_length_mm"] / novo["bill_depth_mm"]

    modelo = joblib.load(MODELO_PATH)
    classe = modelo.predict(novo)[0]
    probabilidades = modelo.predict_proba(novo)[0]
    confianca = probabilidades.max()

    print(f"Espécie prevista: {classe} (confiança: {confianca:.2%})")
    for nome, probabilidade in zip(modelo.classes_, probabilidades):
        print(f"  {nome}: {probabilidade:.4f}")


if __name__ == "__main__":
    main()
