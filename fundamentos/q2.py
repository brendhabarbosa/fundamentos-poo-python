def analyze_text(text):
    vogals = "aeiouAEIOU"
    cont = 0
    invert = text[::-1]
    for letra in text:
        if letra in vogals:
            cont += 1
    if text == invert:
        print(f"A palavra {text} é um palíndromo")

    return cont, invert

print(analyze_text("arara"))
print(analyze_text("luisa"))