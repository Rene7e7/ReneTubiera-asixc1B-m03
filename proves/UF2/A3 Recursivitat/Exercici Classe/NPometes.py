
applesCount = 5
def getAppleSongStanza(applesCount):
    if applesCount == 0:
        POMA="pometa"
    else:
        POMA="pometes"
    stanza = f"{applesCount} pometes té el pomer,\n" \
 \
             f"de {applesCount} una, de {applesCount} una,\n" \
 \
             f"{applesCount} pometes té el pomer,\n" \
 \
             f"de {applesCount} una en caigué.\n" \
 \
             f"Si mireu el vent d'on vé\n" \
 \
             f"veureu el pomer com dansa,\n" \
 \
             f"si mireu el vent d'on vé\n" \ 
 \
             f"veureu com dansa el pomer."

    return stanza

def getAppleSong(applesCount):

   """

   :param applesCount: Number of apples

   :return: All the song text
   sin for ni while
   """

    if applesCount == 0:
        return "No hi ha pomes al pomer."
    else:
        return "\n\n".join([getAppleSongStanza(i) for i in range(applesCount, 0, -1)])

