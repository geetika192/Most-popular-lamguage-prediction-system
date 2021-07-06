import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
class languageratings():
    def showchart(self):
        languageratings=pd.read_excel("language_rating.xlsx",sheet_name="rating")
        print(languageratings)
        plt.xlabel("language")
        plt.ylabel("ratings")
        plt.title("language_ratings")
        plt.bar(languageratings["language"],languageratings["rating"])
        plt.show()
def main():
    p=languageratings()
    p.showchart()

if __name__ == '__main__':main()
