import pandas as pd
import matplotlib.pyplot as plt

data = {
"genre": [
    "Pop","Rock","Hip-Hop","Electronic","Pop","Rock","Hip-Hop","Electronic",
    "Pop","Rock","Hip-Hop","Electronic","Pop","Rock","Hip-Hop","Electronic",
    "Pop","Rock","Hip-Hop","Electronic"
],
"streams": [
    120,90,150,70,130,95,140,80,
    110,85,155,75,125,100,145,78,
    118,92,160,82
],
"likes": [
    30,20,50,15,35,22,48,18,
    28,19,55,16,32,25,47,17,
    29,21,60,19
],
"shares": [
    10,8,20,5,12,9,18,6,
    9,7,22,5,11,10,19,6,
    10,8,25,7
],
"year": [
    2020,2020,2020,2020,2021,2021,2021,2021,
    2022,2022,2022,2022,2023,2023,2023,2023,
    2024,2024,2024,2024
]
}

df = pd.DataFrame(data)