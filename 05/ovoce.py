barvy_ovoce = {
    "hruska" : "zelena",
    "jablko" : "cervena"
}

barvy_ovoce_po_tyzdnu = dict(barvy_ovoce)

for barva in barvy_ovoce_po_tyzdnu:
    barvy_ovoce_po_tyzdnu[barva] = "hnedo-" + barvy_ovoce_po_tyzdnu[barva]

print(barvy_ovoce)
print(barvy_ovoce_po_tyzdnu)