# ==========================================
# Scratch Encode / Decode (Python)
# Compatível com o projeto enviado
# ==========================================

COSTUMES = [
    "Blank1","Blank2","Blank3","Blank4","Blank5","Blank6","Blank7","Blank8","Blank9",
    "A","a","B","b","C","c","D","d","E","e","F","f","G","g","H","h","I","i",
    "J","j","K","k","L","l","M","m","N","n","O","o","P","p","Q","q","R","r",
    "S","s","T","t","U","u","V","v","W","w","X","x","Y","y","Z","z",
    "0","1","2","3","4","5","6","7","8","9",
    ".","+","-","?","!"," ",":",";","\"","'",
    ",","<",">","/","@","#","$","%","^","&",
    "*","(",")","_","="
]

# caractere -> número do costume
CHAR_TO_ID = {
    costume: i
    for i, costume in enumerate(COSTUMES, start=1)
    if not costume.startswith("Blank")
}

# número -> caractere
ID_TO_CHAR = {
    i: costume
    for i, costume in enumerate(COSTUMES, start=1)
    if not costume.startswith("Blank")
}


def encode(text: str) -> str:
    """
    Igual ao bloco Encode do Scratch.
    """

    encoded = ""

    for char in text:
        if char not in CHAR_TO_ID:
            raise ValueError(f"Caractere não suportado: {repr(char)}")

        encoded += f"{CHAR_TO_ID[char]:02d}"

    encoded += "00"

    return encoded


def decode(data: str) -> str:
    """
    Igual ao bloco Decode do Scratch.
    """

    if len(data) % 2 != 0:
        raise ValueError("Código inválido.")

    decoded = ""

    for i in range(0, len(data), 2):

        number = int(data[i:i+2])

        if number == 0:
            break

        if number not in ID_TO_CHAR:
            raise ValueError(f"Código inválido: {number}")

        decoded += ID_TO_CHAR[number]

    return decoded

