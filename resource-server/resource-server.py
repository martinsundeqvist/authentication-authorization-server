from fastapi import FastAPI
from fastapi.responses import PlainTextResponse

app = FastAPI()

PUBLIC_MOVES = """
-=--=--=--=--=--=--=--=--=--=--=--=--=-
            Grab Moves
-=--=--=--=--=--=--=--=--=--=--=--=--=-

Up, Circle - Airwalk
Up/Right, Circle - Rocket Air
Right, Circle - Indy
Right/Down, Circle - Madonna
Down, Circle - Indy Stiffy
Down/Left, Circle - Benihana
Left, Circle - Crossbone
Up/Left, Circle - Judo
"""

SECRET_MOVES = """
-=--=--=--=--=--=--=--=--=--=--=--=--=-
             Secret Moves
-=--=--=--=--=--=--=--=--=--=--=--=--=-

Left, Right, Square - Nollie Underflip
Left, Right, Circle - Pogo Air
Right, Left, Circle - Christ Air
Left, Right, Triangle - Heelflip Darkslide
Right, Left, Triangle - Layback Grind
"""

@app.get("/combo-moves", response_class=PlainTextResponse)
def read_root():
    moves = PUBLIC_MOVES + '\n' + SECRET_MOVES
    return moves
