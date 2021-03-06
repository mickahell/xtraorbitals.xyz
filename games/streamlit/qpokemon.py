import streamlit as st
import pandas as pd
import datetime
import io
import requests
import plotly.graph_objects as go


def info():
    page_name = "qpokemon"
    return page_name


def app():
    st.write("# Quantum Pokémon fight")

    rules = st.expander("Rules", expanded=False)
    rules_view = """
    A Pokémon fight is a turn by turn game, each opponent as a team of 3 Pokémons and the last who still have Pokémon in shape win the game !  
    At each turn the fastest Pokémon attack first, if the speed stats are the same the choice will be random.  
    Each fire, electric, ice and poison attack can inflicted (almost) permanent damages and stats alteration :
    
    |   Type   |          Effect          |    Stats    |
    |:--------:|:------------------------:|:-----------:|
    | Fire     | Permanent damages        | drop attack |
    | Ice      | Can't attack             |             |
    | Electric | Can not attack sometimes | drop speed  |
    | Poison   | Permanent damages        |             |
        """
    rules.write(rules_view, unsafe_allow_html=True)

    article = st.expander("How does it works ?", expanded=False)
    article_view = """
        <iframe
            title="Quantum Pokémon Fight article"
            width="100%"
            height="720"
            src="https://fullstackquantumcomputation.tech/blog/post-quantum-pokemon-fight/">
        </iframe>
        """
    article.write(article_view, unsafe_allow_html=True)

    qpokemon = st.expander("Game", expanded=True)
    qpokemon_view = """
    <iframe
        title="Quantum Pokémon Fight"
        width="100%"
        height="510"
        src="https://qpokemon-fight.xtraorbitals.xyz">
    </iframe>
    """
    qpokemon.write(qpokemon_view, unsafe_allow_html=True)
    st.write("<h3>See on <a href='https://qpokemon-fight.xtraorbitals.xyz'><b>QPokémon game page</b></a></h3>", unsafe_allow_html=True)
    badge = """
        [![GitHub release (latest by date)](https://img.shields.io/github/v/release/mickahell/quantum_pokemon-fight)](https://github.com/mickahell/quantum_pokemon-fight/releases)
        """
    st.markdown(badge)

    #############################################################
    # Graph
    r = requests.get('https://raw.githubusercontent.com/mickahell/robots-data/main/games/stats/qpokemon_results.csv')
    file_csv = io.StringIO(r.text)

    robot_evo_csv = []
    human_evo_csv = []
    date_csv = []

    csv_file = pd.read_csv(filepath_or_buffer=file_csv)
    
    robot_csv = csv_file["robot"].tolist()
    human_csv = csv_file["human"].tolist()
    date_csv_temp = csv_file["date"].tolist()

    for i in range(len(date_csv_temp)):
        date_csv.append(datetime.datetime.strptime(date_csv_temp[i], '%m-%Y').date())

    for i in range(len(robot_csv)):
        robot_evo_csv.append(robot_csv[i] / (human_csv[i] + robot_csv[i]) * 100)
        human_evo_csv.append(human_csv[i] / (human_csv[i] + robot_csv[i]) * 100)

    left_column, right_column = st.columns(2)

    fig_bar = go.Figure([go.Bar(x=['Robot', 'Human'], y=[sum(robot_csv), sum(human_csv)])])
    fig_bar.update_layout(title_text='Robot VS Human')
    left_column.plotly_chart(fig_bar, use_container_width=True)

    fig_series = go.Figure([go.Scatter(x=date_csv, y=robot_evo_csv, mode='lines+markers', marker=dict(color="aqua"))])
    fig_series.update_layout(title_text='Robot evolution', xaxis_title="Months", yaxis_title="% of victory")
    right_column.plotly_chart(fig_series, use_container_width=True)
