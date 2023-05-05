# Finity experimentation

This project comprises of a Python Poetry project called "/data_proc" and a Node.js React App called "/graphing".

The "/data_proc" folder is intended for experimentation with mathematical methods and experimentation with Machine Learning. After each method is well established, it should be deployed to the [fin_tools module](https://github.com/FinityWorks/fin-tools), which is a dependency of [Finity FastAPI backend](https://github.com/FinityWorks/data_client). The "/data_proc" has FastAPI as a dependency itself so it can push data for visualisation on the "/graphing" frontend.

The "/graphing" folder contains a React App purely for convenience - it can be difficult to port Plotly through Python/WSL so this allows us to easliy create and manipulate Plotly visualisations by calling "/data_proc" as if it is a backend via a get request. It can also be used as practise for visualisations on the [Finity React Frontend](https://github.com/FinityWorks/finity-frontend).

## data_proc

```bash
  cd data_proc/
  poetry shell
  poetry install
```

## graphing

```bash
  cd /graphing
  npm start
```

## Authors

- [@NathanDBrowne](https://www.github.com/NathanDBrowne)
