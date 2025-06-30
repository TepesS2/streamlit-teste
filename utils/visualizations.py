import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd

def create_smoking_pie_chart(df, title="Distribuição do Status de Tabagismo"):
    """Cria um gráfico de pizza para distribuição do status de tabagismo"""
    if 'Smoking_Status' not in df.columns:
        return None
    
    fig = px.pie(
        df, 
        names='Smoking_Status',
        title=title,
        color_discrete_sequence=px.colors.qualitative.Set3
    )
    fig.update_traces(textposition='inside', textinfo='percent+label')
    return fig

def create_age_histogram(df, title="Distribuição de Idade"):
    """Cria histograma para distribuição de idade"""
    if 'Age' not in df.columns:
        return None
    
    fig = px.histogram(
        df,
        x='Age',
        nbins=20,
        title=title,
        color_discrete_sequence=['#1f77b4']
    )
    fig.update_layout(xaxis_title="Idade", yaxis_title="Contagem")
    return fig

def create_correlation_heatmap(df, title="Matriz de Correlação"):
    """Cria mapa de calor de correlação para variáveis numéricas"""
    numeric_cols = df.select_dtypes(include=['number']).columns
    
    if len(numeric_cols) < 2:
        return None
    
    correlation_matrix = df[numeric_cols].corr()
    
    fig = px.imshow(
        correlation_matrix,
        title=title,
        color_continuous_scale='RdBu_r',
        aspect="auto"
    )
    return fig

def create_grouped_bar_chart(df, x_col, color_col, title="Gráfico de Barras Agrupadas"):
    """Cria gráfico de barras agrupadas"""
    if x_col not in df.columns or color_col not in df.columns:
        return None
    
    crosstab = pd.crosstab(df[x_col], df[color_col])
    
    fig = px.bar(
        crosstab.reset_index(),
        x=x_col,
        y=crosstab.columns.tolist(),
        title=title,
        barmode='group'
    )
    return fig

def create_box_plot(df, x_col, y_col, title="Gráfico de Caixa"):
    """Cria gráfico de caixa para comparar distribuições"""
    if x_col not in df.columns or y_col not in df.columns:
        return None
    
    fig = px.box(
        df,
        x=x_col,
        y=y_col,
        title=title
    )
    return fig
