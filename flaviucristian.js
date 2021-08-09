var quotes = [
    "Toţi se plâng de lipsă de bani, dar de lipsă de minte, nimeni. (Proverb evreiesc)",
    "Nu întoarceţi nimănui rău pentru rău. Urmăriţi ce este bine, înaintea tuturor oamenilor. (Romani 12:17)",
    "Păzeşte-te de o capră – din faţă, de un cal -din spate, de un prost – din toate părţile. (Proverb evreiesc)",
    "Mi-a părut rău de mine însumi fiindcă nu aveam pantofi – până când am întâlnit un om care nu avea picioare. (Proverb evreiesc)",
    "Mîndria merge înaintea pieirii, şi trufia merge înainte căderii. Proverbe 16:18",
    "Nu întoarceţi nimănui rău pentru rău. Urmăriţi ce este bine, înaintea tuturor oamenilor. (Romani 12:17)",
];

function randomQuotes() {
    var idx = Math.floor(Math.random() * quotes.length);
    document.getElementById("quote").innerHTML = quotes[idx];
}