Hotel = "Suriya Bhavan"
QVada = int(input("No of Vada: "))
QDosa = int(input("No of Dosa: "))
QIdly = int(input("No of Idly: "))
QPoori = int(input("No of Poori: "))
QPongal = int(input("No of Pongal: "))
Vada = 10 * QVada
Dosa = 20 * QDosa
Idly = 10 * QIdly
Poori = 15 * QPoori
Pongal = 25 * QPongal
Total = Vada + Dosa + Idly + Poori + Pongal
print(f"   Hotel {Hotel}\nItem     Qty    Amount \nVada      {QVada}      {Vada}\nDosa      {QDosa}      {Dosa}\nIdly      {QIdly}      {Idly}\nPoori     {QPoori}      {Poori}\nPongal    {QPongal}      {Pongal}\n\nTotal            {Total}")
