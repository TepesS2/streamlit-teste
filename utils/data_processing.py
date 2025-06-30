import pandas as pd
import numpy as np
from pathlib import Path

def clean_data(df):
    """Limpa e pré-processa o dataset"""
    # Remove duplicatas
    df = df.drop_duplicates()
    
    # Trata valores ausentes
    # Isso será customizado baseado na estrutura real do dataset
    
    return df

def create_age_groups(df, age_col='Age'):
    """Cria grupos etários da coluna de idade"""
    if age_col in df.columns:
        df['age_group'] = pd.cut(
            df[age_col], 
            bins=[0, 18, 30, 45, 60, 100], 
            labels=['<18', '18-30', '31-45', '46-60', '60+'],
            include_lowest=True
        )
    return df

def calculate_smoking_stats(df):
    """Calcula estatísticas relacionadas ao tabagismo"""
    stats = {}
    
    if 'Smoking_Status' in df.columns:
        smoking_counts = df['Smoking_Status'].value_counts()
        total = len(df)
        
        stats['total_participants'] = total
        stats['current_smokers'] = smoking_counts.get('Current', 0)
        stats['former_smokers'] = smoking_counts.get('Former', 0)
        stats['never_smokers'] = smoking_counts.get('Never', 0)
        stats['smoking_rate'] = (stats['current_smokers'] / total) * 100
    
    return stats

def get_data_summary(df):
    """Obtém resumo abrangente dos dados"""
    summary = {
        'total_rows': len(df),
        'total_columns': len(df.columns),
        'missing_values': df.isnull().sum().sum(),
        'duplicate_rows': df.duplicated().sum(),
        'memory_usage': df.memory_usage(deep=True).sum() / 1024**2  # MB
    }
    
    return summary
