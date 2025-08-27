import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def setup_plot_style():
    sns.set_theme(style="whitegrid")

def plot_turnout_abstention_by_gender(df):
    setup_plot_style()
    plt.figure(figsize=(12, 6))
    summary_data = df.groupby('DS_GENERO')[['QT_COMPARECIMENTO', 'QT_ABSTENCAO']].sum().reset_index()
    melted_data = summary_data.melt(id_vars='DS_GENERO', value_vars=['QT_COMPARECIMENTO', 'QT_ABSTENCAO'],
                                  var_name='Status', value_name='Count')
    sns.barplot(data=melted_data, x='DS_GENERO', y='Count', hue='Status')
    plt.title('Voter Turnout and Abstention by Gender')
    plt.xlabel('Gender')
    plt.ylabel('Count')
    plt.legend(title='Status')
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.show()

def plot_turnout_abstention_by_age_group(df):
    setup_plot_style()
    plt.figure(figsize=(12, 6))
    age_summary = df.groupby('DS_FAIXA_ETARIA')[['QT_COMPARECIMENTO', 'QT_ABSTENCAO']].sum().reset_index()
    age_melted_data = age_summary.melt(id_vars='DS_FAIXA_ETARIA', value_vars=['QT_COMPARECIMENTO', 'QT_ABSTENCAO'],
                                     var_name='Status', value_name='Count')
    sns.barplot(data=age_melted_data, x='DS_FAIXA_ETARIA', y='Count', hue='Status')
    plt.title('Voter Turnout and Abstention by Age Group')
    plt.xlabel('Age Group')
    plt.ylabel('Count')
    plt.legend(title='Status')
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.show()

def plot_turnout_abstention_by_educational_level(df):
    setup_plot_style()
    plt.figure(figsize=(12, 6))
    education_summary = df.groupby('DS_GRAU_ESCOLARIDADE')[['QT_COMPARECIMENTO', 'QT_ABSTENCAO']].sum().reset_index()
    education_melted_data = education_summary.melt(id_vars='DS_GRAU_ESCOLARIDADE', value_vars=['QT_COMPARECIMENTO', 'QT_ABSTENCAO'],
                                               var_name='Status', value_name='Count')
    sns.barplot(data=education_melted_data, x='DS_GRAU_ESCOLARIDADE', y='Count', hue='Status')
    plt.title('Voter Turnout and Abstention by Educational Level')
    plt.xlabel('Educational Level')
    plt.ylabel('Count')
    plt.legend(title='Status')
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.show()

def plot_comparecimento_faixa_etaria_pct(df):
    setup_plot_style()
    plt.figure(figsize=(12, 6))
    sns.barplot(data=df, x='DS_FAIXA_ETARIA', y='PCT_COMPARECIMENTO', palette='Blues', edgecolor=None)
    plt.xticks(rotation=90)
    plt.title('Comparecimento por Faixa Etária (%)')
    plt.xlabel('Faixa Etária')
    plt.ylabel('Percentual de Comparecimento')
    plt.show()

def plot_abstencao_grau_escolaridade_pct(df):
    setup_plot_style()
    plt.figure(figsize=(12, 6))
    sns.barplot(data=df, x='DS_GRAU_ESCOLARIDADE', y='PCT_ABSTENCAO', palette='Reds', edgecolor=None)
    plt.xticks(rotation=90)
    plt.title('Abstenção por Grau de Escolaridade (%)')
    plt.xlabel('Grau de Escolaridade')
    plt.ylabel('Percentual de Abstenção')
    plt.show()

def plot_comparecimento_genero_pct(df):
    setup_plot_style()
    plt.figure(figsize=(8, 6))
    sns.barplot(data=df, x='DS_GENERO', y='PCT_COMPARECIMENTO', palette='Greens', edgecolor=None)
    plt.title('Comparecimento por Gênero (%)')
    plt.xlabel('Gênero')
    plt.ylabel('Percentual de Comparecimento')
    plt.show()

def plot_distribuicao_comparecimento_pct(df):
    setup_plot_style()
    plt.figure(figsize=(10, 5))
    sns.histplot(df['PCT_COMPARECIMENTO'], bins=20, kde=True, color='blue')
    plt.title('Distribuição do Percentual de Comparecimento')
    plt.xlabel('Percentual de Comparecimento')
    plt.ylabel('Frequência')
    plt.show()

def plot_comparecimento_vs_abstencao_faixa_etaria(df):
    setup_plot_style()
    plt.figure(figsize=(12, 6))
    df_melted = df.melt(id_vars=['DS_FAIXA_ETARIA'], value_vars=['PCT_COMPARECIMENTO', 'PCT_ABSTENCAO'],
                        var_name='Categoria', value_name='Percentual')
    sns.barplot(data=df_melted, x='DS_FAIXA_ETARIA', y='Percentual', hue='Categoria', palette=['blue', 'red'], edgecolor=None)
    plt.xticks(rotation=45)
    plt.title('Comparecimento vs. Abstenção por Faixa Etária (%)')
    plt.xlabel('Faixa Etária')
    plt.ylabel('Percentual')
    handles, labels = plt.gca().get_legend_handles_labels()
    plt.legend(handles, ['Comparecimento', 'Abstenção'], title='Categoria')
    plt.show()

def plot_comparecimento_vs_abstencao_grau_escolaridade(df):
    setup_plot_style()
    plt.figure(figsize=(12, 6))
    df_melted = df.melt(id_vars=['DS_GRAU_ESCOLARIDADE'], value_vars=['PCT_COMPARECIMENTO', 'PCT_ABSTENCAO'],
                        var_name='Categoria', value_name='Percentual')
    sns.barplot(data=df_melted, x='DS_GRAU_ESCOLARIDADE', y='Percentual', hue='Categoria', palette=['blue', 'red'], edgecolor=None)
    plt.xticks(rotation=90)
    plt.title('Comparecimento vs. Abstenção por Grau de Escolaridade (%)')
    plt.xlabel('Grau de Escolaridade')
    plt.ylabel('Percentual')
    handles, labels = plt.gca().get_legend_handles_labels()
    plt.legend(handles, ['Comparecimento', 'Abstenção'], title='Categoria')
    plt.show()

def plot_comparecimento_vs_abstencao_cidade(df):
    setup_plot_style()
    top_cidades = df.groupby('NM_MUNICIPIO')['QT_APTOS'].sum().nlargest(10).index
    df_top_cidades = df[df['NM_MUNICIPIO'].isin(top_cidades)]
    df_top_cidades_sorted = df_top_cidades.groupby('NM_MUNICIPIO').agg({
        'PCT_COMPARECIMENTO': 'mean',
        'PCT_ABSTENCAO': 'mean'
    }).sort_values(by='PCT_COMPARECIMENTO', ascending=False).reset_index()
    df_melted = df_top_cidades_sorted.melt(id_vars=['NM_MUNICIPIO'], value_vars=['PCT_COMPARECIMENTO', 'PCT_ABSTENCAO'],
                                       var_name='Categoria', value_name='Percentual')
    plt.figure(figsize=(14, 7))
    sns.barplot(data=df_melted, x='NM_MUNICIPIO', y='Percentual', hue='Categoria', palette=['blue', 'red'], edgecolor=None)
    plt.xticks(rotation=90)
    plt.title('Comparecimento vs. Abstenção por Cidade (%)')
    plt.xlabel('Cidade')
    plt.ylabel('Percentual')
    handles, labels = plt.gca().get_legend_handles_labels()
    plt.legend(handles, ['Comparecimento', 'Abstenção'], title='Categoria')
    plt.show()

def plot_comparecimento_vs_abstencao_deficiencia(df):
    setup_plot_style()
    top_15_cidades = df.groupby('NM_MUNICIPIO')['QT_APTOS'].sum().nlargest(15).index
    df_top_15_cidades = df[df['NM_MUNICIPIO'].isin(top_15_cidades)]
    df_top_15_cidades_sorted = df_top_15_cidades.sort_values(by='PCT_COMPARECIMENTO_DEFICIENCIA', ascending=False)
    plt.figure(figsize=(14, 7))
    df_melted = df_top_15_cidades_sorted.melt(id_vars=['NM_MUNICIPIO'], value_vars=['PCT_COMPARECIMENTO_DEFICIENCIA', 'PCT_ABSTENCAO_DEFICIENCIA'],
                                           var_name='Categoria', value_name='Percentual')
    sns.barplot(data=df_melted, x='NM_MUNICIPIO', y='Percentual', hue='Categoria',
                palette={'PCT_COMPARECIMENTO_DEFICIENCIA': 'blue', 'PCT_ABSTENCAO_DEFICIENCIA': 'red'}, edgecolor=None)
    plt.xticks(rotation=90)
    plt.title('Comparecimento vs. Abstenção de Pessoas com Deficiência em 15 Cidades de Alagoas (%)')
    plt.xlabel('Município')
    plt.ylabel('Percentual (%)')
    handles, labels = plt.gca().get_legend_handles_labels()
    plt.legend(handles, ['Comparecimento', 'Abstenção'], title='Categoria')
    plt.show()

def plot_faixa_etaria_maior_comparecimento(df):
    setup_plot_style()
    df_comparecimento = df[df['QT_COMPARECIMENTO'] > 0]
    plt.figure(figsize=(12, 6))
    sns.countplot(data=df_comparecimento, x='DS_FAIXA_ETARIA', order=df_comparecimento['DS_FAIXA_ETARIA'].value_counts().index, palette='viridis')
    plt.xticks(rotation=45)
    plt.title('Faixa Etária com Maior Comparecimento')
    plt.xlabel('Faixa Etária')
    plt.ylabel('Número de Pessoas')
    plt.show()

def plot_distribuicao_percentual_comparecimento_faixa_etaria(df):
    setup_plot_style()
    df_faixa_etaria = df.groupby('DS_FAIXA_ETARIA')['QT_COMPARECIMENTO'].sum().reset_index()
    df_faixa_etaria['Percentual'] = (df_faixa_etaria['QT_COMPARECIMENTO'] / df_faixa_etaria['QT_COMPARECIMENTO'].sum()) * 100
    plt.figure(figsize=(12, 6))
    sns.barplot(data=df_faixa_etaria, x='DS_FAIXA_ETARIA', y='Percentual', palette='viridis', order=df_faixa_etaria.sort_values('Percentual', ascending=False)['DS_FAIXA_ETARIA'])
    plt.xticks(rotation=45)
    plt.title('Distribuição Percentual do Comparecimento por Faixa Etária')
    plt.xlabel('Faixa Etária')
    plt.ylabel('Percentual de Comparecimento (%)')
    plt.show()

def plot_tte_comparecimento_abstencao_uf(df):
    setup_plot_style()
    fig, axes = plt.subplots(3, 1, figsize=(12, 18))
    df_grouped_uf = df.groupby("SG_UF_ORIGEM")[["QT_COMPARECIMENTO_TTE", "QT_ABSTENCAO_TTE"]].sum().reset_index()
    df_grouped_uf = df_grouped_uf.sort_values(by="QT_COMPARECIMENTO_TTE", ascending=False)
    sns.barplot(data=df_grouped_uf.melt(id_vars="SG_UF_ORIGEM", value_vars=["QT_COMPARECIMENTO_TTE", "QT_ABSTENCAO_TTE"]),
                x="SG_UF_ORIGEM", y="value", hue="variable", palette=["#4CAF50", "#F44336"], ax=axes[0])
    axes[0].set_title("Distribuição do Comparecimento e Abstenção por Estado", fontsize=14)
    axes[0].set_xlabel("Estado (UF)")
    axes[0].set_ylabel("Quantidade de Eleitores")

def plot_tte_comparecimento_abstencao_faixa_etaria(df):
    setup_plot_style()
    fig, axes = plt.subplots(3, 1, figsize=(12, 18))
    df_grouped_etaria = df.groupby("DS_FAIXA_ETARIA")[["QT_COMPARECIMENTO_TTE", "QT_ABSTENCAO_TTE"]].sum().reset_index()
    df_grouped_etaria = df_grouped_etaria.sort_values(by="QT_COMPARECIMENTO_TTE", ascending=False)
    sns.barplot(data=df_grouped_etaria.melt(id_vars="DS_FAIXA_ETARIA", value_vars=["QT_COMPARECIMENTO_TTE", "QT_ABSTENCAO_TTE"]),
                x="DS_FAIXA_ETARIA", y="value", hue="variable", palette=["#2196F3", "#FF9800"], ax=axes[1])
    axes[1].set_title("Proporção de Comparecimento e Abstenção por Faixa Etária", fontsize=14)
    axes[1].set_xlabel("Faixa Etária")
    axes[1].set_ylabel("Quantidade de Eleitores")
    axes[1].set_xticklabels(axes[1].get_xticklabels(), rotation=45)

def plot_tte_comparecimento_tipo_transferencia(df):
    setup_plot_style()
    fig, axes = plt.subplots(3, 1, figsize=(12, 18))
    df_grouped_tte = df.groupby("DS_TIPO_TRANSFERENCIA")[[ "QT_COMPARECIMENTO_TTE", "QT_ABSTENCAO_TTE"]].sum().reset_index()
    df_grouped_tte = df_grouped_tte.sort_values(by="QT_COMPARECIMENTO_TTE", ascending=False)
    sns.barplot(data=df_grouped_tte.melt(id_vars="DS_TIPO_TRANSFERENCIA", value_vars=["QT_COMPARECIMENTO_TTE", "QT_ABSTENCAO_TTE"]),
                y="DS_TIPO_TRANSFERENCIA", x="value", hue="variable", palette=["#9C27B0", "#FF5722"], ax=axes[2])
    axes[2].set_title("Comparecimento por Tipo de Transferência Temporária", fontsize=14)
    axes[2].set_xlabel("Quantidade de Eleitores")
    axes[2].set_ylabel("Tipo de Transferência")
    plt.tight_layout()
    plt.show()
