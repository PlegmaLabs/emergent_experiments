# emergent_experiments

## Description

Project title: a usEr-driven energy Management systEm foR enerGy Efficiency iN faciliTies (EMERGENT)

This is the open-source repository containing experiments for the EMERGENT project.

## Demand forecasting component
- Emergent demand forecasting experiments.ipynb - Jupyter notebok containing experiments for the generalized demand forecasting component
- kwh_hourly_dataset_stacked.csv - A dataset containing the hourly energy consumption from 370 buildings in CSV format (Original source: https://archive.ics.uci.edu/dataset/321/electricityloaddiagrams20112014, processed version: https://drive.google.com/file/d/1Vb1ojP1GjYlcmpp7Acq6PRu9Od71xTs8/view?usp=sharing)


## Energy efficiency recommendations component
- nyiso_hourly_prices.csv - CSV containing all the historical price data needed for the environment from NYISO (https://www.nyiso.com/energy-market-operational-data)
- SmartHomeGymEnv_v2_deployment.py - The gym environment python file required to train the Reinforcement Learning algorithms
- train_agent_on_environment.ipynb - The notebook that trains the agent in several environments
- test_agent_deployment.ipynb - The notebook that uses already trained agents and tests their performance on a given day
- env_5_pr_5_df_experiments_marwil - A folder that contains checkpoints for all the available environment combinations for the MARWIL algorithm


## License
Open-source distributed under the license AGPLv3.

## Acknowledgement
The EMERGENT project is a bottom-up project that receives funding from the i-NERGY cascading funding project.

For more information please visit the European Union’s Horizon 2020 research and innovation programme's Grant Agreement No 101016508.


<img src="https://i-nergy.eu/sites/default/files/i-nergy_logo-small-removebg-preview.png" width="250"/> <img src="https://matrycs.eu/themes/custom/matrycs/pattern-library/04-components/eu-block/eu_flag.svg" width="100"/>