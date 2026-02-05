

database = 'database (2).sqlite'

import pandas as pd

import numpy as np

import sqlite3 

conn = sqlite3.connect(database)



match_details = pd.read_sql("""SELECT Match_Id, Season_Id,
                            v.Venue_Name,c.City_Name,t.Team_Name AS Winner
                            FROM Match
                            INNER JOIN Venue AS v ON Match.Venue_Id == v.Venue_Id
                            INNER JOIN City AS c ON v.City_Id == c.City_Id
                            INNER JOIN Team AS t ON Match.Match_Winner == t.Team_Id;""",conn)

match_details


csk_matches_2015 = pd.read_sql("""SELECT Match_Id,Team_2 AS Away_Team,Toss_Winner,Match_Winner
                               FROM Match
                               WHERE Team_1 =
                               (SELECT Team_1
                               WHERE Team_1 == 3 AND Season_Id == 8);""",conn)
print("Matches Played by Chennai Super Kings in 2015")
csk_matches_2015

csk_wins = pd.read_sql("""SELECT*
                       FROM Match
                       WHERE Match_Winner == 3 AND Season_Id == 8;""",conn)
print("Matches Won by CSK as Home Team in Year 2015")
csk_wins

match_runs = pd.read_sql("""SELECT Match_Id ,Runs_Scored AS Total_Runs , Innings_No
                        FROM Batsman_Scored
                        WHERE Total_Runs > 5 AND Match_Id IN
                        (SELECT Match_Id
                         FROM Match
                         WHERE Season_Id == 8);""",conn)
print("Matches with scored runs grater than 5 in year 2015")
match_runs

average_runs = pd.read_sql("""SELECT Match_Id ,Runs_Scored AS Total_Runs , Innings_No
                        FROM Batsman_Scored
                        WHERE Innings_No == 1 AND Runs_Scored >
                        (SELECT AVG(Runs_Scored)
                        FROM Batsman_Scored);""",conn)
print("Matches with Scored Run Grater than Average Scored Run")
average_runs

