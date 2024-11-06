from aqt import mw
from anki.collection import Collection
from aqt.utils import showInfo, qconnect
from aqt.qt import *


def test_function():
    ids = mw.col.find_cards("deck:\"JP Mining\"")
    if len(ids):
        card = mw.col.get_card(ids[0])
        names = ""
        for name, value in card.note().items():
            names += name + "\n"
        pitch_info = card.note()["PAPositions"]
        if pitch_info:
            downstep = pitch_info.find("[") + 14  # hardcoded to find downstep in html PAPosition field

            showInfo(str(pitch_info[downstep]))
        else:
            showInfo("Error: no pa data")


action = QAction("test", mw)
qconnect(action.triggered, test_function)
mw.form.menuTools.addAction(action)