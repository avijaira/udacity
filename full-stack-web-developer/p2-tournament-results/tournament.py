#!/usr/bin/env python
#
# tournament.py -- implementation of a Swiss-system tournament


import psycopg2


"""
from math import log2
def isPowerOfTwo(num):
    power = int(log2(num) + 0.5)
    return 2**power == num
"""


def connect():
    """Connect to the PostgreSQL database.

    Returns a database connection and a cursor.
    """
    try:
        db = psycopg2.connect(
            'host=localhost dbname=tournament user=postgres password=password')
        cursor = db.cursor()
        return db, cursor
    except ValueError:
        print("Unable to connect to the database.")


def deleteMatches():
    """Remove all the match records from the database."""
    db, cursor = connect()
    sql = '''DELETE FROM games;'''
    cursor.execute(sql)
    db.commit()
    db.close()


def deletePlayers():
    """Remove all the player records from the database."""
    db, cursor = connect()
    sql = '''DELETE FROM players;'''
    cursor.execute(sql)
    db.commit()
    db.close()


def countPlayers():
    """Returns the number of players currently registered."""
    db, cursor = connect()
    sql = '''SELECT COUNT(*) FROM players;'''
    cursor.execute(sql)
    result = cursor.fetchone()
    db.close()
    return result[0]


def registerPlayer(name):
    """Adds a player to the tournament database.

    The database assigns a unique serial id number for the player.

    Args:
      name: the player's full name (need not be unique).
    """
    db, cursor = connect()
    """NOTE 1: The variables placeholder must always be a %s.
    """
    sql = '''INSERT INTO players(name) VALUES(%s);'''
    """NOTE 2: For positional variables binding, the second argument must
    always be a sequence, even if it contains a single variable (a tuple or
    a list).
    """
    cursor.execute(sql, (name,))
    db.commit()
    db.close()


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    db, cursor = connect()
    sql = '''INSERT INTO games(winner, loser) VALUES(%s, %s);'''
    cursor.execute(sql, (winner, loser))
    db.commit()
    db.close()


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a
    player tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    db, cursor = connect()
    sql = '''SELECT * FROM playerStandings;'''
    cursor.execute(sql)
    results = cursor.fetchall()
    db.close()
    return results


def swissPairings():
    """Returns a list of pairs of players for the next round of a match.

    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.

    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    results = []
    if (countPlayers() % 2 == 0):
        db, cursor = connect()
        sql = '''SELECT * FROM playerStandings;'''
        cursor.execute(sql)
        """Fetchall() returns a list of dictionaries (a dictionary per row),
        convert it in to a list of tuples (id1, name1, id2, name2)
        """
        r = cursor.fetchall()
        db.close()
        for d in range(0, len(r), 2):
            t = (r[d][0], r[d][1], r[d+1][0], r[d+1][1])
            results.append(t)
    else:
        raise ValueError("Num of players registered should be power of two.")
    return results
