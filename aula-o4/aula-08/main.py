import pandas as pd 
from sklearn.model_selection import train_teat_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# ler arquivo cav pelo pandas
def ler_cav(filre_path);
    return pd.read_cav(file_path)

def treinar(df):
    x = df[{'acidez','densidade','viscosidade','tonalidade'}]
    y = df['tipo_de_vinho']  

    x_train,x_test,y_train,y_test = train_test_split(x,y, test_size=0.2,rondom_state=42)
    
    # Usando Random como exemplo
    model = RandomForestClassifier()
    model.fit(x_train,y_train)

    # Avaliar modelo a sua precisão
    y_pred = model.predict(x_test)
    precisao = accuracy_score(y_test,y_pred)
    print(f"Presao: (precisao * 100:2f)%")

    return model
# Prever o vinho
def praver_vinho(model,acidez,densidade,viscosidade,tonalidade):
    entrada = pd.DataFrame({
        'acidez':[acidez],
        'densidade':[densidade],
        'viscosidade':[viscosidade],
        'tonalidade':[tonalidade]
    })
    predicao = model.predict(entrada)

    return predicao[0],max(probabilidade[0]*100)

# Metodo principal
if __name__ == "__main__":
    # Variavel que armazena nome de arquivo cav
    arquivo = 'vinhos.cav'
    df = ler_cav(arquivo)
    model = treinar(df)

    # Entrada de dados pelo usuario
    acidez = float(input("Valor da acidez: "))
    densidade = float(input("Valor da densidade: "))
    tonalidade = float(input("Valor da tonalidade: "))

    vinho = prever_Vinho(model,acidez,densidade,viscosidade,tonalidade)
    certeza = prever_Vinho(model,acidez,desindade,viscosidade,tornalidade) 