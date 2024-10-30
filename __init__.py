from aqt import mw
from anki.collection import Collection
from aqt.utils import showInfo, qconnect
from aqt.qt import *


def test_function():
    ids = mw.col.find_cards("deck:\"JP Mining\"")
    if len(ids):
        card = mw.col.get_card(ids[0])
        showInfo(f"{card.question()}")

action = QAction("test", mw)
qconnect(action.triggered, test_function)
mw.form.menuTools.addAction(action)