
-- tournament:
DROP DATABASE IF EXISTS tournament;
CREATE DATABASE tournament;

-- Connect to database 'tournament'
\c tournament

-- players:
--    id (unique),
--    name (full name of a player)
CREATE TABLE IF NOT EXISTS players (
  id SERIAL UNIQUE PRIMARY KEY,
  name VARCHAR(128)
);

-- games:
--    id (unique),
--    winner (an id of the player who won the game),
--    loser (an id of the player who lost the game)
CREATE TABLE IF NOT EXISTS games (
  id SERIAL UNIQUE PRIMARY KEY,
  winner INTEGER REFERENCES players(id),
  loser INTEGER REFERENCES players(id),
  CHECK (winner <> loser)
);

-- playerStandings:
-- Returns player standings even when no matches have been played.
CREATE OR REPLACE VIEW matchesplayed AS
  SELECT p.id AS ID, COUNT(*) AS Matches
  FROM players p, games g
  WHERE p.id = g.winner OR p.id = g.loser
  GROUP BY p.id;

CREATE OR REPLACE VIEW matcheswon AS
  SELECT p.id AS ID, COUNT(*) AS Wins
  FROM players p, games g
  WHERE p.id = g.winner
  GROUP BY p.id;

CREATE OR REPLACE VIEW playerstandings AS
SELECT p.id AS ID, p.name as Name, COALESCE(w.Wins, 0) AS Wins, COALESCE(m.Matches, 0) AS Matches
  FROM players p
  LEFT JOIN matcheswon w
  ON p.id = w.ID
  LEFT JOIN matchesplayed m
  ON p.id = m.ID
  ORDER BY Wins DESC, Matches ASC, ID ASC;
