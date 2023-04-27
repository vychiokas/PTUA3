import csv

from bs4 import BeautifulSoup
import requests

source = requests.get("https://www.telia.lt/prekes/mobilieji-telefonai/samsung").text
soup = BeautifulSoup(source, "html.parser")

blokai = soup.find_all(
    "div",
    class_="mobiles-product-card card card__product card--anim js-product-compare-product",
)

with open("Telia Samsung telefonai.csv", "w", encoding="UTF-8", newline="") as failas:
    csv_writer = csv.writer(failas)
    csv_writer.writerow(["Modelis", "Mėnesio kaina", "Kaina"])

    for blokas in blokai:
        try:
            pavadinimas = blokas.find(
                "a", class_="mobiles-product-card__title js-open-product"
            ).text.strip()
            men_kaina = blokas.find(
                "div", class_="mobiles-product-card__price-marker"
            ).text.strip()
            kaina = blokas.find_all("div", class_="mobiles-product-card__price-marker")[
                1
            ].text.strip()
            print(pavadinimas, men_kaina, kaina)
            csv_writer.writerow([pavadinimas, men_kaina, kaina])
        except:
            pass
