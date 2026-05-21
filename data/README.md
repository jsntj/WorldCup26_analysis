# Historical World Cup dataset notes

`historical_world_cup_performance.csv` is a compact starter dataset for initial model experimentation.

## Columns

- `year`: World Cup year.
- `team`: National team name.
- `fifa_rank`: Approximate FIFA ranking entering the tournament.
- `recent_win_rate`: Approximate pre-tournament win rate (0 to 1) from recent international matches.
- `avg_goals`: Approximate average goals scored per match before the tournament.
- `won_world_cup`: Target label (1 if champion, 0 otherwise).

Values are intentionally lightweight to bootstrap the analysis pipeline and can be replaced with richer sourced data in later iterations.
