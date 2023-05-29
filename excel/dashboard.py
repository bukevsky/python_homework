import pandas as pd
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.graph_objects as go

# Чтение данных из Excel-файла
df = pd.read_excel('C:\project\Financial Statistics Dashboard Systems.xlsx')

# Создание интерактивной веб-диаграммы
app = dash.Dash(__name__)

# Определение стилей
chart_style = {'display': 'inline-block', 'width': '45%', 'padding': '10px'}

# Определение компонентов веб-страницы
app.layout = html.Div([
    html.H1('Статистика доходов и операционной прибыли'),
    html.Label('Выберите год:'),
    dcc.Dropdown(
        id='year-dropdown',
        options=[{'label': str(year), 'value': year} for year in df['Year'].unique()],
        value=df['Year'].min()
    ),
    html.Div(
        children=[
            html.Div(
                style=chart_style,
                children=[
                    html.H2('Диаграмма доходов по месяцам'),
                    dcc.Graph(id='stats-graph')
                ]
            ),
            html.Div(
                style=chart_style,
                children=[
                    html.H2('Круговая диаграмма по стратегиям маркетинга'),
                    dcc.Graph(id='pie-chart')
                ]
            ),
            html.Div(
                style=chart_style,
                children=[
                    html.H2('Средний месячный доход по годам'),
                    dcc.Graph(id='avg-monthly-income')
                ]
            )
        ],
        style={'display': 'flex', 'justify-content': 'center'}
    ),
    html.Div(
        style=chart_style,
        children=[
            html.H2('Target Income - количество в году (Таблица)'),
            html.Table(
                id='target-income-table',
                style={'width': '100%'},
                children=[
                    html.Thead(html.Tr([
                        html.Th('Sources'),
                        html.Th('Quantity (% от количества)'),
                        html.Th('Counts')
                    ])),
                    html.Tbody(id='target-income-table-body')
                ]
            )
        ]
    ),
    html.Div(
        style=chart_style,
        children=[
            html.H2('Income - количество в году (Таблица)'),
            html.Table(
                id='income-table',
                style={'width': '100%'},
                children=[
                    html.Thead(html.Tr([
                        html.Th('Sources'),
                        html.Th('Quantity (% от количества)'),
                        html.Th('Counts')
                    ])),
                    html.Tbody(id='income-table-body')
                ]
            )
        ]
    )
])

# Определение функции обновления графика при изменении значения выпадающего списка
@app.callback(
    [Output('stats-graph', 'figure'), Output('pie-chart', 'figure'), Output('avg-monthly-income', 'figure'), Output('target-income-table-body', 'children'), Output('income-table-body', 'children')],
    [Input('year-dropdown', 'value')]
)
def update_graph(selected_year):
    print(f'Selected Year: {selected_year}')

    # Фильтрация данных по выбранному году
    filtered_df = df[df['Year'] == selected_year]

    print(f'Filtered Data:\n{filtered_df}')

    # Создание столбчатой диаграммы доходов по месяцам
    fig = go.Figure()
    fig.add_trace(go.Bar(x=filtered_df['Month'], y=filtered_df['Income'], name='Доходы'))
    fig.update_layout(
        title=f'Доходы и операционная прибыль по месяцам в {selected_year}',
        xaxis_title='Месяц',
        yaxis_title='Доходы'
    )

    # Добавление графика линий операционной прибыли по месяцам
    fig.add_trace(go.Scatter(x=filtered_df['Month'], y=filtered_df['operating profit'], name='Операционная прибыль'))

    # Создание круговой диаграммы по стратегиям маркетинга
    pie_data = filtered_df['Marketing Strategies'].value_counts()
    pie_labels = pie_data.index.tolist()
    pie_values = pie_data.values.tolist()

    pie_fig = go.Figure(data=[go.Pie(labels=pie_labels, values=pie_values)])
    pie_fig.update_layout(title=f'Стратегии маркетинга в {selected_year}')

    # Вычисление среднего месячного дохода по годам
    avg_monthly_df = df.groupby('Year')['Income'].mean().reset_index()
    avg_monthly_fig = go.Figure()
    avg_monthly_fig.add_trace(go.Bar(x=avg_monthly_df['Year'], y=avg_monthly_df['Income'], name='Средний доход'))
    avg_monthly_fig.update_layout(
        title='Средний месячный доход по годам',
        xaxis_title='Год',
        yaxis_title='Средний доход'
    )

    # Создание таблицы Target Income - количество в году
    target_income_df = filtered_df.groupby('Income sources')['Counts'].sum().reset_index()
    target_income_table_body = []
    total_counts = target_income_df['Counts'].sum()
    target_income_df['Quantity'] = (target_income_df['Counts'] / total_counts) * 100
    target_income_df = target_income_df.sort_values('Quantity', ascending=False)
    for i in range(len(target_income_df)):
        target_income_table_body.append(
            html.Tr([
                html.Td(target_income_df.iloc[i]['Income sources']),
                html.Td(f'{target_income_df.iloc[i]["Quantity"]:.2f}%'),
                html.Td(target_income_df.iloc[i]['Counts'])
            ])
        )

    # Создание таблицы Income - количество в году
    income_df = filtered_df.groupby('Income sources')['Income'].sum().reset_index()
    income_table_body = []
    total_counts = income_df['Income'].sum()
    income_df['Quantity'] = (income_df['Income'] / total_counts) * 100
    income_df = income_df.sort_values('Quantity', ascending=False)
    for i in range(len(income_df)):
        income_table_body.append(
            html.Tr([
                html.Td(income_df.iloc[i]['Income sources']),
                html.Td(f'{income_df.iloc[i]["Quantity"]:.2f}%'),
                html.Td(income_df.iloc[i]['Income'])
            ])
        )

    return fig, pie_fig, avg_monthly_fig, target_income_table_body, income_table_body

# Запуск веб-приложения
if __name__ == '__main__':
    app.run_server(debug=True)
