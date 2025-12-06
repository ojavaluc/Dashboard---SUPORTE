import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd

# Exemplo de dados fictícios
data = {
    "atendente": ["Ana", "Carlos", "João", "Ana", "Carlos", "João"],
    "semana": [1, 1, 1, 2, 2, 2],
    "atendimentos": [30, 25, 20, 40, 35, 28]
}

df = pd.DataFrame(data)

# Gráfico de atendimentos por semana
fig_semana = px.bar(df, x="semana", y="atendimentos", color="atendente",
                    barmode="group", title="Atendimentos por Semana")

# Gráfico de atendimentos totais por atendente
fig_total = px.bar(df.groupby("atendente", as_index=False).sum(),
                   x="atendente", y="atendimentos",
                   title="Total de Atendimentos por Atendente")

# Criando app Dash
app = dash.Dash(__name__)

app.layout = html.Div(children=[
    html.H1("Dashboard SAC"),
    dcc.Graph(figure=fig_semana),
    dcc.Graph(figure=fig_total)
])

if __name__ == "__main__":
    app.run_server(debug=True)